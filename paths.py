from pathlib import Path


def safe_join(root: str, relative: str) -> Path:
    root_path = Path(root).resolve()
    path = Path(root) / relative
    resolved_path = path.resolve()

    # Reject paths that escape the root directory or are absolute
    if not resolved_path.is_relative_to(root_path):
        raise ValueError(f"Path '{relative}' escapes root directory '{root}'")

    return resolved_path
