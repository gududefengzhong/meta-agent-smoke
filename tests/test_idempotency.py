from idempotency import build_idempotency_key


def test_build_idempotency_key_normalizes_tag_order_and_duplicates() -> None:
    left = build_idempotency_key("bug_fix", "tenant-a", ["redis", "python", "redis"])
    right = build_idempotency_key("bug_fix", "tenant-a", ["python", "redis"])

    assert left == right
