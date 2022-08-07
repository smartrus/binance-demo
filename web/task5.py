import all_tasks
import time


def main():
    aggregator = all_tasks.AggTrades()
    aggregator.symbols = ['BTCUSDT', 'WINUSDT', 'ETHUSDT', 'BTTUSDT', 'HOTUSDT', 'BNBUSDT', 'FILUSDT', 'DOTUSDT',
                          'XRPUSDT', 'TRXUSDT', 'BUSDUSDT', 'EOSUSDT', 'DENTUSDT']
    selected_list = aggregator.create_q2_top_list()

    symbols = selected_list.keys()
    print(symbols)

    spread = all_tasks.PriceSpread()
    spread.symbols = symbols

    while True:
        delta_spread_dict = {}
        price_spread_dict = dict(spread.create_price_spread())
        if spread.price_spread_list_old is not None:
            price_spread_dict_old = dict(spread.price_spread_list_old)
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

        print(delta_spread_dict)
        time.sleep(10)


if __name__ == "__main__":
    main()
