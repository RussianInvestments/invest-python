import os
import uuid

from _decimal import Decimal

from tinkoff.invest import (
    PostStopOrderRequest,
    PostStopOrderRequestTrailingData,
    PostStopOrderResponse,
    StopOrderExpirationType,
    StopOrderType,
)
from tinkoff.invest.sandbox.client import SandboxClient
from tinkoff.invest.schemas import Quotation, StopOrderDirection, TrailingValueType
from tinkoff.invest.utils import decimal_to_quotation


def main():
    token = os.environ["INVEST_TOKEN"]

    with SandboxClient(token) as client:
        accounts = client.users.get_accounts()
        account_id = accounts.accounts[0].id
        response = post_stop_order(
            client,
            account_id,
            "BBG004730ZJ9",
            stop_order_direction=StopOrderDirection.STOP_ORDER_DIRECTION_BUY,
            quantity=1,
            price=Quotation(units=10, nano=0),
        )
        print(response)


def post_stop_order(
    sandbox_service, account_id, instrument_id, stop_order_direction, quantity, price
) -> PostStopOrderResponse:
    return sandbox_service.sandbox.post_sandbox_stop_order(
        request=PostStopOrderRequest(
            account_id=account_id,
            instrument_id=instrument_id,
            direction=stop_order_direction,
            quantity=quantity,
            price=price,
            order_id=str(uuid.uuid4()),
            expiration_type=StopOrderExpirationType.STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL,
            stop_price=price,
            stop_order_type=StopOrderType.STOP_ORDER_TYPE_TAKE_PROFIT,
            trailing_data=PostStopOrderRequestTrailingData(
                indent_type=TrailingValueType.TRAILING_VALUE_RELATIVE,
                indent=decimal_to_quotation(Decimal(1)),
            ),
        )
    )


if __name__ == "__main__":
    main()
