import os

from tinkoff.invest.sandbox.client import SandboxClient
from tinkoff.invest.schemas import (
    GetStopOrdersRequest,
    GetStopOrdersResponse,
    StopOrderStatusOption,
)


def main():
    token = os.environ["INVEST_TOKEN"]

    with SandboxClient(token) as client:
        accounts = client.users.get_accounts()
        account_id = accounts.accounts[0].id
        response = get_stop_orders(
            client, account_id, StopOrderStatusOption.STOP_ORDER_STATUS_ACTIVE
        )
        if len(response.stop_orders) > 0:
            print(response.stop_orders)
        else:
            print("Активных отложенных заявок не найдено")


def get_stop_orders(sandbox_service, account_id, status) -> GetStopOrdersResponse:
    return sandbox_service.sandbox.get_sandbox_stop_orders(
        request=GetStopOrdersRequest(
            account_id=account_id,
            status=status,
        )
    )


if __name__ == "__main__":
    main()
