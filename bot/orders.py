import logging
from .validators import validate_order

def place_order(client, symbol, side, order_type, quantity, price=None):
    validate_order(order_type, quantity, price)

    logging.info(f"Placing {order_type} order: {symbol} {side}")

    if order_type == "MARKET":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
    else:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

    logging.info(f"Order Response: {order}")
    return order
