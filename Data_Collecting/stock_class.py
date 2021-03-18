
def compare_stocks(stock1, stock2) -> int:
    # returns 0, 1 or -1
    return 0


class StockData:

    def __init__(self, info: {}):
        self.symbol = info["Symbol"]
        self.company_name = info["Company Name"]
        self.price = info["Price"]
        self.short_interest = info["Short Interest"]
        self.float_shorted = info["Float Shorted"]

    def get_home_page_info(self):
        return [self.symbol, self.company_name, self.price, self.short_interest, self.float_shorted]
