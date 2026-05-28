def discount_price(price: float, discount_percent: float) -> float:
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError(f"discount_percent must be between 0 and 100, got {discount_percent}")
    return price - (price * discount_percent / 100)