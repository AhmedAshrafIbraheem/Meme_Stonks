from pymongo import MongoClient
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
        self.my_client.server_info()

    def store_top10s(self, tickers_list: []):
        to_store = []
        for ticker in tickers_list:
            to_store.append(ticker.get_home_page_info())
        self.top10s.insert_one({"Top10": to_store})
        print("Top10 Write is Done")

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

        print("All Stocks")
        for x in self.stocks.find():
            print(x)

    def store_stock(self, stock_data: {}):
        pass

