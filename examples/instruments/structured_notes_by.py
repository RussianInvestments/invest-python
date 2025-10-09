import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import InstrumentIdType, InstrumentRequest


def main():
    token = os.environ["INVEST_TOKEN"]

    with Client(token) as client:
        r = client.instruments.structured_note_by(
            request=InstrumentRequest(
                id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_UID,
                id="1d7dfabb-9e82-4de4-8add-8475db83d2bd",
            )
        )
        print(r.instrument)


if __name__ == "__main__":
    main()
