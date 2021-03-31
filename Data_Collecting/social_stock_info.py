# social_stock_info.py
# slamstonks.com
# ...
# ...
#from requests import get
#import tweepy
#import re
import pandas as pd
from pytrends.request import TrendReq


# THE CODE TO DO THIS IS NOT DONE YET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# pull top_10 stocks from db or from the controller that calls this and the mw scraper:
top_10_stocks = ["LAZR", "KMPH", "TMBR", "EYES", "FBRX", "ROOT", "OTRK", "HJLI", "PUBM", "ASO"]

############################################################
#
### AVERAGER ###############################################
# Accepts a ticker dictionary that has hours per day and a
# corresponding value. These hour values are averaged for
# the day and returned in a dictionary.
def averager(ticker_dictionary):
    dictionary_to_return = {}  # loads nested_dictionary_return when full and empties for next ticker
    popping_from_ticker = ticker_dictionary.popitem()  # pops a tuple from into the var
    current_date = popping_from_ticker[0].strftime("%Y-%m-%d")  # string
    counter = popping_from_ticker[1]  # int
    counter_for_avg = 1
    while (len(ticker_dictionary) > 0):
        popping_from_ticker = ticker_dictionary.popitem()
        temp_current_date = popping_from_ticker[0].strftime("%Y-%m-%d")
        if temp_current_date == current_date:
            counter_for_avg += 1
            counter += popping_from_ticker[1]
        if temp_current_date != current_date:
            dictionary_to_return.update({current_date: counter / counter_for_avg})
            current_date = temp_current_date
            counter = popping_from_ticker[1]
            counter_for_avg = 1
        if len(ticker_dictionary) == 0:
            dictionary_to_return.update({current_date: counter / counter_for_avg})

    # print(dictionary_to_return)

    return dictionary_to_return
# END averager


