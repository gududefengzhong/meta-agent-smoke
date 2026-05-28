from webhook_signing import compute_signature


def test_compute_signature_is_stable_for_semantically_identical_json() -> None:
    left = {"task_id": "t1", "status": "awaiting_approval"}
    right = {"status": "awaiting_approval", "task_id": "t1"}

    assert compute_signature("secret", left) == compute_signature("secret", right)
