from event_parser import parse_event


def test_parse_event_normalizes_string_booleans_and_numbers() -> None:
    payload = '{"name": "nightly-sync", "enabled": "false", "retries": "3"}'

    parsed = parse_event(payload)

    assert parsed == {
        "name": "nightly-sync",
        "enabled": False,
        "retries": 3,
    }
