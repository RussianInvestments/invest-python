"""Example - How to get order price."""

import logging
import os
from decimal import Decimal

from tinkoff.invest import Client, GetOrderPriceRequest, OrderDirection
from tinkoff.invest.utils import decimal_to_quotation

TOKEN = os.environ["INVEST_TOKEN"]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


INSTRUMENT_ID = "TCS00A105GE2"
QUANTITY = 1
PRICE = 230.1


def main():
    logger.info("Getting Max Lots")
    with Client(TOKEN) as client:
        response = client.users.get_accounts()
        account, *_ = response.accounts
        account_id = account.id

        logger.info(
            "Get pre-trade order commission and price for instrument=%s, quantity=%s and price=%s",
            INSTRUMENT_ID,
            QUANTITY,
            PRICE,
        )
        get_order_price = client.orders.get_order_price(
            GetOrderPriceRequest(
                account_id=account_id,
                instrument_id=INSTRUMENT_ID,
                quantity=QUANTITY,
                direction=OrderDirection.ORDER_DIRECTION_BUY,
                price=decimal_to_quotation(Decimal(PRICE)),
            )
        )

    print(get_order_price)


if __name__ == "__main__":
    main()
