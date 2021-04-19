from flask import Flask, render_template, url_for, flash, redirect, request
from gevent.pywsgi import WSGIServer
from models import get_analysis, get_ticker_data, get_chart_analysis, search_ticker
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# TODO: Mohamed, Implement error pages with skeleton. Found in templates/errors


@app.errorhandler(403)
def forbidden(error):
    return render_template("errors/403.html", title="Forbidden"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html", title="Page Not Found"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("errors/500.html", title="Server Error"), 500


@app.route('/', methods=['GET'])
def index():
    data = get_analysis()
    chart = get_chart_analysis()
    return render_template('front_page.html', data=data, legend=chart['legend'], the_date=chart['the_date'],
                           tickers=chart['tickers'], nested_dictionaries=chart['nested_dictionaries'])


@app.route('/stock/<string:ticker>', methods=['GET'])
def stock_data(ticker: str):
    if not _ticker_validation(ticker):
        flash("Wrong Ticker Format")
        return redirect(url_for("index"))

    ticker = ticker.upper()
    data = get_ticker_data(ticker)
    
    if not data:
        flash("Wrong Ticker Format")
        return redirect(url_for("index"))

    return render_template('secondpage.html', data=data)


@app.route('/search', methods=['POST'])
def search_stock():
    ticker = request.form['search']

    if not _ticker_validation(ticker):
        flash("Wrong Ticker Format")
        return redirect(url_for("index"))

    ticker = ticker.upper()
    data = search_ticker(ticker)

    if not data:
        flash("Wrong Ticker Format")
        return redirect(url_for("index"))

    return render_template('secondpage.html', data=data)


def _ticker_validation(ticker: str) -> bool:
    if len(ticker) < 3 or len(ticker) > 5:
        return False
    return ticker.isalpha()


if __name__ == '__main__':
    app.run(debug=True)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
