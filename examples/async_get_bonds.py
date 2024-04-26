import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import InstrumentExchangeType

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        bonds = await client.instruments.bonds(
            instrument_exchange=InstrumentExchangeType.INSTRUMENT_EXCHANGE_UNSPECIFIED,
        )
        for bond in bonds.instruments:
            print(bond)


if __name__ == "__main__":
    asyncio.run(main())
