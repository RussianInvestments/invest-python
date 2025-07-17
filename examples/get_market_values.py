import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import GetMarketValuesRequest, MarketValueType

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        for values in client.market_data.get_market_values(
            request=GetMarketValuesRequest(
                instrument_id=["BBG004730N88"],
                values=[
                    MarketValueType.INSTRUMENT_VALUE_LAST_PRICE,
                    MarketValueType.INSTRUMENT_VALUE_CLOSE_PRICE,
                ],
            )
        ).instruments:
            for value in values.values:
                print(value)

    return 0


if __name__ == "__main__":
    main()
