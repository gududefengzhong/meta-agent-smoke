from datetime import datetime, timezone

from recent import is_recent


def test_is_recent_treats_naive_timestamps_as_utc() -> None:
    now = datetime(2026, 5, 28, 12, 0, 0, tzinfo=timezone.utc)

    assert is_recent("2026-05-28T11:59:45", now, 60) is True
    assert is_recent("2026-05-28T11:58:30Z", now, 60) is False
