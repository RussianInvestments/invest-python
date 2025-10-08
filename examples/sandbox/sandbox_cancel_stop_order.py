import os

from tinkoff.invest.sandbox.client import SandboxClient
from tinkoff.invest.schemas import (
    CancelStopOrderRequest,
    CancelStopOrderResponse,
    GetStopOrdersRequest,
    StopOrderStatusOption,
)


def main():
    token = os.environ["INVEST_TOKEN"]

    with SandboxClient(token) as client:
        accounts = client.users.get_accounts()
        account_id = accounts.accounts[0].id
        stop_orders = client.sandbox.get_sandbox_stop_orders(
            request=GetStopOrdersRequest(
                account_id=account_id,
                status=StopOrderStatusOption.STOP_ORDER_STATUS_ACTIVE,
            )
        )
        stop_order_id = stop_orders.stop_orders[0].stop_order_id
        response = cancel_stop_order(client, account_id, stop_order_id)
        print(f"Отменена отложенная заявка id={stop_order_id}: {response}")


def cancel_stop_order(
    sandbox_service, account_id, stop_order_id
) -> CancelStopOrderResponse:
    return sandbox_service.sandbox.cancel_sandbox_stop_order(
        request=CancelStopOrderRequest(
            account_id=account_id,
            stop_order_id=stop_order_id,
        )
    )


if __name__ == "__main__":
    main()