############################################################
# ......................................................................................................................
### GOOGLE TRENDS ALL ######################################
# pytrends, pandas (dataframe, timeframe)
# returns a nested dictonary containing data needed for
# comparing the relative frequency of tickers compared to
# each other.
# Very helpful: https://towardsdatascience.com/telling-stories-with-google-trends-using-pytrends-in-python-a11e5b8a177
def google_trends_normalized(top_10_stocks):
    # reference keyword is the last element in top_10_stocks
    first_three_tickers = top_10_stocks[0:3]
    first_three_tickers.append(top_10_stocks[9])
    second_three_tickers = top_10_stocks[3:6]
    second_three_tickers.append(top_10_stocks[9])
    last_four_tickers = top_10_stocks[6:10]

    # Only need to load this one time for following operations:
    pytrends = TrendReq()
    # pull 1
    kw_list = first_three_tickers
    pytrends.build_payload(kw_list, cat=7, timeframe='now 7-d', geo='US', gprop='')
    interest_over_time_1_df = pytrends.interest_over_time()
    interest_over_time_1_df.rename(columns={top_10_stocks[9]: top_10_stocks[9] + '1'}, inplace=True)
    del interest_over_time_1_df['isPartial']
    #print(interest_over_time_1_df.head())        # useful for error testing
    # pull 2
    kw_list = second_three_tickers
    pytrends.build_payload(kw_list, cat=7, timeframe='now 7-d', geo='US', gprop='')
    interest_over_time_2_df = pytrends.interest_over_time()
    interest_over_time_2_df.rename(columns={top_10_stocks[9]: top_10_stocks[9] + '2'}, inplace=True)
    del interest_over_time_2_df['isPartial']
    #print(interest_over_time_2_df.head())      # useful for error testing
    # pull 3
    kw_list = last_four_tickers
    pytrends.build_payload(kw_list, cat=7, timeframe='now 7-d', geo='US', gprop='')
    interest_over_time_3_df = pytrends.interest_over_time()
    interest_over_time_3_df.rename(columns={top_10_stocks[9]: top_10_stocks[9] + '3'}, inplace=True)
    del interest_over_time_3_df['isPartial']
    #print(interest_over_time_3_df.head())     # useful for error testing

    master_df = pd.concat([interest_over_time_1_df.reset_index(), interest_over_time_2_df.reset_index(), interest_over_time_3_df.reset_index()], axis=1)
    master_df = master_df.loc[:,~master_df.columns.duplicated()]
    master_df.set_index('date', inplace=True)
    #print(master_df.to_string())

    nested_dictionary = {}

    tickers_plus_normalizers_list = list(master_df.columns)

    #print(tickers_plus_normalizers_list)

    for x in tickers_plus_normalizers_list:
        # prepping variables for the coming while loop that uses them. We need to get the current_date before we can
        # cycle through the dictionary. current_date is critical to successful execution.
        ticker_only_dictionary = master_df.to_dict().get(x) # grabs the ticker dictionary from the dataframe
        #print(ticker_only_dictionary)
        nested_dictionary.update({x: averager(ticker_only_dictionary)})

    #print(nested_dictionary)

    for_loop_counter = 0
    for x in tickers_plus_normalizers_list:
        #print(x)
        if for_loop_counter < 3:
            for xx in nested_dictionary[x]:
                nested_dictionary[x][xx] = round((float(nested_dictionary[x][xx]) + .01) * (float(nested_dictionary[tickers_plus_normalizers_list[7]][xx]) + .01) / (float(nested_dictionary[tickers_plus_normalizers_list[3]][xx]) + .01), 2)
                #print(x, xx, nested_dictionary[x][xx], sep="\t\t\t")
        if for_loop_counter == 3:
            for xx in nested_dictionary[x]:
                nested_dictionary[x][xx] = round(nested_dictionary[x][xx], 2)
                #print(x, xx, nested_dictionary[x][xx], sep="\t\t\t")
        if for_loop_counter > 3 and for_loop_counter < 7:
            for xx in nested_dictionary[x]:
                nested_dictionary[x][xx] = round((float(nested_dictionary[x][xx]) + .01) * (float(nested_dictionary[tickers_plus_normalizers_list[3]][xx]) + .01) / (float(nested_dictionary[tickers_plus_normalizers_list[7]][xx]) + .01), 2)
                #print(x, xx, nested_dictionary[x][xx], sep="\t\t\t")
        #if for_loop_counter == 7:
            #for xx in nested_dictionary[x]:
                #print(x, xx, nested_dictionary[x][xx], sep="\t\t\t")
        if for_loop_counter > 7 and for_loop_counter < 11:
            for xx in nested_dictionary[x]:
                nested_dictionary[x][xx] = round((float(nested_dictionary[x][xx]) + .01) * (float(nested_dictionary[tickers_plus_normalizers_list[3]][xx]) + .01) / (float(nested_dictionary[tickers_plus_normalizers_list[11]][xx]) + .01), 2)
                #print(x, xx, nested_dictionary[x][xx], sep="\t\t\t")

        for_loop_counter += 1

    nested_dictionary.pop(tickers_plus_normalizers_list[7])
    nested_dictionary.pop(tickers_plus_normalizers_list[11])
    remove_the_digit = tickers_plus_normalizers_list[3][:-1]
    temp_dictionary = {remove_the_digit: nested_dictionary[tickers_plus_normalizers_list[3]]}
    nested_dictionary.update(temp_dictionary)
    nested_dictionary.pop(tickers_plus_normalizers_list[3])
    del temp_dictionary

    #print(nested_dictionary)

    return nested_dictionary
# END google_trends_normalized


def google_trends(ticker):
    # Only need to load this one time for following operations:
    pytrends = TrendReq()

    # Will get back to the commented-out code below after MVP:
    # # Get Google Hot Trends data
    # today_searches_df = pytrends.today_searches()
    # print(today_searches_df.to_string())

    kw_list = [ticker]
    # check pytrends documentation as well as the embedded code snippet from
    # trends.google.com to find proper pararmeters/formatting
    pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='US', gprop='')
    interest_over_time_df = pytrends.interest_over_time()
    #print(interest_over_time_df.head())        # useful for error testing

    # prepping variables for the coming while loop that uses them. We need to get the current_date before we can
    # cycle through the dictionary. current_date is critical to successful execution.
    ticker_only_dictionary = interest_over_time_df.to_dict().get(ticker) # grabs the ticker dictionary from the dataframe
    # print(interest_over_time_df.to_string())
    return averager(ticker_only_dictionary)
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
    #print(google_trends_normalized(top_10_stocks))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# END social_stock_info.py