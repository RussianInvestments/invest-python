import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import GetMarketValuesRequest, MarketValueType

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        market_values = await client.market_data.get_market_values(
            request=GetMarketValuesRequest(
                instrument_id=["BBG004730N88", "64c0da45-4c90-41d4-b053-0c66c7a8ddcd"],
                values=[
                    MarketValueType.INSTRUMENT_VALUE_LAST_PRICE,
                    MarketValueType.INSTRUMENT_VALUE_CLOSE_PRICE,
                ],
            )
        )
        for instrument in market_values.instruments:
            print(instrument.instrument_uid)
            for value in instrument.values:
                print(value)


if __name__ == "__main__":
    asyncio.run(main())
