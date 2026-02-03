def validate_order(order_type, quantity, price):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")
