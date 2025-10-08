import os

from tinkoff.invest import Client

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        response = client.users.get_info()
        print(response)


if __name__ == "__main__":
    main()
