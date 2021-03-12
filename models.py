
# Fetch Data From Database

class Top10:

    def __init__(self, symbol: str, company_name: str, price: float, short_interest: int, float_shorted: float):
        self.symbol = symbol
        self.company_name = company_name
        self.price = price
        self.short_interest = short_interest
        self.float_shorted = float_shorted


def get_analysis():
    tmp_data = [
        Top10("GME", "Game Stop Corp.", 192.25, 2309662, 54.44),
        Top10("NOK", "Nokia Corp.", 3.86, 623316, 52.73),
        Top10("SENS", "Senseonics Holdings Inc.", 2.47, 59476737, 44.24),
        Top10("AMC", "AMC Networks", 9.03, 12791353, 40.31),
        Top10("BBBY", "Bed Bath & Beyond Inc.", 31.20, 16199074, 40.04),
        Top10("LAZR", "Luminar Technologies Inc.", 6.95, 5417119, 39.74),
        Top10("NNDM", "Nano Dimension Ltd.", 8.16, 43091520, 39.73),
        Top10("RKT", "Rocket Cos. Inc.", 24.61, 887394, 39.29),
        Top10("TRIT", "Triterras Inc.", 6.78, 26946139, 38.04),
        Top10("ESPR", "Esperion Therapeutics", 4.03, 19241124, 35.43)
    ]
    return tmp_data


def get_ticker_data(ticker):
    cur_top10 = ["GME", "NOK", "SENS", "AMC", "BBBY", "LAZR", "NNDM", "RKT", "TRIT", "ESPR"]
    if ticker in cur_top10:
        return "{} is a really Good Stock to buy".format(ticker)
    return "Ticker is not in our DataBase"
