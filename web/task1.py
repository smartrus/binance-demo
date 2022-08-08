import all_tasks


def main():
    aggregator = all_tasks.AggTrades()
    # all available Binance BTC symbols must be supplied below (a few for testing from the global list in all_tasks.py)
    aggregator.symbols = list(filter(lambda x: 'BTC' in x, all_tasks.symbols_global))
    selected_list = aggregator.create_q1_top_list()
    print(selected_list)


if __name__ == "__main__":
    main()
