import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import OrderStateStreamRequest

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        request = OrderStateStreamRequest()
        request.ping_delay_millis = 10000
        stream = client.orders_stream.order_state_stream(request=request)
        for order_state in stream:
            print(order_state)


if __name__ == "__main__":
    main()
