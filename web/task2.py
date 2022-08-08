import all_tasks


def main():
    aggregator = all_tasks.AggTrades()
    # all available Binance USDT symbols must be supplied below (a few for testing)
    aggregator.symbols = ['BTCUSDT', 'WINUSDT', 'ETHUSDT', 'BTTUSDT', 'HOTUSDT', 'BNBUSDT', 'FILUSDT', 'DOTUSDT',
                          'XRPUSDT', 'TRXUSDT', 'BUSDUSDT', 'EOSUSDT', 'DENTUSDT']
    selected_list = aggregator.create_q2_top_list()
    print(selected_list)


if __name__ == "__main__":
    main()
