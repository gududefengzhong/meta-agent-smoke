def accumulate_cost_micros(costs_usd: list[float]) -> int:
    total = 0
    for cost in costs_usd:
        total += int(cost * 1_000_000)
    return total
