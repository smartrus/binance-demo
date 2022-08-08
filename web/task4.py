import all_tasks


def main():
    aggregator = all_tasks.AggTrades()
    # all available Binance USDT symbols must be supplied below (a few for testing)
    aggregator.symbols = ['BTCUSDT', 'WINUSDT', 'ETHUSDT', 'BTTUSDT', 'HOTUSDT', 'BNBUSDT', 'FILUSDT', 'DOTUSDT',
                          'XRPUSDT', 'TRXUSDT', 'BUSDUSDT', 'EOSUSDT', 'DENTUSDT']
    selected_list = aggregator.create_q2_top_list()

    symbols = selected_list.keys()

    spread = all_tasks.PriceSpread()
    spread.symbols = symbols
    price_spread_list = spread.create_price_spread()

    print(dict(price_spread_list))


if __name__ == "__main__":
    main()
