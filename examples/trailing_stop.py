"""Example - Trailing Stop Take Profit order.
spread=0.5 relative value
indent=0.5 absolute value
"""

import json
import logging
import os
from decimal import Decimal

from tinkoff.invest import (
    Client,
    ExchangeOrderType,
    GetStopOrdersRequest,
    PostStopOrderRequest,
    PostStopOrderRequestTrailingData,
    StopOrderDirection,
    StopOrderExpirationType,
    StopOrderTrailingData,
    StopOrderType,
    TakeProfitType,
)
from tinkoff.invest.schemas import TrailingValueType
from tinkoff.invest.utils import decimal_to_quotation

TOKEN = os.environ["INVEST_TOKEN"]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


INSTRUMENT_ID = "TCS00A105GE2"
QUANTITY = 1
PRICE = 230.500000000
STOPPRICE = 230
INDENT = 0.5
SPREAD = 0.5


def main():
    logger.info("Getting Max Lots")
    with Client(TOKEN) as client:
        response = client.users.get_accounts()
        account, *_ = response.accounts
        account_id = account.id

        logger.info(
            "Post take profit stop order for instrument=%s and trailing parameters: indent=%s, spread=%s, price=%s ",
            INSTRUMENT_ID,
            INDENT,
            SPREAD,
            STOPPRICE,
        )

        post_stop_order = client.stop_orders.post_stop_order(
            quantity=QUANTITY,
            price=decimal_to_quotation(Decimal(PRICE)),
            stop_price=decimal_to_quotation(Decimal(STOPPRICE)),
            direction=StopOrderDirection.STOP_ORDER_DIRECTION_SELL,
            account_id=account_id,
            stop_order_type=StopOrderType.STOP_ORDER_TYPE_TAKE_PROFIT,
            instrument_id=INSTRUMENT_ID,
            expiration_type=StopOrderExpirationType.STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL,
            exchange_order_type=ExchangeOrderType.EXCHANGE_ORDER_TYPE_LIMIT,
            take_profit_type=TakeProfitType.TAKE_PROFIT_TYPE_TRAILING,
            trailing_data=StopOrderTrailingData(
                indent=decimal_to_quotation(Decimal(INDENT)),
                indent_type=TrailingValueType.TRAILING_VALUE_ABSOLUTE,
                spread=decimal_to_quotation(Decimal(SPREAD)),
                spread_type=TrailingValueType.TRAILING_VALUE_RELATIVE,
            ),
        )

    print(post_stop_order)


if __name__ == "__main__":
    main()
