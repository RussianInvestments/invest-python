"""Example - How to get list of insider deals.
   Request data in loop with batches of 10 records.
"""
import asyncio
import logging
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import GetInsiderDealsRequest

TOKEN = os.environ["INVEST_TOKEN"]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def main():
    async with AsyncClient(TOKEN) as client:
        deals = []

        next_cursor = None
        while True:
            response = await client.instruments.get_insider_deals(
                request=GetInsiderDealsRequest(
                    instrument_id="BBG004730N88", limit=10, next_cursor=next_cursor
                )
            )
            deals.extend(response.insider_deals)
            if not next_cursor:
                break
            next_cursor = response.next_cursor
    print("Insider deals:")
    for deal in deals:
        print(deal)


if __name__ == "__main__":
    asyncio.run(main())
