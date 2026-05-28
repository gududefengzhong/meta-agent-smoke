from pathlib import Path


def safe_join(root: str, relative: str) -> Path:
    if relative.startswith('/') or '..' in relative.split('/'):
        raise ValueError('Path traversal detected')
    return Path(root) / relative