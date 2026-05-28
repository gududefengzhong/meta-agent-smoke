from pathlib import Path

import pytest

from paths import safe_join


def test_safe_join_allows_normal_child_paths(tmp_path) -> None:
    result = safe_join(str(tmp_path), "reports/output.txt")

    assert result == Path(tmp_path) / "reports" / "output.txt"


def test_safe_join_rejects_path_traversal(tmp_path) -> None:
    with pytest.raises(ValueError):
        safe_join(str(tmp_path), "../../etc/passwd")

    with pytest.raises(ValueError):
        safe_join(str(tmp_path), "/etc/passwd")
