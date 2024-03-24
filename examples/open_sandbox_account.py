import os

from tinkoff.invest.sandbox.client import SandboxClient

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with SandboxClient(TOKEN) as client:
        print(client.sandbox.open_sandbox_account(name="tcs"))
        print(client.users.get_accounts())


if __name__ == "__main__":
    main()
