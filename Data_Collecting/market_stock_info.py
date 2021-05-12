from requests import get
from datetime import datetime


def grab_stock_info(ticker):
    info = dict()
    intraday = Intraday(ticker)
    # daily = Daily(ticker)
    overview = Overview(ticker)

    info['Symbol'] = ticker
    info['intraday'] = intraday
    # info['daily'] = daily
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
    url = f'https://api.marketstack.com/v1/intraday?access_key=61578059aad857bacd9150dc716b8c82&symbols={ticker}&interval=1min&limit=500'
    response = get(url)
    info = response.json()

    if 'data' in info:
        data = info['data']
        intraday = []
        for curr in data:
            if curr['last']:
                date_obj = datetime.strptime(curr['date'], '%Y-%m-%dT%H:%M:%S+%f')
                curr['date'] = datetime.strftime(date_obj, '%Y-%m-%d %H:%M')
                intraday.append(curr)
        return intraday

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=1min&apikey=75NGNLOY2P6P3HT4'
    response = get(url)
    info = response.json()
    if 'Time Series (1min)' in info:
        data = info['Time Series (1min)']
        intraday = []
        for cur_key, cur_value in data.items():
            date_obj = datetime.strptime(cur_key, '%Y-%m-%d %H:%M:%S')
            cur_value.update({'date': datetime.strftime(date_obj, '%Y-%m-%d %H:%M')})
            cur_value['open'] = float(cur_value.pop('1. open'))
            cur_value['high'] = float(cur_value.pop('2. high'))
            cur_value['low'] = float(cur_value.pop('3. low'))
            cur_value['last'] = float(cur_value.pop('4. close'))
            cur_value['volume'] = float(cur_value.pop('5. volume'))
            intraday.append(cur_value)

        return intraday
    return None
    # for key, value in final.items():
    #     print(f'{key} -- {value}')


# @Param: None
# API call that fetches the Daily Open High Low Close and Volume for a given Ticker
# @Return: Python dictionary
def Daily(ticker):
    url = f'https://api.marketstack.com/v1/eod?access_key=61578059aad857bacd9150dc716b8c82&symbols={ticker}'
    response = get(url)
    info = response.json()

    if 'data' not in info:
        return None

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

    if 'Symbol' not in overview:
        return None

    return overview

    # for key, value in overview.items():
    #     print(f'{key} -- {value}')



# A test function to test the functions inside the Ticker class
# def test():
#     # Intraday('LGHL')
#     # Daily('AAPL')
#     # Overview('LGHL')
#     # Quote('LGHL')
#     # RealTimeData('AAPL')
