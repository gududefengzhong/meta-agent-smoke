import pytest

from discount import discount_price


def test_discount_normal() -> None:
    assert discount_price(100, 20) == 80


def test_discount_zero() -> None:
    assert discount_price(100, 0) == 100


def test_discount_full() -> None:
    assert discount_price(100, 100) == 0


def test_discount_negative_raises() -> None:
    with pytest.raises(ValueError, match="discount_percent"):
        discount_price(100, -10)


def test_discount_over_100_raises() -> None:
    with pytest.raises(ValueError, match="discount_percent"):
        discount_price(100, 150)
