from requests import get


# TODO: call all functions together and append it to one dictionary
def grab_stock_info(ticker):
    info = dict()
    intraday = Intraday(ticker)
    daily = Daily(ticker)
    overview = Overview(ticker)

    info['intraday'] = intraday
    info['daily'] = daily
    info['overview'] = overview

    return info

    # for key, value in info.items():
    #     print(f'{key} -- {value}')




    # info = {"price": 23}
    # kol = {"volume": 43}
    # info.update(kol)
    # info {"price": 23, "volume": 43}

# # @Param: None
# # API call that fetches the intraday(1 Min, 5 Min, 15 Min, 30 Min, 60 Min) Open High Low Close and
# # Volume for a given Ticker and*Includes extended trading hours*
# # @Return: Python dictionary
def Intraday(ticker):
    url = f'https://api.marketstack.com/v1/intraday?access_key=61578059aad857bacd9150dc716b8c82&symbols={ticker}&interval=1min'
    response = get(url)
    info = response.json()
    data = info['data']
    time = []

    for i in range(len(data)):
        time.append(data[i]['date'])

    intraday = dict(zip(time,data))

    return intraday

    # for key, value in final.items():
    #     print(f'{key} -- {value}')


# @Param: None
# API call that fetches the Daily Open High Low Close and Volume for a given Ticker
# @Return: Python dictionary
def Daily(ticker):
    url = f'https://api.marketstack.com/v1/eod?access_key=61578059aad857bacd9150dc716b8c82&symbols={ticker}'
    response = get(url)
    info = response.json()
    data = info['data']
    time = []

    for i in range(len(data)):
        time.append(data[i]['date'])

    daily = dict(zip(time, data))

    return daily


    # for key, value in info.items():
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


# def SMA(ticker):


# A test function to test the functions inside the Ticker class
# def test():
#     # Intraday('LGHL')
#     # Daily('AAPL')
#     # Overview('LGHL')
#     # Quote('LGHL')
#     # RealTimeData('AAPL')


if __name__ == '__main__':
    grab_stock_info('AAPL')
