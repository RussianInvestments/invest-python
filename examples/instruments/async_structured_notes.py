import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import InstrumentsRequest, InstrumentStatus


async def main():
    token = os.environ["INVEST_TOKEN"]

    with AsyncClient(token) as client:
        r = await client.instruments.structured_notes(
            request=InstrumentsRequest(
                instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL
            )
        )
        for note in r.instruments:
            print(note)


if __name__ == "__main__":
    asyncio.run(main())
