import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import IndicativesRequest

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        request = IndicativesRequest()
        indicatives = client.instruments.indicatives(request=request)
        for instrument in indicatives.instruments:
            print(instrument.name)


if __name__ == "__main__":
    main()
