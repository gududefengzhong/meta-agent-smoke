from clamp import clamp


def test_clamp_inside_range() -> None:
    assert clamp(50, 10, 100) == 50


def test_clamp_below_range() -> None:
    assert clamp(5, 10, 100) == 10


def test_clamp_equal_to_min() -> None:
    assert clamp(10, 10, 100) == 10


def test_clamp_equal_to_max() -> None:
    assert clamp(100, 10, 100) == 100


def test_clamp_above_range() -> None:
    assert clamp(120, 10, 100) == 100
