import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import AssetsRequest, InstrumentStatus, InstrumentType

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        r = client.instruments.get_assets(
            request=AssetsRequest(instrument_type=InstrumentType.INSTRUMENT_TYPE_BOND)
        )
        print("BONDS")
        for bond in r.assets:
            print(bond)
        r = client.instruments.get_assets(
            request=AssetsRequest(
                instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE
            )
        )
        print("BASE ASSETS")
        for bond in r.assets:
            print(bond)


if __name__ == "__main__":
    main()
