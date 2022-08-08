import all_tasks
import time


def main():
    aggregator = all_tasks.AggTrades()
    # all available Binance USDT symbols must be supplied below (a few for testing from the global list in all_tasks.py)
    aggregator.symbols = list(filter(lambda x: 'USDT' in x, all_tasks.symbols_global))
    selected_list = aggregator.create_q2_top_list()

    symbols = selected_list.keys()

    spread = all_tasks.PriceSpread()
    spread.symbols = symbols

    while True:
        delta_spread_dict = {}
        price_spread_dict = dict(spread.create_price_spread())
        # previous price spread is stored in the instance of the class
        if spread.price_spread_list_old is not None:
            price_spread_dict_old = dict(spread.price_spread_list_old)
        else:
            price_spread_dict_old = {}

        for symbol in symbols:
            delta_list = []
            # old value is available in the instance state
            if symbol in price_spread_dict_old.keys():
                old_value = price_spread_dict_old[symbol]
            else:
                old_value = 0
            # delta calculation
            delta = price_spread_dict[symbol] - old_value
            delta_list.append(price_spread_dict[symbol])
            delta_list.append(delta)
            delta_spread_dict[symbol] = delta_list

        print(delta_spread_dict)
        # sleep 10s
        time.sleep(10)


if __name__ == "__main__":
    main()
