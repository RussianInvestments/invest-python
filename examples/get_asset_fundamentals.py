import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import GetAssetFundamentalsRequest

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        request = GetAssetFundamentalsRequest(
            assets=["TCS00A105GE2"],
        )
        print(client.instruments.get_asset_fundamentals(request=request))


if __name__ == "__main__":
    main()
