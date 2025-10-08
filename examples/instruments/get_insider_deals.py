"""Example - How to get list of insider deals.
   Request data in loop with batches of 10 records.
"""
import logging
import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import GetInsiderDealsRequest

TOKEN = os.environ["INVEST_TOKEN"]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    with Client(TOKEN) as client:
        deals = []

        next_cursor = None
        while True:
            response = client.instruments.get_insider_deals(
                request=GetInsiderDealsRequest(
                    instrument_id="BBG004730N88", limit=10, next_cursor=next_cursor
                )
            )
            deals.extend(response.insider_deals)
            next_cursor = response.next_cursor
            if not next_cursor:
                break
    print("Insider deals:")
    for deal in deals:
        print(deal)


if __name__ == "__main__":
    main()
