import re


_AUTH_RE = re.compile(r"Bearer\s+\S+")


def redact_authorization(header: str) -> str:
    return _AUTH_RE.sub("Bearer <redacted>", header)
