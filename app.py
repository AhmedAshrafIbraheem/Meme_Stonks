from flask import Flask, render_template

app = Flask(__name__)


nested_dictionaries = {'LAZR': {'2021-04-01': 7.12, '2021-03-31': 9.22, '2021-03-30': 20.37, '2021-03-29': 10.49, '2021-03-28': 1.41, '2021-03-27': 1.68, '2021-03-26': 6.4, '2021-03-25': 7.67}, 'KMPH': {'2021-04-01': 3.41, '2021-03-31': 4.05, '2021-03-30': 4.88, '2021-03-29': 5.27, '2021-03-28': 0.83, '2021-03-27': 1.75, '2021-03-26': 6.01, '2021-03-25': 5.73}, 'TMBR': {'2021-04-01': 1.47, '2021-03-31': 1.78, '2021-03-30': 3.06, '2021-03-29': 2.21, '2021-03-28': 0.31, '2021-03-27': 0.78, '2021-03-26': 2.69, '2021-03-25': 2.55}, 'EYES': {'2021-04-01': 50.27, '2021-03-31': 47.58, '2021-03-30': 45.37, '2021-03-29': 49.27, '2021-03-28': 29.05, '2021-03-27': 34.48, '2021-03-26': 48.84, '2021-03-25': 56.36}, 'FBRX': {'2021-04-01': 0.67, '2021-03-31': 0.52, '2021-03-30': 0.95, '2021-03-29': 0.98, '2021-03-28': 0.26, '2021-03-27': 1.38, '2021-03-26': 1.97, '2021-03-25': 1.44}, 'ROOT': {'2021-04-01': 77.3, '2021-03-31': 88.99, '2021-03-30': 88.64, '2021-03-29': 90.38, '2021-03-28': 56.89, '2021-03-27': 84.32, '2021-03-26': 105.01, '2021-03-25': 119.21}, 'OTRK': {'2021-04-01': 1.55, '2021-03-31': 1.78, '2021-03-30': 1.61, '2021-03-29': 1.58, '2021-03-28': 0.42, '2021-03-27': 0.7, '2021-03-26': 2.49, '2021-03-25': 3.44}, 'HJLI': {'2021-04-01': 2.24, '2021-03-31': 1.67, '2021-03-30': 1.91, '2021-03-29': 1.19, '2021-03-28': 0.44, '2021-03-27': 0.08, '2021-03-26': 1.4, '2021-03-25': 1.78}, 'PUBM': {'2021-04-01': 1.86, '2021-03-31': 2.11, '2021-03-30': 2.73, '2021-03-29': 1.89, '2021-03-28': 0.84, '2021-03-27': 1.0, '2021-03-26': 1.76, '2021-03-25': 2.91}, 'ASO': {'2021-04-01': 3.0, '2021-03-31': 3.46, '2021-03-30': 5.21, '2021-03-29': 2.17, '2021-03-28': 1.08, '2021-03-27': 1.25, '2021-03-26': 1.42, '2021-03-25': 2.0}}


@app.route('/')

def home():
    tickers = list(nested_dictionaries.keys())
    legend = 'Monthly Data'
    the_date = list(nested_dictionaries[tickers[0]].keys())
    the_date.reverse()
    values = list(nested_dictionaries[tickers[0]].values())
    values.reverse()
    return render_template('table.html',  legend=legend, the_date=the_date, tickers=tickers, nested_dictionaries=nested_dictionaries,


                           stock_1_ticker="GME", stock_1_name="Gamestop", stock_1_price="220.92",
                           stock_1_float_shorted="42.11", stock_1_short_iterest="10,020,340",

                           stock_2_ticker="NOK", stock_2_name="Nokia", stock_2_price="220.92",
                           stock_2_float_shorted="42.11", stock_2_short_iterest="10,020,340",

                           stock_3_ticker="BBBY", stock_3_name="Gamestop", stock_3_price="220.92",
                           stock_3_float_shorted="42.11", stock_3_short_iterest="10,020,340",

                           stock_4_ticker="SENS", stock_4_name="Gamestop", stock_4_price="220.92",
                           stock_4_float_shorted="42.11", stock_4_short_iterest="10,020,340",

                           stock_5_ticker="ROK", stock_5_name="Gamestop", stock_5_price="220.92",
                           stock_5_float_shorted="42.11", stock_5_short_iterest="10,020,340",

                           stock_6_ticker="SOS", stock_6_name="Gamestop", stock_6_price="220.92",
                           stock_6_float_shorted="42.11", stock_6_short_iterest="10,020,340",

                           stock_7_ticker="RIOT", stock_7_name="Gamestop", stock_7_price="220.92",
                           stock_7_float_shorted="42.11", stock_7_short_iterest="10,020,340",

                           stock_8_ticker="MARA", stock_8_name="Gamestop", stock_8_price="220.92",
                           stock_8_float_shorted="42.11", stock_8_short_iterest="10,020,340",

                           stock_9_ticker="AMC", stock_9_name="Gamestop", stock_9_price="220.92",
                           stock_9_float_shorted="42.11", stock_9_short_iterest="10,020,340",

                           stock_10_ticker="SPCE", stock_10_name="Gamestop", stock_10_price="220.92",
                           stock_10_float_shorted="42.11", stock_10_short_iterest="10,020,340",
                           )





@app.route('/stock/<string:stock_id>')
def stock(stock_id):
    return render_template('secondpage.html', twitter_analysis="***Here we will input twitter sentiment analysis",
                           ticker="XXX", ticker_name="Sample", price="", volume="", average_volume="",
                           market_captialization="", fiftytwo_week_high="", fiftytwo_week_low="")


if __name__ == '__main__':
    app.run()
