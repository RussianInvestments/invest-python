import asyncio
import os

from tinkoff.invest import AsyncClient, InstrumentType
from tinkoff.invest.schemas import EventType, GetBondEventsRequest

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        bond = (
            await client.instruments.find_instrument(
                query="Тинькофф Банк выпуск 1",
                instrument_kind=InstrumentType.INSTRUMENT_TYPE_BOND,
            )
        ).instruments[0]

        request = GetBondEventsRequest(
            instrument_id=bond.uid,
            type=EventType.EVENT_TYPE_CALL,
        )
        print(await client.instruments.get_bond_events(request=request))


if __name__ == "__main__":
    asyncio.run(main())
