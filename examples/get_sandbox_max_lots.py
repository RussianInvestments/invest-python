import os

from tinkoff.invest import GetMaxLotsRequest
from tinkoff.invest.sandbox.client import SandboxClient

TOKEN = os.environ["INVEST_SANDBOX_TOKEN"]


def main():
    with SandboxClient(TOKEN) as client:
        account_id = client.users.get_accounts().accounts[0].id
        request = GetMaxLotsRequest(
            account_id=account_id,
            instrument_id="BBG004730N88",
        )
        print(client.sandbox.get_sandbox_max_lots(request=request))


if __name__ == "__main__":
    main()
