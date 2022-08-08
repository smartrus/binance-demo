from flask import Flask, render_template
from . import all_tasks


app = Flask(__name__)
price_spread_dict_old_global = {}


def price_spread():
    aggregator = all_tasks.AggTrades()
    aggregator.symbols = ['BTCUSDT', 'WINUSDT', 'ETHUSDT', 'BTTUSDT', 'HOTUSDT', 'BNBUSDT', 'FILUSDT', 'DOTUSDT',
                          'XRPUSDT', 'TRXUSDT', 'BUSDUSDT', 'EOSUSDT', 'DENTUSDT']
    selected_list = aggregator.create_q2_top_list()

    symbols = selected_list.keys()
    print(symbols)

    spread = all_tasks.PriceSpread()
    spread.symbols = symbols

    while True:
        global price_spread_dict_old_global
        delta_spread_dict = {}
        price_spread_dict = dict(spread.create_price_spread())
        if price_spread_dict_old_global is not None:
            price_spread_dict_old = price_spread_dict_old_global
            price_spread_dict_old_global = price_spread_dict
        else:
            price_spread_dict_old = {}

        for symbol in symbols:
            delta_list = []
            if symbol in price_spread_dict_old.keys():
                old_value = price_spread_dict_old[symbol]
            else:
                old_value = 0
            delta = price_spread_dict[symbol] - old_value
            delta_list.append(price_spread_dict[symbol])
            delta_list.append(delta)
            delta_spread_dict[symbol] = delta_list

        return delta_spread_dict


@app.route('/metrics')
def metrics():
    metrics = ""
    for key, val in price_spread().items():
        metrics += 'price_spread{symbol="%s"}\t%s\t%s\n'\
                   % (key, val[0], val[1])
    return metrics


@app.route("/")
def index():
    return render_template('main.html')
