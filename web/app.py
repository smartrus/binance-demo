from flask import Flask, render_template
from . import all_tasks


app = Flask(__name__)
# a global variable to save the state for calculating the delta
price_spread_dict_old_global = {}


def price_spread():
    # it can be retrieved from the task2 output as it is done in task5,
    # but for the sake of performance supplied as a static list
    symbols = ['BTCUSDT', 'ETHUSDT', 'BUSDUSDT', 'BNBUSDT', 'HOTUSDT', 'XRPUSDT']

    spread = all_tasks.PriceSpread()
    spread.symbols = symbols

    while True:
        # used the global variable with the state to calculate the delta
        global price_spread_dict_old_global
        delta_spread_dict = {}
        # getting the spread from the latest market data
        price_spread_dict = dict(spread.create_price_spread())
        # check if old data is available
        if price_spread_dict_old_global is not None:
            # if old data is available calculate the delta
            price_spread_dict_old = price_spread_dict_old_global
            # store the latest data in the global variable for the next delta calculation
            price_spread_dict_old_global = price_spread_dict
        else:
            price_spread_dict_old = {}

        for symbol in symbols:
            delta_list = []
            if symbol in price_spread_dict_old.keys():
                old_value = price_spread_dict_old[symbol]
            else:
                old_value = 0
            # delta calculation
            delta = price_spread_dict[symbol] - old_value
            # list generation
            delta_list.append(price_spread_dict[symbol])
            delta_list.append(delta)
            delta_spread_dict[symbol] = delta_list

        return delta_spread_dict


@app.route('/metrics')
def metrics():
    metrics = ""
    # Prometheus format for metrics
    for key, val in price_spread().items():
        metrics += 'price_spread{symbol="%s"}\t%s\t%s\n'\
                   % (key, val[0], val[1])
    return metrics


@app.route("/")
def index():
    return render_template('main.html')
