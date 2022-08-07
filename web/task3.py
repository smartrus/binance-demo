from binance.spot import Spot
import all_tasks


def get_for_symbol(symbol):
    client = Spot()

    orders = (client.depth(symbol, limit=200))
    return orders


def sum_orders(orders):
    total_orders = []
    total_amount = 0

    orders.pop('lastUpdateId')

    for order_book in orders:
        for book in orders[order_book]:
            total_amount = total_amount + float(book[0])*float(book[1])
        total_orders.append(total_amount)
        total_amount = 0
    return total_orders


def get_sum_for_symbol(symbol):
    orders = get_for_symbol(symbol)
    return symbol, sum_orders(orders)


def main():
    aggregator = all_tasks.AggTrades()
    aggregator.symbols = ['BTCAUD', 'BTCBIDR', 'BTCBRL', 'BTCBUSD', 'BTCEUR', 'BTCGBP', 'BTCRUB', 'BTCTRY',
                          'BTCTUSD', 'BTCUAH', 'BTCUSDC', 'BTCUSDP', 'BTCUSDT']
    selected_list = aggregator.create_q1_top_list()

    symbols = selected_list.keys()

    orders_list = []

    for symbol in symbols:
        notional_value = get_sum_for_symbol(symbol)
        orders_list.append(notional_value)

    print(dict(orders_list))


if __name__ == "__main__":
    main()
