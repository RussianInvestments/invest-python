import os

from tinkoff.invest import Client

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        response = client.users.get_accounts()
        accounts = [account.id for account in response.accounts]
        for response in client.operations_stream.positions_stream(
            accounts=accounts, with_initial_positions=True
        ):  # noqa:E501 # pylint:disable=line-too-long
            print(response)


if __name__ == "__main__":
    main()
