import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import IndicativesRequest

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        request = IndicativesRequest()
        indicatives = await client.instruments.indicatives(request=request)
        for instrument in indicatives.instruments:
            print(instrument.name)


if __name__ == "__main__":
    asyncio.run(main())
