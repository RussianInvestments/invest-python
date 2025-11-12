import asyncio
import logging
from dataclasses import dataclass, fields
from datetime import datetime
from typing import AsyncGenerator, Generator, Optional

import grpc

from tinkoff.invest.grpc.common import Quotation as BaseQuotation
from tinkoff.invest.grpc.instruments import AsyncInstrumentsService, InstrumentsService
from tinkoff.invest.grpc.marketdata import (
    AsyncMarketDataService,
    AsyncMarketDataStreamService,
    CandleInterval,
    CandleSource,
    GetCandlesRequest,
    GetCandlesResponse,
    HistoricCandle,
    MarketDataService,
    MarketDataStreamService,
)
from tinkoff.invest.grpc.operations import (
    AsyncOperationsService,
    AsyncOperationsStreamService,
    OperationsService,
    OperationsStreamService,
)
from tinkoff.invest.grpc.orders import (
    AsyncOrdersService,
    AsyncOrdersStreamService,
    CancelOrderRequest,
    GetOrdersRequest,
    OrdersService,
    OrdersStreamService,
)
from tinkoff.invest.grpc.sandbox import AsyncSandboxService, SandboxService
from tinkoff.invest.grpc.signals import AsyncSignalService, SignalService
from tinkoff.invest.grpc.stoporders import (
    AsyncStopOrdersService,
    CancelStopOrderRequest,
    GetStopOrdersRequest,
    StopOrdersService,
)
from tinkoff.invest.grpc.users import AsyncUsersService, UsersService
from tinkoff.invest.market_data_stream.async_market_data_stream_manager import (
    AsyncMarketDataStreamManager,
)
from tinkoff.invest.market_data_stream.market_data_stream_manager import (
    MarketDataStreamManager,
)
from tinkoff.invest.metadata import get_metadata
from tinkoff.invest.typedefs import AccountId
from tinkoff.invest.utils import get_intervals, now

logger = logging.getLogger(__name__)


class Services:
    def __init__(
        self,
        channel: grpc.Channel,
        token: str,
        sandbox_token: Optional[str] = None,
        app_name: Optional[str] = None,
    ) -> None:
        metadata = get_metadata(token, app_name)
        sandbox_metadata = get_metadata(sandbox_token or token, app_name)
        self.instruments = InstrumentsService(channel, metadata)
        self.market_data = MarketDataService(channel, metadata)
        self.market_data_stream = MarketDataStreamService(channel, metadata)
        self.operations = OperationsService(channel, metadata)
        self.operations_stream = OperationsStreamService(channel, metadata)
        self.orders_stream = OrdersStreamService(channel, metadata)
        self.orders = OrdersService(channel, metadata)
        self.users = UsersService(channel, metadata)
        self.sandbox = SandboxService(channel, sandbox_metadata)
        self.stop_orders = StopOrdersService(channel, metadata)
        self.signals = SignalService(channel, metadata)

    def create_market_data_stream(self) -> MarketDataStreamManager:
        return MarketDataStreamManager(
            market_data_stream_service=self.market_data_stream
        )

    def cancel_all_orders(self, account_id: AccountId) -> None:
        orders_service: OrdersService = self.orders
        stop_orders_service: StopOrdersService = self.stop_orders

        orders_response = orders_service.get_orders(GetOrdersRequest(account_id=account_id))
        for order in orders_response.orders:
            orders_service.cancel_order(CancelOrderRequest(account_id=account_id, order_id=order.order_id))

        stop_orders_response = stop_orders_service.get_stop_orders(
            GetStopOrdersRequest(
                account_id=account_id
            )
        )
        for stop_order in stop_orders_response.stop_orders:
            stop_orders_service.cancel_stop_order(
                CancelStopOrderRequest(
                    account_id=account_id, stop_order_id=stop_order.stop_order_id
                )
            )

    # pylint:disable=too-many-nested-blocks
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
        def make_candle_fields_tuple(candle: HistoricCandle):
            values = []
            for field in fields(candle):
                value = getattr(candle, field.name)
                if field.name == "candle_source":
                    if isinstance(value, int):
                        values.append(value)
                    continue
                elif isinstance(value, BaseQuotation):
                    values.append((value.units, value.nano))
                else:
                    values.append(value)
            return tuple(values)

        to = to or now()
        previous_candles = set()
        for current_from, current_to in get_intervals(interval, from_, to):
            candles_response: GetCandlesResponse = self.market_data.get_candles(
                GetCandlesRequest(
                    figi=figi,
                    interval=interval,
                    from_=current_from,
                    to=current_to,
                    instrument_id=instrument_id,
                    candle_source_type=candle_source_type,
                )
            )

            current_candles = set()
            for candle in candles_response.candles:
                hashable_candle = make_candle_fields_tuple(candle)
                if hashable_candle not in previous_candles and hashable_candle not in current_candles:
                    yield candle
                current_candles.add(hashable_candle)

            previous_candles = current_candles


