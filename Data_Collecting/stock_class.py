class StockData:

    def __init__(self, info: {}):
        self.info = info

    def get_home_page_info(self):
        return [self.info["Symbol"], self.info["Name"],
                self.info["Float Shorted"], self.info["Short Interest"]]

    def get_all(self):
        return self.info

    def get_ticker(self):
        return self.info["Symbol"]
