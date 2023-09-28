import abc
from typing import Generic, Iterable, TypeVar

from tinkoff.invest.caching.market_data_cache.datetime_range import DatetimeRange
from tinkoff.invest.caching.market_data_cache.instrument_date_range_market_data import (
    InstrumentDateRangeData,
)

TInstrumentData = TypeVar("TInstrumentData")


class IInstrumentMarketDataStorage(abc.ABC, Generic[TInstrumentData]):
    def get(self, request_range: DatetimeRange) -> Iterable[InstrumentDateRangeData]:
        pass

    def update(self, data_list: Iterable[InstrumentDateRangeData]):
        pass
