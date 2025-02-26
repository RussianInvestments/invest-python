"""Example - How to get Signals with filtering"""

import os

from tinkoff.invest import Client
from tinkoff.invest.schemas import GetSignalsRequest, SignalState

TOKEN = os.environ["INVEST_TOKEN"]


def main():
    with Client(TOKEN) as client:
        request = GetSignalsRequest()
        request.instrument_uid = "e6123145-9665-43e0-8413-cd61b8aa9b13"  # Сбербанк
        request.active = SignalState.SIGNAL_STATE_ACTIVE  # только активные сигналы
        r = client.signals.get_signals(request=request)
        for signal in r.signals:
            print(signal)


if __name__ == "__main__":
    main()
