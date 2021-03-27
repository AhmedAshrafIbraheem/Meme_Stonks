from requests import get
import tweepy as tw
import re


consumer_key = 'Dvkp7foIvb2EMqxFoXCqcD4YZ'
consumer_secret = 'gs0w56HCcSwuWJEyVKXL0ywv9ibE1R98ZomPUyDSbtl7kDy4sv'
access_token = '1371241350746755074-zbpTUM7DqzTxie9tJ5VOvbVYSZ1CAI'
access_token_secret = '9EazuwZG4XEnBR5eInRBqE1BzpEV72iJLoF8OzGzZBBnT'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# TODO: Twitter code to be written here returned as a dictionary
def get_social_stock_info(ticker):
    pass


##
