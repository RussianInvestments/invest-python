# Breaking changes
## 0.2.0-beta60
- `MarketDataCache` was moved to [tinkoff/invest/caching/market_data_cache/cache.py](tinkoff/invest/caching/market_data_cache/cache.py).
- The correct import is now `from tinkoff.invest.caching.market_data_cache.cache import MarketDataCache` instead of `from tinkoff.invest.services import MarketDataCache`.
- Import in [download_all_candles.py](examples/download_all_candles.py) was also corrected.