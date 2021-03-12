from social_stock_info import get_social_stock_info
from market_stock_info import get_market_stock_info


class StockData:
    pass


def analyze(ticker):
    market_info = get_market_stock_info(ticker)
    social_info = get_social_stock_info(ticker)

