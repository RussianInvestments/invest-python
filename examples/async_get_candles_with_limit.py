import asyncio
import os

from tinkoff.invest import AsyncClient, CandleInterval
from tinkoff.invest.utils import now

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        candles = await client.market_data.get_candles(
            instrument_id="BBG004730N88",
            to=now(),
            limit=3,
            interval=CandleInterval.CANDLE_INTERVAL_HOUR,
        )
        for candle in candles.candles:
            print(candle)

    return 0


if __name__ == "__main__":
    asyncio.run(main())
