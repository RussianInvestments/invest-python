"""Example - How to get available limits."""

import logging
import os

from tinkoff.invest import Client, GetMaxLotsRequest

TOKEN = os.environ["INVEST_TOKEN"]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


INSTRUMENT_ID = "TCS00A105GE2"


def main():
    logger.info("Getting Max Lots")
    with Client(TOKEN) as client:
        response = client.users.get_accounts()
        account, *_ = response.accounts
        account_id = account.id

        logger.info(
            "Calculating available order amount for instrument=%s and market price",
            INSTRUMENT_ID,
        )
        get_max_lots = client.orders.get_max_lots(
            GetMaxLotsRequest(account_id=account_id, instrument_id=INSTRUMENT_ID)
        )

    print(get_max_lots)


if __name__ == "__main__":
    main()
