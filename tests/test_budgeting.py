from budgeting import accumulate_cost_micros


def test_accumulate_cost_micros_rounds_up_fractional_values() -> None:
    assert accumulate_cost_micros([0.0000004, 0.0000012]) == 3
