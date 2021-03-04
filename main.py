from flask import Flask, render_template
from gevent.pywsgi import WSGIServer
from models import get_analysis
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


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
    return render_template('base.html', title="Welcome", data=data)


if __name__ == '__main__':
    app.run(debug=True)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
