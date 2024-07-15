import os

from tinkoff.invest import Client

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        print(client.market_data.get_last_prices(figi=["BBG004730ZJ9"]))


if __name__ == "__main__":
    main()