class AsyncServices:
    def __init__(
        self,
        channel: grpc.aio.Channel,
        token: str,
        sandbox_token: Optional[str] = None,
        app_name: Optional[str] = None,
    ) -> None:
        metadata = get_metadata(token, app_name)
        sandbox_metadata = get_metadata(sandbox_token or token, app_name)
        self.instruments = AsyncInstrumentsService(channel, metadata)
        self.market_data = AsyncMarketDataService(channel, metadata)
        self.market_data_stream = AsyncMarketDataStreamService(channel, metadata)
        self.operations = AsyncOperationsService(channel, metadata)
        self.operations_stream = AsyncOperationsStreamService(channel, metadata)
        self.orders_stream = AsyncOrdersStreamService(channel, metadata)
        self.orders = AsyncOrdersService(channel, metadata)
        self.users = AsyncUsersService(channel, metadata)
        self.sandbox = AsyncSandboxService(channel, sandbox_metadata)
        self.stop_orders = AsyncStopOrdersService(channel, metadata)
        self.signals = AsyncSignalService(channel, metadata)

    def create_market_data_stream(self) -> AsyncMarketDataStreamManager:
        return AsyncMarketDataStreamManager(market_data_stream=self.market_data_stream)

    async def cancel_all_orders(self, account_id: AccountId) -> None:
        orders_service: AsyncOrdersService = self.orders
        stop_orders_service: AsyncStopOrdersService = self.stop_orders

        orders_response = await orders_service.get_orders(GetOrdersRequest(account_id=account_id))
        await asyncio.gather(
            *[
                orders_service.cancel_order(
                    CancelOrderRequest(
                        account_id=account_id, order_id=order.order_id
                    )
                )
                for order in orders_response.orders
            ]
        )

        stop_orders_response = await stop_orders_service.get_stop_orders(
            GetStopOrdersRequest(account_id=account_id)
        )
        await asyncio.gather(
            *[
                stop_orders_service.cancel_stop_order(
                    CancelStopOrderRequest(
                        account_id=account_id, stop_order_id=stop_order.stop_order_id
                    )
                )
                for stop_order in stop_orders_response.stop_orders
            ]
        )

    async def get_all_candles(
        self,
        *,
        from_: datetime,
        to: Optional[datetime] = None,
        interval: CandleInterval = CandleInterval(0),
        figi: str = "",
        instrument_id: str = "",
        candle_source_type: Optional[CandleSource] = None,
    ) -> AsyncGenerator[HistoricCandle, None]:
        to = to or now()

        for local_from_, local_to in get_intervals(interval, from_, to):
            candles_response = await self.market_data.get_candles(
                GetCandlesRequest(
                    figi=figi,
                    interval=interval,
                    from_=local_from_,
                    to=local_to,
                    instrument_id=instrument_id,
                    candle_source_type=candle_source_type,
                )
            )
            for candle in candles_response.candles:
                yield candle



@dataclass(eq=False, repr=True)
class Quotation(BaseQuotation):
    def __init__(self, units: int, nano: int):
        max_quotation_nano = 1_000_000_000
        self.units = units + nano // max_quotation_nano
        self.nano = nano % max_quotation_nano

    def __add__(self, other: "Quotation") -> "Quotation":
        return Quotation(
            units=self.units + other.units,
            nano=self.nano + other.nano,
        )

    def __sub__(self, other: "Quotation") -> "Quotation":
        return Quotation(
            units=self.units - other.units,
            nano=self.nano - other.nano,
        )

    def __hash__(self) -> int:
        return hash((self.units, self.nano))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quotation):
            return NotImplemented
        return self.units == other.units and self.nano == other.nano

    def __lt__(self, other: "Quotation") -> bool:
        return self.units < other.units or (
            self.units == other.units and self.nano < other.nano
        )

    def __le__(self, other: "Quotation") -> bool:
        return self.units < other.units or (
            self.units == other.units and self.nano <= other.nano
        )

    def __gt__(self, other: "Quotation") -> bool:
        return self.units > other.units or (
            self.units == other.units and self.nano > other.nano
        )

    def __ge__(self, other: "Quotation") -> bool:
        return self.units > other.units or (
            self.units == other.units and self.nano >= other.nano
        )

    def __abs__(self) -> "Quotation":
        return Quotation(units=abs(self.units), nano=abs(self.nano))
