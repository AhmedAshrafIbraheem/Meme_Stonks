from pymongo import MongoClient
from stock_class import StockData
# sudo systemctl start mongod


class DatabaseInteraction:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseInteraction._instance is None:
            DatabaseInteraction()
            print('Connection with PyMongo DB established !!')
        return DatabaseInteraction._instance

    def __init__(self):
        if DatabaseInteraction._instance is not None:
            raise Exception('This class is a singleton!')

        DatabaseInteraction._instance = self
        self.my_client = MongoClient('mongodb://localhost:27017/')
        self.my_db = self.my_client['SlamStonks']
        self.top10s = self.my_db['Top10s']
        self.stocks = self.my_db['Stocks']
        self.sentiment = self.my_db['Sentiment']
        self.options = self.my_db['Options']
        self.my_client.server_info()

    def store_options(self, info):
        self.options.insert_one({"Options": info})
        print("Options Write is Done")

    def store_top10s(self, tickers_list: []):
        to_store = []
        for ticker in tickers_list:
            to_store.append(ticker.get_home_page_info())
        self.top10s.insert_one({"Top10": to_store})
        print("Top10 Write is Done")

    def store_sentiment(self, tickers_trends):
        self.sentiment.insert_one({"Sentiment": tickers_trends})
        print("Sentiment Write is Done")

    def delete_sentiment(self):
        self.my_db.drop_collection('Sentiment')
        print('Sentiment Deleted')

    def delete_top10s(self):
        self.my_db.drop_collection('Top10s')
        print('Top10s Deleted')

    def delete_stocks(self):
        self.my_db.drop_collection('Stocks')
        print('Stocks Deleted')

    def read_all(self):
        print("All Top10s")
        for x in self.top10s.find():
            print(x)

        print('All Trends')
        for x in self.sentiment.find():
            print(x)

        print("All Stocks")
        for x in self.stocks.find():
            print(x)

    def store_stock(self, stock_data: StockData):
        self.stocks.find_one_and_delete({"_id": stock_data.get_ticker()})
        # self.stocks.insert_one({"_id": stock_data.get_ticker(),
        #                         "Data": self._remove_dots(stock_data.get_all())})
        self.stocks.insert_one({"_id": stock_data.get_ticker(),
                                "Data": stock_data.get_all()})
        print("{} is written".format(stock_data.get_ticker()))

    def _remove_dots(self, d: dict):
        new = {}
        for k, v in d.items():
            if isinstance(v, dict):
                v = self._remove_dots(v)
            new[k.replace('.', '-')] = v
        return new
