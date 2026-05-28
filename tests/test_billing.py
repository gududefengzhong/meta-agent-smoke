from datetime import date

from billing import next_billing_date


def test_next_billing_date_clamps_to_end_of_shorter_months() -> None:
    assert next_billing_date(date(2024, 1, 31)) == date(2024, 2, 29)
    assert next_billing_date(date(2023, 1, 31)) == date(2023, 2, 28)
    assert next_billing_date(date(2024, 12, 31)) == date(2025, 1, 31)
