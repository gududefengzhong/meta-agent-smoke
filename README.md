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

## Ready-to-run payloads

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
