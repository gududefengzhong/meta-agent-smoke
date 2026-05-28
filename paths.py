from pathlib import Path


def safe_join(root: str, relative: str) -> Path:
    return Path(root) / relative
