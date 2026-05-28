#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import shlex
from pathlib import Path


def _load_cases(catalog_path: Path) -> list[dict[str, object]]:
    raw = json.loads(catalog_path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise SystemExit("catalog must be a JSON array")
    cases: list[dict[str, object]] = []
    for item in raw:
        if not isinstance(item, dict):
            raise SystemExit("catalog entries must be JSON objects")
        cases.append(item)
    return cases


def _select_cases(
    cases: list[dict[str, object]],
    *,
    selected_cases: set[str],
    selected_batches: set[str],
    selected_categories: set[str],
) -> list[dict[str, object]]:
    filtered: list[dict[str, object]] = []
    for case in cases:
        name = str(case.get("case", ""))
        batch = str(case.get("batch", ""))
        categories = {
            str(item)
            for item in case.get("categories", [])
            if isinstance(item, str)
        }
        if selected_cases and name not in selected_cases:
            continue
        if selected_batches and batch not in selected_batches:
            continue
        if selected_categories and not (categories & selected_categories):
            continue
        filtered.append(case)
    return filtered


def _build_payload(
    case: dict[str, object],
    *,
    repo_url: str,
    verify_suite: str,
    model: str,
) -> dict[str, object]:
    return {
        "issue_description": case["issue_description"],
        "repo_url": repo_url,
        "base_ref": case["case"],
        "target_files": case["target_files"],
        "verify_suite": verify_suite,
        "model": model,
    }


def _render_submit_command(
    payload: dict[str, object],
    *,
    api_url: str,
    token: str,
    task_type: str,
) -> str:
    payload_json = json.dumps(payload, ensure_ascii=False)
    return "\n".join(
        [
            "uv run python -m meta_agent.cli submit \\",
            f"  --task-type {shlex.quote(task_type)} \\",
            f"  --api-url {shlex.quote(api_url)} \\",
            f"  --token {shlex.quote(token)} \\",
            f"  --payload {shlex.quote(payload_json)}",
        ]
    )


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Render meta-agent bug-fix submit commands for smoke cases."
    )
    parser.add_argument(
        "--catalog",
        default=str(repo_root / "catalog" / "cases.json"),
        help="Path to the smoke-case catalog JSON.",
    )
    parser.add_argument(
        "--case",
        dest="cases",
        action="append",
        default=[],
        help="Select a specific case/branch, e.g. case/py-safe-join-traversal.",
    )
    parser.add_argument(
        "--batch",
        dest="batches",
        action="append",
        default=[],
        help="Filter by batch: first, second, third.",
    )
    parser.add_argument(
        "--category",
        dest="categories",
        action="append",
        default=[],
        help="Filter by category tag such as security, performance, or caching.",
    )
    parser.add_argument(
        "--format",
        choices=("submit", "payload", "list"),
        default="submit",
        help="Output format.",
    )
    parser.add_argument(
        "--repo-url",
        default="https://github.com/gududefengzhong/meta-agent-smoke.git",
        help="Repo URL injected into the payload.",
    )
    parser.add_argument(
        "--verify-suite",
        default="python_test",
        help="verify_suite value injected into the payload.",
    )
    parser.add_argument(
        "--model",
        default="deepseek/deepseek-v4-pro",
        help="model value injected into the payload.",
    )
    parser.add_argument(
        "--api-url",
        default="http://localhost:8000",
        help="API base URL used in rendered submit commands.",
    )
    parser.add_argument(
        "--token",
        default="dev-token",
        help="Bearer token used in rendered submit commands.",
    )
    parser.add_argument(
        "--task-type",
        default="bug_fix",
        help="Task type used in rendered submit commands.",
    )
    args = parser.parse_args()

    cases = _load_cases(Path(args.catalog))
    selected = _select_cases(
        cases,
        selected_cases=set(args.cases),
        selected_batches={item.lower() for item in args.batches},
        selected_categories={item.lower() for item in args.categories},
    )
    if not selected:
        raise SystemExit("no cases matched the requested filters")

    chunks: list[str] = []
    for case in selected:
        payload = _build_payload(
            case,
            repo_url=args.repo_url,
            verify_suite=args.verify_suite,
            model=args.model,
        )
        if args.format == "payload":
            rendered = json.dumps(payload, ensure_ascii=False, indent=2)
        elif args.format == "list":
            categories = ", ".join(str(item) for item in case.get("categories", []))
            rendered = f"{case['case']} | batch={case['batch']} | categories={categories}"
        else:
            rendered = _render_submit_command(
                payload,
                api_url=args.api_url,
                token=args.token,
                task_type=args.task_type,
            )
        chunks.append(f"# {case['case']}\n{rendered}")

    print("\n\n".join(chunks))


if __name__ == "__main__":
    main()
