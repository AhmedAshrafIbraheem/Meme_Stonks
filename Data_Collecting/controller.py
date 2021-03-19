from time import sleep
from scraper import scraper
from analyzer import analyze
from store_guy import DatabaseInteraction
from stock_class import compare_stocks


def controller(tickers_list):
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
    tickers_list = scraper()
    counter = 0
    while True:
        counter = (counter + 1) % 10
        if counter == 0:
            tickers_list = scraper()

        controller(tickers_list)

        # sleep for 60 seconds
        sleep(60)


# if __name__ == '__main__':
#     looper()
