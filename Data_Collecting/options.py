from requests import get


def options():
    url = 'https://www.barchart.com/options/unusual-activity/stocks'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    data = get(url, headers=headers)
    print(data.content.decode())

options()