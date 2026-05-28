import pytest

from parse_bool import parse_bool


@pytest.mark.parametrize(("raw", "expected"), [("true", True), ("false", False)])
def test_parse_bool_basic_values(raw: str, expected: bool) -> None:
    assert parse_bool(raw) is expected


@pytest.mark.parametrize(("raw", "expected"), [("1", True), ("0", False), ("yes", True), ("no", False)])
def test_parse_bool_common_aliases(raw: str, expected: bool) -> None:
    assert parse_bool(raw) is expected


def test_parse_bool_rejects_unknown_value() -> None:
    with pytest.raises(ValueError):
        parse_bool("maybe")
