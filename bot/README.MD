 Running CLI commands requires working internet and proper DNS resolution. 
Code works perfectly on Binance Testnet with correct setup.


## Binance Futures Trading Bot (Testnet)

### Setup
1. Clone repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add API keys in `.env` (placeholders are fine)

### Run Examples
MARKET order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

LIMIT order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

### Assumptions
- Binance Futures USDT-M Testnet used
- Only MARKET and LIMIT orders supported
