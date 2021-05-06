from social_stock_info import get_social_stock_info
from market_stock_info import grab_stock_info
from stock_class import StockData


def analyze(ticker_info):
    ticker = ticker_info[0]

    scraped = {"Symbol": ticker_info[0], "Name": ticker_info[1],
               "Short Interest": ticker_info[3], "Float Shorted": ticker_info[4]}

    market_info = grab_stock_info(ticker)
    scraped.update(market_info)

    social_info = get_social_stock_info(ticker)
    scraped.update(social_info)

    return StockData(scraped)
