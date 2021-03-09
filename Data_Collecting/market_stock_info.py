import requests
import json

def get_market_stock_info(ticker):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey=75NGNLOY2P6P3HT4'
    response = requests.get(url)
    info = response.json()
    print(info['Symbol'])
    print(info['Name'])
    print(info['Description'])

get_market_stock_info('AAPL')
