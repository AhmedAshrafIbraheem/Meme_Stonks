from stock_class import StockData
from store_guy import DatabaseInteraction


def writer():
    data = [{"Symbol": "GME", "Company Name": "Game Stop Corp.", "Price": 192.25, "Short Interest": 2309662, "Float Shorted": 54.44},
            {"Symbol": "NOK", "Company Name": "Nokia Corp.", "Price": 3.86, "Short Interest": 623316, "Float Shorted": 52.73},
            {"Symbol": "SENS", "Company Name": "Senseonics Holdings Inc.", "Price": 2.47, "Short Interest": 59476737, "Float Shorted": 44.24},
            {"Symbol": "AMC", "Company Name": "AMC Networks", "Price": 9.03, "Short Interest": 12791353, "Float Shorted": 40.31},
            {"Symbol": "BBBY", "Company Name": "Bed Bath & Beyond Inc.", "Price": 31.20, "Short Interest": 16199074, "Float Shorted": 40.04},
            {"Symbol": "LAZR", "Company Name": "Luminar Technologies Inc.", "Price": 6.95, "Short Interest": 5417119, "Float Shorted": 39.74},
            {"Symbol": "NNDM", "Company Name": "Nano Dimension Ltd.", "Price": 8.16, "Short Interest": 43091520, "Float Shorted": 39.73},
            {"Symbol": "RKT", "Company Name": "Rocket Cos. Inc.", "Price": 24.61, "Short Interest": 887394, "Float Shorted": 39.29},
            {"Symbol": "TRIT", "Company Name": "Triterras Inc.", "Price": 6.78, "Short Interest": 26946139, "Float Shorted": 38.04},
            {"Symbol": "ESPR", "Company Name": "Esperion Therapeutics", "Price": 15.03, "Short Interest": 19241124, "Float Shorted": 35.43}]

    ordered_list = []
    for d in data:
        ordered_list.append(StockData(d))

    DatabaseInteraction.get_instance().store_top10s(ordered_list)


def reader():
    ret = DatabaseInteraction.get_instance().read_top10s()
    if not ret:
        print(ret)
        return

    for x in ret:
        print(x)


def testing():
    while True:
        x = input()
        if x.__eq__("exit"):
            break
        elif x.__eq__("delete1"):
            DatabaseInteraction.get_instance().delete_top10s()
        elif x.__eq__("delete2"):
            DatabaseInteraction.get_instance().delete_stocks()
        elif x.__eq__("readall"):
            DatabaseInteraction.get_instance().read_all()
        elif x.__eq__("write"):
            writer()
        else:
            print("Wrong Input")


if __name__ == '__main__':
    testing()
