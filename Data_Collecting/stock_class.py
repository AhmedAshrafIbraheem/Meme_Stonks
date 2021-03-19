
def compare_stocks(stock1, stock2) -> int:
    # returns 0, 1 or -1
    return 0


class StockData:

    def __init__(self, info: {}):
        self.info = info

    def get_home_page_info(self):
        return [self.info["Symbol"], self.info["Name"], self.info["Price"],
                self.info["Short Interest"], self.info["Float Shorted"]]

    def get_all(self):
        return self.info

    def get_ticker(self):
        return self.info["Symbol"]
