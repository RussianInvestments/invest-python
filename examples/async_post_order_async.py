import asyncio
import os
from uuid import uuid4

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import OrderDirection, OrderType, PostOrderAsyncRequest

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        accounts = await client.users.get_accounts()
        account_id = accounts.accounts[0].id
        request = PostOrderAsyncRequest(
            order_type=OrderType.ORDER_TYPE_MARKET,
            direction=OrderDirection.ORDER_DIRECTION_BUY,
            instrument_id="BBG004730ZJ9",
            quantity=1,
            account_id=account_id,
            order_id=str(uuid4()),
        )
        response = await client.orders.post_order_async(request=request)
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
