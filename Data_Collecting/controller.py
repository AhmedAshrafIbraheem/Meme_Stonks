from time import sleep
from scraper import scraper
from analyzer import analyze
from store_guy import DatabaseInteraction
from stock_class import compare_stocks


def controller():
    # scrape data from watchmaker
    tickers_list = scraper()
    ordered_list = []

    for curr_ticker in tickers_list:
        refined_stock_data = analyze(curr_ticker)
        ordered_list.append(refined_stock_data)
        DatabaseInteraction.get_instance().store_stock(refined_stock_data)

    # sort according ordered_list according to its value
    ordered_list.sort(key=compare_stocks)
    # store list of tickers in DB
    DatabaseInteraction.get_instance().store_top10s(ordered_list)


def looper():
    while True:
        controller()
        # sleep for 60 seconds * 5
        sleep(60 * 5)


if __name__ == '__main__':
    looper()
