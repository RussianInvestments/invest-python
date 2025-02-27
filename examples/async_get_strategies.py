"""Example - How to get all strategies"""
import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import GetStrategiesRequest

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        r = await client.signals.get_strategies(request=GetStrategiesRequest())
        for strategy in r.strategies:
            print(strategy)


if __name__ == "__main__":
    asyncio.run(main())
