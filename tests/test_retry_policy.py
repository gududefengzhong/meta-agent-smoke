from retry_policy import should_retry


def test_should_retry_only_transient_errors_with_remaining_budget() -> None:
    assert should_retry(503, attempt=1, max_attempts=3) is True
    assert should_retry(429, attempt=1, max_attempts=3) is True
    assert should_retry(401, attempt=1, max_attempts=3) is False
    assert should_retry(503, attempt=3, max_attempts=3) is False
