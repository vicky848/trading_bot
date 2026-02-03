import argparse
import logging
from bot.client import get_client
from bot.orders import place_order
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    client = get_client()
    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("Order Placed Successfully")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))

except Exception as e:
    logging.error(str(e))
    print("Error:", e)
