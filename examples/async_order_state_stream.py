import asyncio
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import OrderStateStreamRequest

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        request = OrderStateStreamRequest()
        stream = client.orders_stream.order_state_stream(request=request)
        async for order_state in stream:
            print(order_state)


if __name__ == "__main__":
    asyncio.run(main())
