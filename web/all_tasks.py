from binance.spot import Spot
import time


def get_volume(tuple_key):
    return tuple_key[1]


class AggTrades:

    def __init__(self):
        self.symbols = None
        self.q2_top5_dict = None
        self.q1_top5_dict = None

    def get_for_symbol_for_hour(self, symbol, start_time, end_time):
        client = Spot()

        trades = (client.agg_trades(symbol, startTime=start_time, endTime=end_time))
        return trades

    def get_for_symbol(self, symbol):
        initial_time = round((time.time() * 1000))
        total_trades = []

        for hour in range(2):
            end_time = initial_time - hour*60*60*1000
            start_time = end_time - 60*60*1000
            trades = self.get_for_symbol_for_hour(symbol, start_time, end_time)
            total_trades += trades
            print('*')
        return total_trades

    def sum_trades(self, trades):
        total = 0
        for trade in trades:
            total = total + float(trade['q'])
        return total

    def get_sum_for_symbol(self, symbol):
        trades = self.get_for_symbol(symbol)
        return symbol, self.sum_trades(trades)

    def get_len_for_symbol(self, symbol):
        trades = self.get_for_symbol(symbol)
        return symbol, len(trades)

    def create_q1_top_list(self):
        symbols = self.symbols

        top_list = []

        for symbol in symbols:
            volume = self.get_sum_for_symbol(symbol)
            top_list.append(volume)

        top_list.sort(reverse=True, key=get_volume)
        selected_list = dict(top_list[0:5])

        self.q1_top5_dict = selected_list

        return selected_list

    def create_q2_top_list(self):
        symbols = self.symbols

        top_list = []

        for symbol in symbols:
            volume = self.get_len_for_symbol(symbol)
            top_list.append(volume)

        top_list.sort(reverse=True, key=get_volume)
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
        trades = (client.trades(symbol))
        return trades

    def get_price_spread(self, trades):
        max_price = max(trades, key=lambda x: x['price'])
        min_price = min(trades, key=lambda x: x['price'])
        price_spread = float(max_price['price']) - float(min_price['price'])
        return price_spread

    def get_price_for_symbol(self, symbol):
        trades = self.get_for_symbol(symbol)
        return symbol, self.get_price_spread(trades)

    def create_price_spread(self):
        symbols = self.symbols
        price_spread_list = []

        for symbol in symbols:
            price_spread = self.get_price_for_symbol(symbol)
            price_spread_list.append(price_spread)
        self.price_spread_list_old = self.price_spread_list
        self.price_spread_list = price_spread_list
        return price_spread_list


def main():
    aggregator = AggTrades()
    aggregator.symbols = ['BTCAUD', 'BTCBIDR', 'BTCBRL', 'BTCBUSD', 'BTCEUR', 'BTCGBP', 'BTCRUB', 'BTCTRY',
                          'BTCTUSD', 'BTCUAH', 'BTCUSDC', 'BTCUSDP', 'BTCUSDT']
    selected_list = aggregator.create_q1_top_list()
    print(selected_list)


if __name__ == "__main__":
    main()
