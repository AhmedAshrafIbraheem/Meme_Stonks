from time import sleep
from scraper import scraper
from analyzer import analyze
from store_guy import store_stock, store_tickers


def controller():
    # scrape data from watchmaker
    tickers_list = scraper()
    ordered_list = []

    for curr_ticker in tickers_list:
        refined_stock_data = analyze(curr_ticker)
        ordered_list.append(refined_stock_data)
        store_stock(refined_stock_data)

    # sort according ordered_list according to its value
    ordered_list.sort(key=compare_stocks)
    # store list of tickers in DB
    store_tickers(ordered_list)


def compare_stocks(stock1, stock2) -> int:
    # returns 0, 1 or -1
    return 0


def looper():
    while True:
        controller()
        # sleep for 60 seconds * 5
        sleep(60 * 5)


# if __name__ == '__main__':
#    looper()
