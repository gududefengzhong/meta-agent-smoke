from datetime import date, timedelta


def next_billing_date(current: date) -> date:
    return current + timedelta(days=30)
