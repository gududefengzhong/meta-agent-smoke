from pathlib import Path


def safe_join(root: str, relative: str) -> Path:
    """Join paths safely, rejecting path traversal and absolute paths."""
    path = Path(root) / relative
    
    # Convert to absolute paths for comparison
    root_abs = Path(root).resolve()
    resolved_path = path.resolve()
    
    # Check if the resolved path is outside the root directory
    try:
        resolved_path.relative_to(root_abs)
    except ValueError:
        raise ValueError(f"Path traversal attempt detected: {relative}")
    
    # Reject absolute paths
    if Path(relative).is_absolute():
        raise ValueError(f"Absolute paths are not allowed: {relative}")
    
    return path
