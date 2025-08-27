"""Example - How to get list of orders for 1 last hour (maximum requesting period)."""
import asyncio
import datetime
import logging
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import OrderExecutionReportStatus

TOKEN = os.environ["INVEST_TOKEN"]

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def main():
    async with AsyncClient(TOKEN) as client:
        response = await client.users.get_accounts()
        account, *_ = response.accounts
        account_id = account.id

        now = datetime.datetime.now()
        orders = await client.orders.get_orders(
            account_id=account_id,
            from_=now - datetime.timedelta(hours=1),
            to=now,
            # filter only executed or partially executed orders
            execution_status=[
                OrderExecutionReportStatus.EXECUTION_REPORT_STATUS_FILL,
                OrderExecutionReportStatus.EXECUTION_REPORT_STATUS_PARTIALLYFILL,
            ],
        )
    print("Orders list:")
    for order in orders.orders:
        print(order)


if __name__ == "__main__":
    asyncio.run(main())
