def discount_price(price: float, discount_percent: float) -> float:
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")
    return price - (price * discount_percent / 100)
