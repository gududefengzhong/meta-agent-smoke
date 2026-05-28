RETRYABLE_STATUS_CODES = {500, 502, 503, 504}


def should_retry(status_code: int, attempt: int, max_attempts: int) -> bool:
    if attempt > max_attempts:
        return False
    return status_code in RETRYABLE_STATUS_CODES
