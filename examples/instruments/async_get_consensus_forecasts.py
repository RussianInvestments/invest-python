import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import GetConsensusForecastsRequest, Page

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        request = GetConsensusForecastsRequest(
            paging=Page(page_number=0, limit=2),
        )
        response = await client.instruments.get_consensus_forecasts(request=request)
        print(response.page)
        for forecast in response.items:
            print(forecast.uid, forecast.consensus.name)


if __name__ == "__main__":
    asyncio.run(main())
