from pymongo import MongoClient, DESCENDING

# sudo systemctl start mongod
from Data_Collecting.market_stock_info import grab_stock_info
from Data_Collecting import social_stock_info

server_link = 'mongodb://localhost:27017/'
database_name = 'SlamStonks'


def get_analysis():
    my_client = MongoClient(server_link)
    my_db = my_client[database_name]
    col_top10s = my_db['Top10s']
    my_client.server_info()
    top10s = col_top10s.find_one(sort=[('_id', DESCENDING)])
    my_client.close()
    return top10s["Top10"] if top10s else None


def get_chart_analysis():
    my_client = MongoClient(server_link)
    my_db = my_client[database_name]
    col_sentiment = my_db['Sentiment']
    my_client.server_info()
    sentiment = col_sentiment.find_one(sort=[('_id', DESCENDING)])['Sentiment']
    my_client.close()

    twitter = sentiment['Twitter']
    google_trends = sentiment['GoogleTrends']
    tickers = list(google_trends.keys())
    legend = 'Monthly Data'
    the_date = list(google_trends[tickers[0]].keys())
    the_date.reverse()
    return {'legend': legend, 'the_date': the_date, 'tickers': tickers,
            'nested_dictionaries': google_trends, 'twitter': twitter}


def get_ticker_data(ticker):
    my_client = MongoClient(server_link)
    my_db = my_client[database_name]
    col_stocks = my_db['Stocks']
    my_client.server_info()
    stocks = col_stocks.find_one({"_id": ticker})
    my_client.close()
    return StockInfo(stocks["Data"]) if stocks else None


def search_ticker(ticker):
    data = grab_stock_info(ticker)
    social_info = social_stock_info.google_trends(ticker)
    data['social'] = social_info

    return StockInfo(data) if data['overview'] else None


class StockInfo:

    def __init__(self, info):
        self.symbol = info['Symbol']
        self.name = info['overview']['Name']
        self.market_cap = info['overview']['MarketCapitalization']
        self.fiftytwo_week_high = info['overview']['52WeekHigh']
        self.fiftytwo_week_low = info['overview']['52WeekLow']
        # self.daily = info['daily']

        if info['intraday']:
            intraday = info['intraday']
            self.Dates = []
            self.Values = []
            self.volumes = []

            for cur in intraday:
                self.Dates.append(cur['date'])
                self.Values.append(cur['last'])
                self.volumes.append(cur['volume'])

            self.Dates.reverse()
            self.Values.reverse()
            self.volumes.reverse()

            self.avg_vol = sum(self.volumes) // len(self.volumes)
            self.vol_Average = [self.avg_vol] * len(self.volumes)
            self.avg_price = sum(self.Values) / len(self.Values)
            self.avg_price = round(self.avg_price, 3)

        google_trends = info['google']
        self.google_dates = []
        self.google_values = []
        for key in google_trends:
            self.google_dates.append(key)
            self.google_values.append(google_trends[key])
        self.google_dates.reverse()
        self.google_values.reverse()

        google_week_avg = sum(self.google_values) / len(self.google_values)
        google_last_2_days_avg = (self.google_values[-1] + self.google_values[-2]) / 2

        twitter = info['twitter']
        self.key = list(twitter)[0]
        self.priority = round(twitter.get(self.key)[0], 2)
        self.subjectivity = round(twitter.get(self.key)[1], 2)

        self.counter = 0

        self.priority_rec = ''
        if self.priority > 0.74:
            self.priority_rec = 'EXTREMELY POSITIVELY'
            self.counter += 8
        elif 0.75 > self.priority > 0.49:
            self.priority_rec = 'VERY POSITIVELY'
            self.counter += 7
        elif 0.50 > self.priority > 0.24:
            self.priority_rec = 'POSITIVELY'
            self.counter += 6
        elif 0.25 > self.priority > 0:
            self.priority_rec = 'a LITTLE POSITIVELY'
            self.counter += 5
        elif 0 > self.priority > -0.25:
            self.priority_rec = 'a LITTLE NEGATIVELY'
            self.counter += 4
        elif -0.24 > self.priority > -0.50:
            self.priority_rec = 'NEGATIVELY'
            self.counter += 3
        elif -0.49 > self.priority > -0.75:
            self.priority_rec = 'VERY  NEGATIVELY'
            self.counter += 1
        else:
            self.priority_rec = 'EXTREMELY NEGATIVELY'

        self.subjectivity_rec = ''
        if self.subjectivity > 0.74:
            self.subjectivity_rec = 'IRRATIONAL and generally without any facts'
            self.counter += 2
        elif 0.75 > self.subjectivity > 0.49:
            self.subjectivity_rec = 'SOMEWHAT IRRATIONAL with little basis in fact'
        elif 0.50 > self.subjectivity > 0.24:
            self.subjectivity_rec = 'SOMEWHAT FACTUAL with little emotion'
        else:
            self.subjectivity_rec = 'RATIONAL and with no emotion'
            self.counter += 2

        if google_last_2_days_avg > (1.5 * google_week_avg):
            self.counter += 4
        elif google_week_avg > 60:
            self.counter += 1
        else:
            self.counter += 2

        self.recommendation = ''
        if self.counter > 12:
            self.recommendation = 'IT\'S A SLAMMER!!!'
        elif 13 > self.counter > 9:
            self.recommendation = 'WATCH CLOSELY...'
        elif 9 > self.counter > 5:
            self.recommendation = 'VERY UNLIKELY...'
        else:
            self.recommendation = 'DEAD END. MOVE ON.'


