import logging
from ccxt_download import public, CANDLES, TRADES


# Add handler to ccxt_download logger
logger = logging.getLogger("ccxt_download")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("test.log")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

# Download candles
public.download(
    exchange="bybit",
    data_types=[CANDLES, TRADES],
    symbols=[
        "ETH/USDT:USDT",
        "BTC/USDT:USDT",
    ],
    start_date="2023-09-01",
    end_date="2023-09-05",
)
