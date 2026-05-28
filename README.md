# meta-agent-smoke

Smoke repository for `meta-agent` bug-fix runs.

## Why not keep all broken cases on one branch?

The current `bug_fix` path uses the built-in `python_test` verifier, and that
verifier runs repository-wide `pytest`. If one branch intentionally contains
multiple unrelated failing cases, fixing one bug still leaves the other tests
red, so the agent cannot reach a green terminal state.

For that reason this repo uses:

- `master` as the catalog branch
- one runnable bug case per `case/*` branch

## Cases

- `case/py-greet-format`
- `case/py-discount-validation`
- `case/py-clamp-boundary`
- `case/py-slugify-normalization`
- `case/py-parse-bool`
- `case/py-mutable-default`

## Submit payload template

```json
{
  "issue_description": "<replace me>",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "<replace me>",
  "target_files": ["<replace me>"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```
