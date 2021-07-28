from flask import Flask, jsonify
from flask_cors import CORS
from extract_params import *
from helper_functions import *
import yfinance as yf
import matplotlib.pyplot as plt
import setting

plt.figure()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)


@app.route('/info', methods=['GET', 'POST'])
def info():
    try:
        stock_symbol = get_string_param('stock_symbol')
        ticker = yf.Ticker(stock_symbol)
        return jsonify(ticker.info)
    except Exception as e:
        return jsonify(str(e))


@app.route('/history', methods=['GET', 'POST'])
def history():
    try:
        stock_symbol = get_string_param('stock_symbol')
        ticker_history = yf.download(stock_symbol, progress=False)
        ticker_history_dict = ticker_history.to_dict('index')
        ticker_history_dict = {K.strftime('%Y-%m-%d'): V for K, V in ticker_history_dict.items()}
        return jsonify(ticker_history_dict)
    except Exception as e:
        return jsonify(str(e))


@app.route('/history_interval', methods=['GET', 'POST'])
def history_interval():
    try:
        stock_symbol = get_string_param('stock_symbol')
        start = validate_date(get_string_param('start'), 'start')
        end = validate_date(get_string_param('end'), 'end')
        ticker_history = yf.download(stock_symbol, start=start, end=end, progress=False)
        ticker_history_dict = ticker_history.to_dict('index')
        ticker_history_dict = {K.strftime('%Y-%m-%d'): V for K, V in ticker_history_dict.items()}
        return jsonify(ticker_history_dict)
    except Exception as e:
        return jsonify(str(e))


@app.route('/chart', methods=['GET', 'POST'])
def chart():
    try:
        plt.clf()
        clean_static()
        stock_symbol = get_string_param('stock_symbol')
        type = validate_chart_type(get_string_param('type'))
        ticker = yf.Ticker(stock_symbol)
        df = ticker.history(period='max')
        df[type].plot(title=f'{stock_symbol} stock price')
        chart_relative_link = setting.static + '/chart.png'
        plt.savefig(chart_relative_link)
        return jsonify(request.host + '/' + chart_relative_link)
    except Exception as e:
        return jsonify(str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
