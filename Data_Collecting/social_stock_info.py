from requests import get
import tweepy
import re
import pandas as pd
import time
from pytrends.request import TrendReq

# THE CODE TO DO THIS IS NOT DONE YET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# pull top_10 stocks from db or from the controller that calls this and the mw scraper:
top_10_stocks = ["LAZR", "KMPH", "TMBR", "EYES", "FBRX", "ROOT", "OTRK", "HJLI", "PUBM", "ASO"]


############################################################
# should be run once every 10 minutes (same time as marketwatch scraper)...
### GOOGLE TRENDS ##########################################
# pytrends, pandas (dataframe, timeframe), time
# returns a nested dictionary containing tickers and their
# individual trending percentages for the last seven days
# (including today)
def google_trends():
    # Only need to load this one time for following operations:
    pytrends = TrendReq()

    # Will get back to the commented-out code below after MVP:
    # # Get Google Hot Trends data
    # today_searches_df = pytrends.today_searches()
    # print(today_searches_df.to_string())

    nested_dictionary_return = {}

    for x in top_10_stocks:
        kw_list = [x]
        # check pytrends documentation as well as the embedded code snippet from
        # trends.google.com to find proper pararmeters/formatting
        pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='US', gprop='')
        interest_over_time_df = pytrends.interest_over_time()
        #print(interest_over_time_df.head())        # useful for error testing

        # prepping variables for the coming while loop that uses them. We need to get the current_date before we can
        # cycle through the dictionary. current_date is critical to successful execution.
        ticker_only_dictionary = interest_over_time_df.to_dict().get(x) # grabs the ticker dictionary from the dataframe
        ###
        print(interest_over_time_df.to_string())
        ###
        temp_dictionary = {}        # loads nested_dictionary_return when full and empties for next ticker
        popping_from_ticker = ticker_only_dictionary.popitem()      # pops a tuple from into the var
        current_date = popping_from_ticker[0].strftime("%Y-%m-%d")      # string
        counter = popping_from_ticker[1]        # int
        counter_for_avg = 1
        while(len(ticker_only_dictionary) > 0):
            popping_from_ticker = ticker_only_dictionary.popitem()
            temp_current_date = popping_from_ticker[0].strftime("%Y-%m-%d")
            if temp_current_date == current_date:
                counter_for_avg += 1
                counter += popping_from_ticker[1]
            if temp_current_date != current_date:
                print(str(counter) + " " + str(counter_for_avg) + " ")
                temp_dictionary.update({current_date: counter / counter_for_avg})
                current_date = temp_current_date
                counter = popping_from_ticker[1]
                counter_for_avg = 1
            if len(ticker_only_dictionary) == 0:
                temp_dictionary.update({current_date: counter / counter_for_avg})
                nested_dictionary_return.update({x: temp_dictionary})

        print(nested_dictionary_return)
        time.sleep(1)       # No reason to rush google!

    return nested_dictionary_return
# END google_trends


############################################################
# should be run once every 10 minutes (same time as marketwatch scraper)...
### TWITTER ################################################
############################################################
# ...
def twitter():
    # consumer_key = 'Dvkp7foIvb2EMqxFoXCqcD4YZ'
    # consumer_secret = 'gs0w56HCcSwuWJEyVKXL0ywv9ibE1R98ZomPUyDSbtl7kDy4sv'
    # access_token = '1371241350746755074-zbpTUM7DqzTxie9tJ5VOvbVYSZ1CAI'
    # access_token_secret = '9EazuwZG4XEnBR5eInRBqE1BzpEV72iJLoF8OzGzZBBnT'
    #
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth, wait_on_rate_limit=True)
    #
    # try:
    #     api.verify_credentials()
    #     print("Authentication OK")
    # except:
    #     print("Error during authentication\n\n\n")
    #
    # #trends
    # trends_result = api.trends_place(1)
    # for trend in trends_result[0]["trends"]:
    #     print(trend["name"])
    #
    # print('\n')
    #
    # #cursor
    # # Collect tweets
    # search_words = "gme"
    # date_since = "2021-03-27"
    # tweets = tweepy.Cursor(api.search,
    #               q=search_words,
    #               lang="en",
    #               since=date_since).items(100)
    #
    # # Iterate and print tweets
    # for tweet in tweets:
    #     print(tweet.text)
    pass
# END twitter


# TODO: Twitter code to be written here returned as a dictionary
def get_social_stock_info(ticker):
    pass


def test():
    pass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print(google_trends())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# END social_stock_info.py
