import os

from tinkoff.invest import Client


def main():
    token = os.environ["INVEST_TOKEN"]

    with Client(token) as client:
        response = client.users.get_bank_accounts()
        print(response)


if __name__ == "__main__":
    main()
