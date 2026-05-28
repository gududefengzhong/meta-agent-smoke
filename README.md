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
- `case/py-file-write-parent-dir`
- `case/py-json-enabled-normalization`
- `case/py-next-billing-date`
- `case/py-safe-join-traversal`
- `case/py-compress-ranges-duplicates`
- `case/py-csv-quoted-fields`
- `case/py-http-retry-policy`
- `case/py-template-cache-version`
- `case/py-shell-command-quoting`
- `case/py-recent-window-naive-utc`
- `case/py-page-slice-has-more`
- `case/py-webhook-signature-canonical-json`
- `case/py-idempotency-key-stable-tags`
- `case/py-budget-round-up-micros`
- `case/py-redact-bearer-case-insensitive`
- `case/py-merge-chunks-finish-reason`

## Coverage

This repo intentionally spreads bug categories across small, single-purpose
branches so `meta-agent` can be exercised against more realistic engineering
failure modes without cross-test contamination.

### Batch 1: core code-fix primitives

- output formatting / string formatting
- input validation / business rules
- boundary conditions / numeric logic
- text normalization
- config parsing
- Python mutable state pitfalls

### Batch 2: repository-local engineering bugs

- file I/O and parent-directory handling
- JSON / config normalization
- date and leap-year boundaries
- path traversal safety
- non-termination / performance pathologies
- CSV / serialization parsing

### Batch 3: more production-shaped engineering bugs

- HTTP retry policy
- cache staleness and version invalidation
- shell quoting for subprocess commands
- timezone-aware / naive datetime handling
- pagination contract correctness

### Batch 4: agent-platform and integration bugs

- webhook signature canonicalization
- idempotency key stability
- budget / cost rounding
- secret redaction semantics
- streaming chunk merge correctness

The machine-readable source of truth for all cases lives in
[`catalog/cases.json`](catalog/cases.json).

## Command generator

Do not hand-maintain submit commands for every case. Use the generator instead:

```bash
python scripts/render_submit_commands.py --format list
```

Examples:

```bash
# render submit commands for every third-batch case
python scripts/render_submit_commands.py --batch third

# render only security and performance-oriented cases
python scripts/render_submit_commands.py --category security --category performance

# render just one payload JSON block
python scripts/render_submit_commands.py \
  --case case/py-safe-join-traversal \
  --format payload
```

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

## Ready-to-run payloads

The sections below are examples. The generator script above is the preferred
way to produce current `meta_agent.cli submit` commands.

### `case/py-greet-format`

```json
{
  "issue_description": "The greeting output format is wrong. Fix it so greet(\"world\") returns \"Hello, world!\" and greet(\"Alice\") returns \"Hello, Alice!\".",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-greet-format",
  "target_files": ["greet.py", "tests/test_greet.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-discount-validation`

```json
{
  "issue_description": "Add input validation for discount_percent. Values below 0 or above 100 must raise ValueError, and the error message should mention discount_percent.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-discount-validation",
  "target_files": ["discount.py", "tests/test_discount.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-clamp-boundary`

```json
{
  "issue_description": "Fix the clamp boundary logic so values exactly on the max boundary and above the max boundary both return max_value.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-clamp-boundary",
  "target_files": ["clamp.py", "tests/test_clamp.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-slugify-normalization`

```json
{
  "issue_description": "Fix slugify normalization. It should trim outer whitespace, collapse repeated spaces, lowercase the text, and join words with single hyphens.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-slugify-normalization",
  "target_files": ["slugify.py", "tests/test_slugify.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-parse-bool`

```json
{
  "issue_description": "Fix parse_bool so it accepts common boolean string forms like true/false, 1/0, yes/no, and raises ValueError for unknown inputs.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-parse-bool",
  "target_files": ["parse_bool.py", "tests/test_parse_bool.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-mutable-default`

```json
{
  "issue_description": "Fix the state leak caused by a mutable default argument. Each call should behave independently unless an explicit list is passed in.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-mutable-default",
  "target_files": ["accumulator.py", "tests/test_accumulator.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-file-write-parent-dir`

```json
{
  "issue_description": "Fix write_report so it creates missing parent directories before writing the UTF-8 report file.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-file-write-parent-dir",
  "target_files": ["report_store.py", "tests/test_report_store.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-json-enabled-normalization`

```json
{
  "issue_description": "Fix parse_event so JSON payload fields are normalized correctly: string booleans like \"false\" should become False, and string retry counts should become integers.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-json-enabled-normalization",
  "target_files": ["event_parser.py", "tests/test_event_parser.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-next-billing-date`

```json
{
  "issue_description": "Fix next_billing_date so monthly renewal keeps the same day-of-month when possible and clamps to the end of shorter months, including leap-year February.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-next-billing-date",
  "target_files": ["billing.py", "tests/test_billing.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-safe-join-traversal`

```json
{
  "issue_description": "Fix safe_join so it rejects path traversal and absolute paths instead of allowing callers to escape the provided root directory.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-safe-join-traversal",
  "target_files": ["paths.py", "tests/test_paths.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-compress-ranges-duplicates`

```json
{
  "issue_description": "Fix compress_ranges so duplicated numbers do not cause a hang. The function should merge consecutive values and tolerate duplicates without entering an infinite loop.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-compress-ranges-duplicates",
  "target_files": ["ranges.py", "tests/test_ranges.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```

### `case/py-csv-quoted-fields`

```json
{
  "issue_description": "Fix parse_csv_row so commas inside quoted CSV fields are preserved instead of splitting the field in the middle.",
  "repo_url": "https://github.com/gududefengzhong/meta-agent-smoke.git",
  "base_ref": "case/py-csv-quoted-fields",
  "target_files": ["csv_reader.py", "tests/test_csv_reader.py"],
  "verify_suite": "python_test",
  "model": "deepseek/deepseek-v4-pro"
}
```
