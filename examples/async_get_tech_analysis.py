import asyncio
import os
from datetime import timedelta
from decimal import Decimal

from tinkoff.invest import AsyncClient
from tinkoff.invest.schemas import (
    Deviation,
    GetTechAnalysisRequest,
    IndicatorInterval,
    IndicatorType,
    Smoothing,
    TypeOfPrice,
)
from tinkoff.invest.utils import decimal_to_quotation, now

TOKEN = os.environ["INVEST_TOKEN"]


async def main():
    async with AsyncClient(TOKEN) as client:
        request = GetTechAnalysisRequest(
            indicator_type=IndicatorType.INDICATOR_TYPE_RSI,
            instrument_uid="6542a064-6633-44ba-902f-710c97507522",
            from_=now() - timedelta(days=7),
            to=now(),
            interval=IndicatorInterval.INDICATOR_INTERVAL_4_HOUR,
            type_of_price=TypeOfPrice.TYPE_OF_PRICE_AVG,
            length=42,
            deviation=Deviation(
                deviation_multiplier=decimal_to_quotation(Decimal(1.0)),
            ),
            smoothing=Smoothing(fast_length=13, slow_length=7, signal_smoothing=3),
        )
        response = await client.market_data.get_tech_analysis(request=request)
        for indicator in response.technical_indicators:
            print(indicator.signal)


if __name__ == "__main__":
    asyncio.run(main())
