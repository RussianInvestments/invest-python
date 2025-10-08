import asyncio
import os

from _decimal import Decimal

from tinkoff.invest import AccountType, AsyncClient
from tinkoff.invest.schemas import CurrencyTransferRequest
from tinkoff.invest.utils import decimal_to_money


async def main():
    token = os.environ["INVEST_TOKEN"]

    async with AsyncClient(token) as client:
        accounts = [
            i
            for i in (await client.users.get_accounts()).accounts
            if i.type == AccountType.ACCOUNT_TYPE_TINKOFF
        ]

        if len(accounts) < 2:
            print("Недостаточно счетов для демонстрации")
            return

        from_account_id = accounts[0].id
        to_account_id = accounts[1].id

        await client.users.currency_transfer(
            CurrencyTransferRequest(
                from_account_id=from_account_id,
                to_account_id=to_account_id,
                amount=decimal_to_money(Decimal(1), "rub"),
            )
        )
        print("Перевод выполнен")


if __name__ == "__main__":
    asyncio.run(main())
