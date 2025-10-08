import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import InstrumentIdType, InstrumentRequest


async def main():
    token = os.environ["INVEST_TOKEN"]

    with AsyncClient(token) as client:
        r = await client.instruments.structured_note_by(
            request=InstrumentRequest(
                id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id="BBG012S2DCJ8"
            )
        )
        print(r.instrument)


if __name__ == "__main__":
    asyncio.run(main())
