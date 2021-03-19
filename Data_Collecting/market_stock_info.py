from requests import get


# TODO: call all functions together and append it to one dictionary
def grab_stock_info(ticker):
    pass
    # info = {"price": 23}
    # kol = {"volume": 43}
    # info.update(kol)
    # info {"price": 23, "volume": 43}


# @Param: None
# API call that fetches the intraday(1 Min, 5 Min, 15 Min, 30 Min, 60 Min) Open High Low Close and
# Volume for a given Ticker and*Includes extended trading hours*
# @Return: Python dictionary
def Intraday(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}' \
          f'&interval=1min&adjusted=false&outputsize=full&apikey=75NGNLOY2P6P3HT4'
    response = get(url)
    info = response.json()

    intraday = info['Time Series (1min)']

    return intraday

    # for key, value in series.items():
    #     print(f'{key} -- {value}')


# @Param: None
# API call that fetches the Daily Open High Low Close and Volume for a given Ticker
# @Return: Python dictionary
def Daily(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey=75NGNLOY2P6P3HT4'
    response = get(url)
    info = response.json()

    daily = info['Time Series (Daily)']

    return daily

    # for key, value in series.items():
    #     print(f'{key} -- {value}')


# @Param: None
# API call that fetches the fundamental details/company overview for a given Ticker
# @Return: Python dictionary
def Overview(ticker):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey=75NGNLOY2P6P3HT4'
    response = get(url)
    overview = response.json()

    return overview

    # for key, value in overview.items():
    #     print(f'{key} -- {value}')


# @Param: None
# API call that fetches a quote for a given Ticker from the most recent trading day
# @Return: Python dictionary
def Quote(ticker):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey=75NGNLOY2P6P3HT4'
    response = get(url)
    info = response.json()

    Quote = info['Global Quote']

    return Quote

    # for key, value in Quote.items():
    #     print(f'{key} -- {value}')


# A test function to test the functions inside the Ticker class
def test():
    Intraday('LGHL')
    # Daily('LGHL')
    # Overview('LGHL')
    # Quote('LGHL')


# if __name__ == '__main__':
#     test()
