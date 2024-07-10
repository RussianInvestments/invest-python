import asyncio
import os

from tinkoff.invest import AsyncClient

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        print(await client.market_data.get_last_prices(figi=["BBG004730ZJ9"]))


if __name__ == "__main__":
    asyncio.run(main())
