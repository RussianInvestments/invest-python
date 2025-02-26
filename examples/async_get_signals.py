"""Example - How to get Signals"""
import asyncio
import datetime
import os

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import GetSignalsRequest, SignalState

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        request = GetSignalsRequest()
        request.instrument_uid = "e6123145-9665-43e0-8413-cd61b8aa9b13"  # Сбербанк
        request.active = SignalState.SIGNAL_STATE_ALL  # все сигналы
        request.from_ = datetime.datetime.now() - datetime.timedelta(
            weeks=4
        )  # сигналы, созданные не больше чем 4 недели назад
        r = await client.signals.get_signals(request=request)
        for signal in r.signals:
            print(signal)


if __name__ == "__main__":
    asyncio.run(main())
