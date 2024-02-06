# pylint: disable=redefined-outer-name,unused-variable
import datetime
import os
import tempfile
from datetime import timedelta
from pathlib import Path
from typing import Dict, Iterable

import pytest

from tinkoff.invest import CandleInterval
from tinkoff.invest.caching.market_data_cache.cache import MarketDataCache
from tinkoff.invest.caching.market_data_cache.cache_settings import (
    MarketDataCacheSettings,
)
from tinkoff.invest.sandbox.client import SandboxClient
from tinkoff.invest.utils import now


@pytest.fixture()
def sandbox_service():
    with SandboxClient(token=os.environ["INVEST_SANDBOX_TOKEN"]) as client:
        yield client


PROGRAMMERS_DAY = datetime.datetime(
    2023, 1, 1, tzinfo=datetime.timezone.utc
) + timedelta(days=255)


@pytest.mark.skipif(
    os.environ.get("INVEST_SANDBOX_TOKEN") is None,
    reason="INVEST_SANDBOX_TOKEN should be specified",
)
@pytest.mark.skip("todo fix")
class TestSandboxCachedLoad:
    @pytest.mark.parametrize(
        "calls_kwargs",
        [
            ({"from_": now() - timedelta(days=8)},),
            (
                {
                    "from_": datetime.datetime(
                        2023, 9, 1, 0, 0, tzinfo=datetime.timezone.utc
                    ),
                    "to": datetime.datetime(
                        2023, 9, 5, 0, 0, tzinfo=datetime.timezone.utc
                    ),
                },
            ),
            (
                {
                    "from_": now() - timedelta(days=6),
                },
                {
                    "from_": now() - timedelta(days=10),
                    "to": now() - timedelta(days=7),
                },
                {
                    "from_": now() - timedelta(days=11),
                    "to": now() - timedelta(days=5),
                },
            ),
            (
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=6),
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=6),
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=6),
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=6),
                },
            ),
            (
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=6),
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=5),
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=4),
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=3),
                },
            ),
            (
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=6),
                    "to": PROGRAMMERS_DAY,
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=5),
                    "to": PROGRAMMERS_DAY,
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=4),
                    "to": PROGRAMMERS_DAY,
                },
                {
                    "from_": PROGRAMMERS_DAY - timedelta(days=3),
                    "to": PROGRAMMERS_DAY,
                },
            ),
        ],
    )
    def test_same_from_net_and_cache(
        self, sandbox_service, calls_kwargs: Iterable[Dict[str, datetime]]
    ):
        settings = MarketDataCacheSettings(base_cache_dir=Path(tempfile.gettempdir()))
        market_data_cache = MarketDataCache(settings=settings, services=sandbox_service)
        figi = "BBG004730N88"
        for date_range_kwargs in calls_kwargs:
            call_kwargs = dict(
                figi=figi,
                interval=CandleInterval.CANDLE_INTERVAL_DAY,
                **date_range_kwargs,
            )

            candles_from_cache = list(market_data_cache.get_all_candles(**call_kwargs))
            candles_from_net = list(sandbox_service.get_all_candles(**call_kwargs))
            assert candles_from_cache
            assert candles_from_net
            assert candles_from_cache == candles_from_net, (
                candles_from_cache,
                candles_from_net,
            )
