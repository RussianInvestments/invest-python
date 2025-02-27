"""Example - How to get Post Order"""

import os
from uuid import uuid4

from tinkoff.invest import Client, OrderDirection, OrderType
from tinkoff.invest.schemas import PostOrderAsyncRequest

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts()
        account_id = accounts.accounts[0].id

        request = PostOrderAsyncRequest(
            order_type=OrderType.ORDER_TYPE_MARKET,
            direction=OrderDirection.ORDER_DIRECTION_BUY,
            instrument_id="BBG004730ZJ9",
            quantity=1,
            account_id=account_id,
            order_id=str(uuid4()),
        )
        response = client.orders.post_order_async(request=request)
        print(response)


if __name__ == "__main__":
    main()
