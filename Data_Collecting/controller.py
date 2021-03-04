import time
import scraper as scr
import market_stock_info as msi
import social_stock_info as ssi
import analyzer
import store_guy


def controller():
    while True:
        # scrape data from watchmaker
        tickers_list = scr.scraper()
        ordered_list = []

        for curr_ticker in tickers_list:
            market_info = msi.get_market_stock_info(curr_ticker)
            social_info = ssi.get_social_stock_info(curr_ticker)
            refined_stock_data = analyzer.analyze(market_info, social_info)
            ordered_list.append((curr_ticker, refined_stock_data.value))
            store_guy.store_stock(refined_stock_data)

        # sort according ordered_list according to its value
        # store list of tickers in DB
        store_guy.store_tickers(ordered_list)

        # sleep for 60 seconds * 5
        time.sleep(60 * 5)


if __name__ == '__main__':
    controller()
