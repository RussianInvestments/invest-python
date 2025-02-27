import contextlib
import dataclasses
import enum
import logging
import os
import pickle  # noqa:S403 # nosec
from pathlib import Path
from typing import Dict, Generator, Sequence

from tinkoff.invest.caching.market_data_cache.datetime_range import DatetimeRange

logger = logging.getLogger(__name__)


class MarketDataCacheFormat(str, enum.Enum):
    CSV = "csv"


@dataclasses.dataclass()
class MarketDataCacheSettings:
    base_cache_dir: Path = Path(os.getcwd()) / ".market_data_cache"
    format_extension: MarketDataCacheFormat = MarketDataCacheFormat.CSV
    field_names: Sequence[str] = (
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "is_complete",
        "candle_source",
    )
    meta_extension: str = "meta"


@dataclasses.dataclass()
class FileMetaData:
    cached_range_in_file: Dict[DatetimeRange, Path]


@contextlib.contextmanager
def meta_file_context(meta_file_path: Path) -> Generator[FileMetaData, None, None]:
    try:
        with open(meta_file_path, "rb") as f:
            meta = pickle.load(f)  # noqa:S301 # nosec
    except FileNotFoundError:
        logger.error("File %s was not found. Creating default.", meta_file_path)

        meta = FileMetaData(cached_range_in_file={})
    try:
        yield meta
    finally:
        with open(meta_file_path, "wb") as f:
            pickle.dump(meta, f)
