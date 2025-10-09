import asyncio
import os

from tinkoff.invest import AsyncClient


async def main():
    token = os.environ["INVEST_TOKEN"]

    async with AsyncClient(token) as client:
        response = await client.users.get_bank_accounts()
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
