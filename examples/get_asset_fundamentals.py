import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import GetAssetFundamentalsRequest

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        request = GetAssetFundamentalsRequest(
            assets=["40d89385-a03a-4659-bf4e-d3ecba011782"],
        )
        print(client.instruments.get_asset_fundamentals(request=request))


if __name__ == "__main__":
    main()
