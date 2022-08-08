from binance.spot import Spot
import time

# A list of all symbols available on Binance
# This list is intentionally left small for testing purpose
symbols_global = ['BTCAUD', 'BTCBIDR', 'BTCBRL', 'BTCBUSD', 'BTCEUR', 'BTCGBP', 'BTCRUB', 'BTCTRY', 'BTCTUSD',
                  'BTCUAH', 'BTCUSDC', 'BTCUSDP', 'BTCUSDT', 'WINUSDT', 'ETHUSDT', 'BTTUSDT', 'HOTUSDT', 'BNBUSDT',
                  'FILUSDT', 'DOTUSDT', 'XRPUSDT', 'TRXUSDT', 'BUSDUSDT', 'EOSUSDT', 'DENTUSDT']


def get_volume(tuple_key):
    return tuple_key[1]


# a class for aggregate trades API endpoint
class AggTrades:

    def __init__(self):
        # symbols
        self.symbols = None
        # question 1 top 5 list dictionary
        self.q1_top5_dict = None
        # question 2 top 5 list dictionary
        self.q2_top5_dict = None

    # since endpoint can return data for 1 hour max we have to iterate 24 times
    def get_for_symbol_for_hour(self, symbol, start_time, end_time):
        client = Spot()

        # used Binance API Market/Aggregate Trades endpoint
        trades = (client.agg_trades(symbol, startTime=start_time, endTime=end_time))
        return trades

    # getting trades for the last hour
    def get_for_symbol(self, symbol):
        # initial request time needed as a starting point for 24 iterations
        initial_time = round((time.time() * 1000))
        total_trades = []

        # a loop to get data for 24 hours, since max is 1 hour
        for hour in range(23):
            # minus 1 hour multiplied by an iterator in ms
            end_time = initial_time - hour*60*60*1000
            # minus 1 hour in ms
            start_time = end_time - 60*60*1000
            # getting trades for an hour
            trades = self.get_for_symbol_for_hour(symbol, start_time, end_time)
            # summarizing trades to calculate the total for 24 hours
            total_trades += trades
            # printing a progress indicator
            print('*')
        return total_trades

    # calculating the volume by summarizing quantities for a single symbol
    def sum_trades(self, trades):
        total = 0
        for trade in trades:
            total = total + float(trade['q'])
        return total

    # retrieving sum by symbol and return a list of summarized trades by symbol
    def get_sum_for_symbol(self, symbol):
        trades = self.get_for_symbol(symbol)
        return symbol, self.sum_trades(trades)

    # counting the number of trades per symbol
    def get_len_for_symbol(self, symbol):
        trades = self.get_for_symbol(symbol)
        return symbol, len(trades)

    # generating a list of top 5 symbols for the question 1
    def create_q1_top_list(self):
        symbols = self.symbols

        top_list = []

        for symbol in symbols:
            volume = self.get_sum_for_symbol(symbol)
            top_list.append(volume)

        # sorting by volume
        top_list.sort(reverse=True, key=get_volume)
        # getting top 5 symbols from the list
        selected_list = dict(top_list[0:5])

        self.q1_top5_dict = selected_list

        return selected_list

    # generating a list of top 5 symbols for the question 1
    def create_q2_top_list(self):
        symbols = self.symbols

        top_list = []

        for symbol in symbols:
            # sorting by number of trades
            volume = self.get_len_for_symbol(symbol)
            top_list.append(volume)

        top_list.sort(reverse=True, key=get_volume)
        # getting top 5 symbols from the list
        selected_list = dict(top_list[0:5])

        self.q2_top5_dict = selected_list

        return selected_list


class PriceSpread:
    def __init__(self):
        self.price_spread_list = None
        self.price_spread_list_old = None
        self.symbols = None

    def get_for_symbol(self, symbol):
        client = Spot()
        # used Binance API Market/Recent trades endpoint
        trades = (client.trades(symbol))
        return trades

    def get_price_spread(self, trades):
        # getting max price
        max_price = max(trades, key=lambda x: x['price'])
        # getting min price
        min_price = min(trades, key=lambda x: x['price'])
        # calculating the price spread
        price_spread = float(max_price['price']) - float(min_price['price'])
        return price_spread

    def get_price_for_symbol(self, symbol):
        trades = self.get_for_symbol(symbol)
        return symbol, self.get_price_spread(trades)

    def create_price_spread(self):
        symbols = self.symbols
        price_spread_list = []

        for symbol in symbols:
            # calculating the spread by symbol
            price_spread = self.get_price_for_symbol(symbol)
            # appending sreads to the list
            price_spread_list.append(price_spread)
        self.price_spread_list_old = self.price_spread_list
        self.price_spread_list = price_spread_list
        return price_spread_list
