import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import AssetsRequest, InstrumentStatus, InstrumentType

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        r = await client.instruments.get_assets(
            request=AssetsRequest(
                instrument_type=InstrumentType.INSTRUMENT_TYPE_SHARE,
                instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE,
            )  # pylint:disable=line-too-long
        )
        print("BASE SHARE ASSETS")
        for bond in r.assets:
            print(bond)


if __name__ == "__main__":
    asyncio.run(main())
