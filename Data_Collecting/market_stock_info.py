from requests import get
import json

class Ticker:

    #@Param: Desired Stock Ticker as a string
    #Initializes a Ticker object from the 'symbol' argument, which accepts a string as a valid argument
    #@Return: None
    def __init__(self, symbol: str):
        self.symbol = symbol

    #@Param: None
    #API call that fetches the intraday(1 Min, 5 Min, 15 Min, 30 Min, 60 Min) Open High Low Close and Volume for a given Ticker and*Includes extended trading hours*
    #@Return: Python dictionary
    def Intraday(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={self.symbol}&interval=1min&adjusted=false&outputsize=full&apikey=75NGNLOY2P6P3HT4'
        response = get(url)
        info = response.json()

        series = info['Time Series (1min)']

        for key, value in series.items():
            print(f'{key} -- {value}')

    # @Param: None
    # API call that fetches the Daily Open High Low Close and Volume for a given Ticker
    # @Return: Python dictionary
    def Daily(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.symbol}&apikey=75NGNLOY2P6P3HT4'
        response = get(url)
        info = response.json()

        series = info['Time Series (Daily)']

        for key, value in series.items():
            print(f'{key} -- {value}')

    # @Param: None
    # API call that fetches the fundamental details/company overview for a given Ticker
    # @Return: Python dictionary
    def Overview(self):
        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={self.symbol}&apikey=75NGNLOY2P6P3HT4'
        response = get(url)
        info = response.json()

        for key, value in info.items():
            print(f'{key} -- {value}')

    # @Param: None
    # API call that fetches a quote for a given Ticker from the most recent trading day
    # @Return: Python dictionary
    def Quote(self):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.symbol}&apikey=75NGNLOY2P6P3HT4'
        response = get(url)
        info = response.json()

        Quote = info['Global Quote']
        print(Quote.keys())

        for key, value in Quote.items():
            print(f'{key} -- {value}')


#A test function to test the functions inside the Ticker class
def test():
    x = Ticker('LGHL')
    x.Intraday()
    x.Daily()
    x.Overview()
    x.Quote()

