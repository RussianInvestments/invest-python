"""Example - How to get Strategies"""

import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import GetStrategiesRequest

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        r = client.signals.get_strategies(request=GetStrategiesRequest())
        for strategy in r.strategies:
            print(strategy)


if __name__ == "__main__":
    main()
