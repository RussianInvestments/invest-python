"""Example - How to Post order"""

import os
from uuid import uuid4

from tinkoff.invest import Client, OrderDirection, OrderType
from tinkoff.invest.sandbox.client import SandboxClient

TOKEN = os.environ["INVEST_TOKEN"]

"""
Примеры дешевых акций:
BBG001M2SC01 84.120000000р
BBG000K3STR7 134.900000000р
BBG00F9XX7H4 142.000000000р
"""


def main():
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts()
        account_id = accounts.accounts[0].id

        response = client.orders.post_order(
            order_type=OrderType.ORDER_TYPE_MARKET,
            direction=OrderDirection.ORDER_DIRECTION_BUY,
            instrument_id="BBG004730ZJ9",
            quantity=1,
            account_id=account_id,
            order_id=str(uuid4()),
        )
        print(response)


if __name__ == "__main__":
    main()
