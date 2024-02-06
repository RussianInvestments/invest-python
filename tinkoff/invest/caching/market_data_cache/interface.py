from typing import Protocol, TypeVar

from tinkoff.invest.caching.market_data_cache.datetime_range import DatetimeRange

TInstrumentData = TypeVar("TInstrumentData")


class IInstrumentMarketDataStorage(Protocol[TInstrumentData]):
    def get(self, request_range: DatetimeRange) -> TInstrumentData:
        pass

    def update(self, data_list: TInstrumentData):
        pass
