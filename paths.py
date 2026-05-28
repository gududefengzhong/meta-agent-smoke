from pathlib import Path
import os


def safe_join(root: str, relative: str) -> Path:
    if os.path.isabs(relative):
        raise ValueError("Absolute paths are not allowed")
    
    resolved = Path(root) / relative
    if not Path(root).resolve() in Path(resolved).resolve().parents:
        raise ValueError("Path traversal is not allowed")
    
    return resolved
