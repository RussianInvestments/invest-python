from datetime import datetime
from typing import Generator, Optional, Protocol

from tinkoff.invest import CandleInterval, HistoricCandle


class CandleGetter(Protocol):
    def get_all_candles(  # pragma: no cover
        self,
        *,
        from_: datetime,
        to: Optional[datetime],
        interval: CandleInterval,
        figi: str,
    ) -> Generator[HistoricCandle, None, None]:
        pass
