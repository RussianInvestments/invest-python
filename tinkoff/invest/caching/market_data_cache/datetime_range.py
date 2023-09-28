from datetime import datetime
from typing import NewType, Tuple

DatetimeRange = NewType("DatetimeRange", Tuple[datetime, datetime])
