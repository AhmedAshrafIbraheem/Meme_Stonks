from social_stock_info import google_trends
from market_stock_info import grab_stock_info
from stock_class import StockData


def analyze(ticker_info):
    ticker = ticker_info[0]

    scraped = {"Symbol": ticker_info[0], "Name": ticker_info[1],
               "Short Interest": ticker_info[3], "Float Shorted": ticker_info[4]}

    market_info = grab_stock_info(ticker)
    scraped.update(market_info)

    social_info = google_trends(ticker)
    scraped['social'] = social_info

    return StockData(scraped)
