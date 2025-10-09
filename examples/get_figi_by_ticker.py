import os
from tinkoff.invest import Client

TOKEN = os.environ["INVEST_TOKEN"]
#or TOKEN = "PASTE YOUR TOKEN HERE"

TICKER = "LKOH"

def main():
    with Client(TOKEN) as client:
        r = client.instruments.find_instrument(query=TICKER)
        for i in r.instruments:
            if getattr(i, "ticker") == TICKER:
                print(getattr(i, "figi"))


if __name__ == "__main__":
    main()
