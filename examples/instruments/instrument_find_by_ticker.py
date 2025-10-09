import os

from tinkoff.invest import Client, InstrumentIdType

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        r = client.instruments.get_instrument_by(
            id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER,
            id="LKOH",
            class_code="TQBR",
        )
        print(r.instrument)


if __name__ == "__main__":
    main()
