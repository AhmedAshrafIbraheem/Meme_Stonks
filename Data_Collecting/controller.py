from time import sleep
from scraper import scraper
from analyzer import analyze
from store_guy import DatabaseInteraction
from social_stock_info import google_trends_normalized


def controller():
    tickers_list = scraper()
    ordered_list = []
    twitter_data = []

    for curr_ticker in tickers_list:
        refined_stock_data = analyze(curr_ticker)
        twitter_data.append(refined_stock_data.get_all()['twitter'])
        ordered_list.append(refined_stock_data)
        DatabaseInteraction.get_instance().store_stock(refined_stock_data)

    DatabaseInteraction.get_instance().store_top10s(ordered_list)

    tickers = []
    for ticker in tickers_list:
        tickers.append(ticker[0])

    sentiment = {'GoogleTrends': google_trends_normalized(tickers),
                 'Twitter': twitter_data}

    DatabaseInteraction.get_instance().store_sentiment(sentiment)


def looper():
    while True:
        controller()
        # sleep for 10 minutes
        sleep(10 * 60)


if __name__ == '__main__':
    looper()
