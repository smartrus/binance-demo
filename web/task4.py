import all_tasks


def main():
    aggregator = all_tasks.AggTrades()
    # all available Binance USDT symbols must be supplied below (a few for testing from the global list in all_tasks.py)
    aggregator.symbols = list(filter(lambda x: 'USDT' in x, all_tasks.symbols_global))
    selected_list = aggregator.create_q2_top_list()

    symbols = selected_list.keys()

    spread = all_tasks.PriceSpread()
    spread.symbols = symbols
    price_spread_list = spread.create_price_spread()

    print(dict(price_spread_list))


if __name__ == "__main__":
    main()
