import json


def parse_event(raw: str) -> dict[str, object]:
    data = json.loads(raw)
    return {
        "name": data["name"],
        "enabled": bool(data.get("enabled", False)),
        "retries": int(data.get("retries", 0)),
    }
