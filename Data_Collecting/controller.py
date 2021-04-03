from time import sleep
from scraper import scraper
from analyzer import analyze
from store_guy import DatabaseInteraction
from stock_class import compare_stocks
from social_stock_info import google_trends_normalized


def controller():
    tickers_list = scraper()
    ordered_list = []

    for curr_ticker in tickers_list:
        refined_stock_data = analyze(curr_ticker)
        ordered_list.append(refined_stock_data)
        DatabaseInteraction.get_instance().store_stock(refined_stock_data)

    # sort according ordered_list according to its value
    # ordered_list.sort(key=compare_stocks)
    # store list of tickers in DB
    DatabaseInteraction.get_instance().store_top10s(ordered_list)

    tickers = []
    for ticker in tickers_list:
        tickers.append(ticker[0])

    DatabaseInteraction.get_instance().store_trends(google_trends_normalized(tickers))


def looper():
    while True:
        controller()
        # sleep for 5 minutes
        sleep(5 * 60)


if __name__ == '__main__':
    looper()
