import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import TradeSourceType

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        print(
            client.market_data.get_last_trades(
                instrument_id="BBG004730ZJ9",
                trade_source=TradeSourceType.TRADE_SOURCE_EXCHANGE,
            )
        )


if __name__ == "__main__":
    main()
