from datetime import datetime


def is_recent(event_time: str, now: datetime, window_seconds: int) -> bool:
    event_dt = datetime.fromisoformat(event_time)
    age = (now - event_dt).total_seconds()
    return 0 <= age <= window_seconds
