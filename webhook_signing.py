import hmac
import json
from hashlib import sha256


def compute_signature(secret: str, payload: dict[str, object]) -> str:
    body = json.dumps(payload)
    return hmac.new(secret.encode("utf-8"), body.encode("utf-8"), sha256).hexdigest()
