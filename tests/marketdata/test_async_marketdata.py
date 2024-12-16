from datetime import datetime
from unittest.mock import ANY, call

import pytest
import pytest_asyncio

from tinkoff.invest import CandleInterval, GetCandlesResponse
from tinkoff.invest.async_services import AsyncServices, MarketDataService


@pytest_asyncio.fixture
async def marketdata_service(mocker) -> MarketDataService:
    return mocker.create_autospec(MarketDataService)


@pytest_asyncio.fixture
async def async_services(
    mocker, marketdata_service: MarketDataService
) -> AsyncServices:
    async_services = mocker.create_autospec(AsyncServices)
    async_services.market_data = marketdata_service
    return async_services


class TestAsyncMarketData:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "candle_interval,from_,to,expected",
        [
            (
                CandleInterval.CANDLE_INTERVAL_DAY,
                datetime(2020, 1, 1),
                datetime(2020, 1, 2),
                1,
            ),
            (
                CandleInterval.CANDLE_INTERVAL_DAY,
                datetime(2020, 1, 1),
                datetime(2021, 3, 3),
                2,
            ),
        ],
    )
    async def test_get_candles(
        self,
        async_services: AsyncServices,
        marketdata_service: MarketDataService,
        candle_interval: CandleInterval,
        from_: datetime,
        to: datetime,
        expected: int,
    ):
        marketdata_service.get_candles.return_value = GetCandlesResponse(candles=[])
        [
            candle
            async for candle in AsyncServices.get_all_candles(
                async_services, interval=candle_interval, from_=from_, to=to
            )
        ]
        marketdata_service.get_candles.assert_has_calls(
            [
                call(
                    from_=ANY,
                    to=ANY,
                    interval=candle_interval,
                    candle_source_type=None,
                    figi="",
                    instrument_id="",
                )
                for _ in range(expected)
            ]
        )
