import all_tasks


def main():
    aggregator = all_tasks.AggTrades()
    # all available Binance BTC symbols must be supplied below (a few for testing)
    aggregator.symbols = ['BTCAUD', 'BTCBIDR', 'BTCBRL', 'BTCBUSD', 'BTCEUR', 'BTCGBP', 'BTCRUB', 'BTCTRY',
                          'BTCTUSD', 'BTCUAH', 'BTCUSDC', 'BTCUSDP', 'BTCUSDT']
    selected_list = aggregator.create_q1_top_list()
    print(selected_list)


if __name__ == "__main__":
    main()
