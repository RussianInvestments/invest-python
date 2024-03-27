import logging
from datetime import datetime, timedelta
from typing import Dict, Generator, Iterable, Optional, Tuple

from tinkoff.invest import CandleInterval, HistoricCandle
from tinkoff.invest.caching.market_data_cache.cache_settings import (
    MarketDataCacheSettings,
)
from tinkoff.invest.caching.market_data_cache.datetime_range import DatetimeRange
from tinkoff.invest.caching.market_data_cache.instrument_date_range_market_data import (
    InstrumentDateRangeData,
)
from tinkoff.invest.caching.market_data_cache.instrument_market_data_storage import (
    InstrumentMarketDataStorage,
)
from tinkoff.invest.schemas import CandleSource
from tinkoff.invest.services import Services
from tinkoff.invest.utils import (
    candle_interval_to_timedelta,
    floor_datetime,
    now,
    round_datetime_range,
    with_filtering_distinct_candles,
)

logger = logging.getLogger(__name__)


class MarketDataCache:
    def __init__(self, settings: MarketDataCacheSettings, services: Services):
        self._settings = settings
        self._settings.base_cache_dir.mkdir(parents=True, exist_ok=True)
        self._services = services
        self._figi_cache_storages: Dict[
            Tuple[str, CandleInterval], InstrumentMarketDataStorage
        ] = {}

    def _get_candles_from_net(
        self,
        figi: str,
        interval: CandleInterval,
        from_: datetime,
        to: datetime,
        instrument_id: str = "",
        candle_source_type: Optional[CandleSource] = None,
    ) -> Iterable[HistoricCandle]:
        yield from self._services.get_all_candles(
            figi=figi,
            interval=interval,
            from_=from_,
            to=to,
            instrument_id=instrument_id,
            candle_source_type=candle_source_type,
        )

    def _with_saving_into_cache(
        self,
        storage: InstrumentMarketDataStorage,
        from_net: Iterable[HistoricCandle],
    ) -> Iterable[HistoricCandle]:
        candles = list(from_net)
        if candles:
            complete_candles = list(self._filter_complete_candles(candles))
            complete_candle_times = [candle.time for candle in complete_candles]
            complete_net_range = (
                min(complete_candle_times),
                max(complete_candle_times),
            )
            storage.update(
                [
                    InstrumentDateRangeData(
                        date_range=complete_net_range,
                        historic_candles=complete_candles,
                    )
                ]
            )

        yield from candles

    def _filter_complete_candles(
        self, candles: Iterable[HistoricCandle]
    ) -> Iterable[HistoricCandle]:
        return filter(lambda candle: candle.is_complete, candles)

    @with_filtering_distinct_candles  # type: ignore
    def get_all_candles(
        self,
        *,
        from_: datetime,
        to: Optional[datetime] = None,
        interval: CandleInterval = CandleInterval(0),
        figi: str = "",
        instrument_id: str = "",
        candle_source_type: Optional[CandleSource] = None,
    ) -> Generator[HistoricCandle, None, None]:
        interval_delta = candle_interval_to_timedelta(interval)
        to = to or now()

        processed_time = from_
        figi_cache_storage = self._get_figi_cache_storage(figi=figi, interval=interval)
        for cached in figi_cache_storage.get(
            request_range=round_datetime_range(
                date_range=(from_, to), interval=interval
            )
        ):
            cached_start, cached_end = cached.date_range
            cached_candles = list(cached.historic_candles)
            if cached_start > processed_time:
                yield from self._with_saving_into_cache(
                    storage=figi_cache_storage,
                    from_net=self._get_candles_from_net(
                        figi=figi,
                        interval=interval,
                        from_=processed_time,
                        to=cached_start,
                        instrument_id=instrument_id,
                        candle_source_type=candle_source_type,
                    ),
                )

            yield from cached_candles
            processed_time = cached_end

        if processed_time + interval_delta <= to:
            yield from self._with_saving_into_cache(
                storage=figi_cache_storage,
                from_net=self._get_candles_from_net(figi, interval, processed_time, to),
            )

        figi_cache_storage.merge()

    def _get_figi_cache_storage(
        self, figi: str, interval: CandleInterval
    ) -> InstrumentMarketDataStorage:
        figi_tuple = (figi, interval)
        storage = self._figi_cache_storages.get(figi_tuple)
        if storage is None:
            storage = InstrumentMarketDataStorage(
                figi=figi, interval=interval, settings=self._settings
            )
            self._figi_cache_storages[figi_tuple] = storage
        return storage  # noqa:R504

    def _round_net_range(
        self, net_range: DatetimeRange, interval_delta: timedelta
    ) -> DatetimeRange:
        start, end = net_range
        return floor_datetime(start, interval_delta), floor_datetime(
            end, interval_delta
        )
