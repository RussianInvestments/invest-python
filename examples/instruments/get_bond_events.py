import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import EventType, GetBondEventsRequest, InstrumentType

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        bond = client.instruments.find_instrument(
            query="Тинькофф Банк выпуск 1",
            instrument_kind=InstrumentType.INSTRUMENT_TYPE_BOND,
        ).instruments[0]

        request = GetBondEventsRequest(
            instrument_id=bond.uid,
            type=EventType.EVENT_TYPE_CALL,
        )
        print(client.instruments.get_bond_events(request=request))


if __name__ == "__main__":
    main()
