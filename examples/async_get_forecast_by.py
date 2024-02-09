import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import GetForecastRequest

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        instrument = (
            await client.instruments.find_instrument(
                query="Сбер Банк - привилегированные акции"
            )
        ).instruments[0]
        request = GetForecastRequest(instrument_id=instrument.uid)
        response = await client.instruments.get_forecast_by(request=request)
        print(instrument.name, response.consensus.recommendation.name)


if __name__ == "__main__":
    asyncio.run(main())
