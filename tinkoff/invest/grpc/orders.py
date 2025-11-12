from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import AsyncIterable, Iterable, List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest import _grpc_helpers
from tinkoff.invest._errors import (
    handle_aio_request_error,
    handle_aio_request_error_gen,
    handle_request_error,
    handle_request_error_gen,
)
from tinkoff.invest.grpc import orders_pb2, orders_pb2_grpc
from tinkoff.invest.grpc.common import (
    ErrorDetail,
    MoneyValue,
    Ping,
    PriceType,
    Quotation,
    ResponseMetadata,
    ResultSubscriptionStatus,
)
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


class OrderDirection(IntEnum):
    ORDER_DIRECTION_UNSPECIFIED = 0
    ORDER_DIRECTION_BUY = 1
    ORDER_DIRECTION_SELL = 2


class OrderType(IntEnum):
    ORDER_TYPE_UNSPECIFIED = 0
    ORDER_TYPE_LIMIT = 1
    ORDER_TYPE_MARKET = 2
    ORDER_TYPE_BESTPRICE = 3


class OrderExecutionReportStatus(IntEnum):
    EXECUTION_REPORT_STATUS_UNSPECIFIED = 0
    EXECUTION_REPORT_STATUS_FILL = 1
    EXECUTION_REPORT_STATUS_REJECTED = 2
    EXECUTION_REPORT_STATUS_CANCELLED = 3
    EXECUTION_REPORT_STATUS_NEW = 4
    EXECUTION_REPORT_STATUS_PARTIALLYFILL = 5


class TimeInForceType(IntEnum):
    TIME_IN_FORCE_UNSPECIFIED = 0
    TIME_IN_FORCE_DAY = 1
    TIME_IN_FORCE_FILL_AND_KILL = 2
    TIME_IN_FORCE_FILL_OR_KILL = 3


class OrderIdType(IntEnum):
    ORDER_ID_TYPE_UNSPECIFIED = 0
    ORDER_ID_TYPE_EXCHANGE = 1
    ORDER_ID_TYPE_REQUEST = 2


@dataclass
class TradesStreamRequest(_grpc_helpers.Message):
    accounts: List[str] = _grpc_helpers.string_field(1)
    ping_delay_ms: Optional[int] = _grpc_helpers.int32_field(15, optional=True)


@dataclass
class TradesStreamResponse(_grpc_helpers.Message):
    order_trades: Optional['OrderTrades'] = _grpc_helpers.message_field(1,
        optional=True)
    ping: Optional['Ping'] = _grpc_helpers.message_field(2, optional=True)
    subscription: Optional['SubscriptionResponse'
        ] = _grpc_helpers.message_field(3, optional=True)


@dataclass
class OrderTrades(_grpc_helpers.Message):
    order_id: str = _grpc_helpers.string_field(1)
    created_at: datetime = _grpc_helpers.message_field(2)
    direction: 'OrderDirection' = _grpc_helpers.message_field(3)
    figi: str = _grpc_helpers.string_field(4)
    trades: List['OrderTrade'] = _grpc_helpers.message_field(5)
    account_id: str = _grpc_helpers.string_field(6)
    instrument_uid: str = _grpc_helpers.string_field(7)


@dataclass
class OrderTrade(_grpc_helpers.Message):
    date_time: datetime = _grpc_helpers.message_field(1)
    price: 'Quotation' = _grpc_helpers.message_field(2)
    quantity: int = _grpc_helpers.int64_field(3)
    trade_id: str = _grpc_helpers.string_field(4)


@dataclass
class PostOrderRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    quantity: int = _grpc_helpers.int64_field(2)
    price: Optional['Quotation'] = _grpc_helpers.message_field(3, optional=True
        )
    direction: 'OrderDirection' = _grpc_helpers.message_field(4)
    account_id: str = _grpc_helpers.string_field(5)
    order_type: 'OrderType' = _grpc_helpers.message_field(6)
    order_id: str = _grpc_helpers.string_field(7)
    instrument_id: str = _grpc_helpers.string_field(8)
    time_in_force: 'TimeInForceType' = _grpc_helpers.message_field(9)
    price_type: 'PriceType' = _grpc_helpers.message_field(10)
    confirm_margin_trade: bool = _grpc_helpers.bool_field(11)


@dataclass
class PostOrderResponse(_grpc_helpers.Message):
    order_id: str = _grpc_helpers.string_field(1)
    execution_report_status: 'OrderExecutionReportStatus' = (_grpc_helpers.
        message_field(2))
    lots_requested: int = _grpc_helpers.int64_field(3)
    lots_executed: int = _grpc_helpers.int64_field(4)
    initial_order_price: 'MoneyValue' = _grpc_helpers.message_field(5)
    executed_order_price: 'MoneyValue' = _grpc_helpers.message_field(6)
    total_order_amount: 'MoneyValue' = _grpc_helpers.message_field(7)
    initial_commission: 'MoneyValue' = _grpc_helpers.message_field(8)
    executed_commission: 'MoneyValue' = _grpc_helpers.message_field(9)
    aci_value: 'MoneyValue' = _grpc_helpers.message_field(10)
    figi: str = _grpc_helpers.string_field(11)
    direction: 'OrderDirection' = _grpc_helpers.message_field(12)
    initial_security_price: 'MoneyValue' = _grpc_helpers.message_field(13)
    order_type: 'OrderType' = _grpc_helpers.message_field(14)
    message: str = _grpc_helpers.string_field(15)
    initial_order_price_pt: 'Quotation' = _grpc_helpers.message_field(16)
    instrument_uid: str = _grpc_helpers.string_field(17)
    order_request_id: str = _grpc_helpers.string_field(20)
    response_metadata: 'ResponseMetadata' = _grpc_helpers.message_field(254)


@dataclass
class PostOrderAsyncRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)
    quantity: int = _grpc_helpers.int64_field(2)
    price: Optional['Quotation'] = _grpc_helpers.message_field(3, optional=True
        )
    direction: 'OrderDirection' = _grpc_helpers.message_field(4)
    account_id: str = _grpc_helpers.string_field(5)
    order_type: 'OrderType' = _grpc_helpers.message_field(6)
    order_id: str = _grpc_helpers.string_field(7)
    time_in_force: Optional['TimeInForceType'] = _grpc_helpers.message_field(
        8, optional=True)
    price_type: Optional['PriceType'] = _grpc_helpers.message_field(9,
        optional=True)
    confirm_margin_trade: bool = _grpc_helpers.bool_field(10)


@dataclass
class PostOrderAsyncResponse(_grpc_helpers.Message):
    order_request_id: str = _grpc_helpers.string_field(1)
    execution_report_status: 'OrderExecutionReportStatus' = (_grpc_helpers.
        message_field(2))
    trade_intent_id: Optional[str] = _grpc_helpers.string_field(3, optional
        =True)


@dataclass
class CancelOrderRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    order_id: str = _grpc_helpers.string_field(2)
    order_id_type: Optional['OrderIdType'] = _grpc_helpers.message_field(3,
        optional=True)


@dataclass
class CancelOrderResponse(_grpc_helpers.Message):
    time: datetime = _grpc_helpers.message_field(1)
    response_metadata: 'ResponseMetadata' = _grpc_helpers.message_field(254)


@dataclass
class GetOrderStateRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    order_id: str = _grpc_helpers.string_field(2)
    price_type: 'PriceType' = _grpc_helpers.message_field(3)
    order_id_type: Optional['OrderIdType'] = _grpc_helpers.message_field(4,
        optional=True)


@dataclass
class GetOrdersRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    advanced_filters: Optional['GetOrdersRequestFilters'
        ] = _grpc_helpers.message_field(2, optional=True)


    @dataclass
    class GetOrdersRequestFilters(_grpc_helpers.Message):
        from_: Optional[datetime] = _grpc_helpers.message_field(1, optional
            =True)
        to: Optional[datetime] = _grpc_helpers.message_field(2, optional=True)
        execution_status: List['OrderExecutionReportStatus'
            ] = _grpc_helpers.message_field(3)


@dataclass
class GetOrdersResponse(_grpc_helpers.Message):
    orders: List['OrderState'] = _grpc_helpers.message_field(1)


@dataclass
class OrderState(_grpc_helpers.Message):
    order_id: str = _grpc_helpers.string_field(1)
    execution_report_status: 'OrderExecutionReportStatus' = (_grpc_helpers.
        message_field(2))
    lots_requested: int = _grpc_helpers.int64_field(3)
    lots_executed: int = _grpc_helpers.int64_field(4)
    initial_order_price: 'MoneyValue' = _grpc_helpers.message_field(5)
    executed_order_price: 'MoneyValue' = _grpc_helpers.message_field(6)
    total_order_amount: 'MoneyValue' = _grpc_helpers.message_field(7)
    average_position_price: 'MoneyValue' = _grpc_helpers.message_field(8)
    initial_commission: 'MoneyValue' = _grpc_helpers.message_field(9)
    executed_commission: 'MoneyValue' = _grpc_helpers.message_field(10)
    figi: str = _grpc_helpers.string_field(11)
    direction: 'OrderDirection' = _grpc_helpers.message_field(12)
    initial_security_price: 'MoneyValue' = _grpc_helpers.message_field(13)
    stages: List['OrderStage'] = _grpc_helpers.message_field(14)
    service_commission: 'MoneyValue' = _grpc_helpers.message_field(15)
    currency: str = _grpc_helpers.string_field(16)
    order_type: 'OrderType' = _grpc_helpers.message_field(17)
    order_date: datetime = _grpc_helpers.message_field(18)
    instrument_uid: str = _grpc_helpers.string_field(19)
    order_request_id: str = _grpc_helpers.string_field(20)


@dataclass
class OrderStage(_grpc_helpers.Message):
    price: 'MoneyValue' = _grpc_helpers.message_field(1)
    quantity: int = _grpc_helpers.int64_field(2)
    trade_id: str = _grpc_helpers.string_field(3)
    execution_time: datetime = _grpc_helpers.message_field(5)


@dataclass
class ReplaceOrderRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    order_id: str = _grpc_helpers.string_field(6)
    idempotency_key: str = _grpc_helpers.string_field(7)
    quantity: int = _grpc_helpers.int64_field(11)
    price: Optional['Quotation'] = _grpc_helpers.message_field(12, optional
        =True)
    price_type: Optional['PriceType'] = _grpc_helpers.message_field(13,
        optional=True)
    confirm_margin_trade: bool = _grpc_helpers.bool_field(14)


@dataclass
class GetMaxLotsRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)
    price: Optional['Quotation'] = _grpc_helpers.message_field(3, optional=True
        )


@dataclass
class GetMaxLotsResponse(_grpc_helpers.Message):
    currency: str = _grpc_helpers.string_field(1)
    buy_limits: 'BuyLimitsView' = _grpc_helpers.message_field(2)
    buy_margin_limits: 'BuyLimitsView' = _grpc_helpers.message_field(3)
    sell_limits: 'SellLimitsView' = _grpc_helpers.message_field(4)
    sell_margin_limits: 'SellLimitsView' = _grpc_helpers.message_field(5)


    @dataclass
    class BuyLimitsView(_grpc_helpers.Message):
        buy_money_amount: 'Quotation' = _grpc_helpers.message_field(1)
        buy_max_lots: int = _grpc_helpers.int64_field(2)
        buy_max_market_lots: int = _grpc_helpers.int64_field(3)


    @dataclass
    class SellLimitsView(_grpc_helpers.Message):
        sell_max_lots: int = _grpc_helpers.int64_field(1)


@dataclass
class GetOrderPriceRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)
    price: 'Quotation' = _grpc_helpers.message_field(3)
    direction: 'OrderDirection' = _grpc_helpers.message_field(12)
    quantity: int = _grpc_helpers.int64_field(13)


@dataclass
class GetOrderPriceResponse(_grpc_helpers.Message):
    total_order_amount: 'MoneyValue' = _grpc_helpers.message_field(1)
    initial_order_amount: 'MoneyValue' = _grpc_helpers.message_field(5)
    lots_requested: int = _grpc_helpers.int64_field(3)
    executed_commission: 'MoneyValue' = _grpc_helpers.message_field(7)
    executed_commission_rub: 'MoneyValue' = _grpc_helpers.message_field(8)
    service_commission: 'MoneyValue' = _grpc_helpers.message_field(9)
    deal_commission: 'MoneyValue' = _grpc_helpers.message_field(10)
    extra_bond: Optional['ExtraBond'] = _grpc_helpers.message_field(12,
        optional=True)
    extra_future: Optional['ExtraFuture'] = _grpc_helpers.message_field(13,
        optional=True)


    @dataclass
    class ExtraBond(_grpc_helpers.Message):
        aci_value: 'MoneyValue' = _grpc_helpers.message_field(2)
        nominal_conversion_rate: 'Quotation' = _grpc_helpers.message_field(3)


    @dataclass
    class ExtraFuture(_grpc_helpers.Message):
        initial_margin: 'MoneyValue' = _grpc_helpers.message_field(2)


@dataclass
class OrderStateStreamRequest(_grpc_helpers.Message):
    accounts: List[str] = _grpc_helpers.string_field(1)
    ping_delay_millis: Optional[int] = _grpc_helpers.int32_field(15,
        optional=True)


@dataclass
class SubscriptionResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    status: 'ResultSubscriptionStatus' = _grpc_helpers.message_field(2)
    stream_id: str = _grpc_helpers.string_field(4)
    accounts: List[str] = _grpc_helpers.string_field(5)
    error: Optional['ErrorDetail'] = _grpc_helpers.message_field(7,
        optional=True)


@dataclass
class OrderStateStreamResponse(_grpc_helpers.Message):
    order_state: Optional['OrderState'] = _grpc_helpers.message_field(1,
        optional=True)
    ping: Optional['Ping'] = _grpc_helpers.message_field(2, optional=True)
    subscription: Optional['SubscriptionResponse'
        ] = _grpc_helpers.message_field(3, optional=True)


    @dataclass
    class OrderState(_grpc_helpers.Message):
        order_id: str = _grpc_helpers.string_field(1)
        order_request_id: Optional[str] = _grpc_helpers.string_field(2,
            optional=True)
        client_code: str = _grpc_helpers.string_field(3)
        created_at: datetime = _grpc_helpers.message_field(4)
        execution_report_status: 'OrderExecutionReportStatus' = (_grpc_helpers
            .message_field(5))
        status_info: Optional['StatusCauseInfo'] = _grpc_helpers.message_field(
            6, optional=True)
        ticker: str = _grpc_helpers.string_field(7)
        class_code: str = _grpc_helpers.string_field(8)
        lot_size: int = _grpc_helpers.int32_field(9)
        direction: 'OrderDirection' = _grpc_helpers.message_field(10)
        time_in_force: 'TimeInForceType' = _grpc_helpers.message_field(11)
        order_type: 'OrderType' = _grpc_helpers.message_field(12)
        account_id: str = _grpc_helpers.string_field(13)
        initial_order_price: 'MoneyValue' = _grpc_helpers.message_field(22)
        order_price: 'MoneyValue' = _grpc_helpers.message_field(23)
        amount: Optional['MoneyValue'] = _grpc_helpers.message_field(24,
            optional=True)
        executed_order_price: 'MoneyValue' = _grpc_helpers.message_field(25)
        currency: str = _grpc_helpers.string_field(26)
        lots_requested: int = _grpc_helpers.int64_field(27)
        lots_executed: int = _grpc_helpers.int64_field(28)
        lots_left: int = _grpc_helpers.int64_field(29)
        lots_cancelled: int = _grpc_helpers.int64_field(30)
        marker: Optional['MarkerType'] = _grpc_helpers.message_field(31,
            optional=True)
        trades: List['OrderTrade'] = _grpc_helpers.message_field(33)
        completion_time: datetime = _grpc_helpers.message_field(35)
        exchange: str = _grpc_helpers.string_field(36)
        instrument_uid: str = _grpc_helpers.string_field(41)


    class MarkerType(IntEnum):
        MARKER_UNKNOWN = 0
        MARKER_BROKER = 1
        MARKER_CHAT = 2
        MARKER_PAPER = 3
        MARKER_MARGIN = 4
        MARKER_TKBNM = 5
        MARKER_SHORT = 6
        MARKER_SPECMM = 7
        MARKER_PO = 8


    class StatusCauseInfo(IntEnum):
        CAUSE_UNSPECIFIED = 0
        CAUSE_CANCELLED_BY_CLIENT = 15
        CAUSE_CANCELLED_BY_EXCHANGE = 1
        CAUSE_CANCELLED_NOT_ENOUGH_POSITION = 2
        CAUSE_CANCELLED_BY_CLIENT_BLOCK = 3
        CAUSE_REJECTED_BY_BROKER = 4
        CAUSE_REJECTED_BY_EXCHANGE = 5
        CAUSE_CANCELLED_BY_BROKER = 6


class OrdersStreamService(BaseService):
    """//TradesStream — стрим сделок пользователя"""
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersStreamServiceStub

    @handle_request_error_gen('TradesStream')
    def trades_stream(self, request: 'TradesStreamRequest'=
        TradesStreamRequest()) ->Iterable['TradesStreamResponse']:
        for response in self._stub.TradesStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            TradesStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, TradesStreamResponse)

    @handle_request_error_gen('OrderStateStream')
    def order_state_stream(self, request: 'OrderStateStreamRequest'=
        OrderStateStreamRequest()) ->Iterable['OrderStateStreamResponse']:
        for response in self._stub.OrderStateStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            OrderStateStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, OrderStateStreamResponse)


class AsyncOrdersStreamService(BaseService):
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersStreamServiceStub

    @handle_aio_request_error_gen('TradesStream')
    async def trades_stream(self, request: 'TradesStreamRequest'=
        TradesStreamRequest()) ->AsyncIterable['TradesStreamResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            TradesStreamRequest())
        async for response in self._stub.TradesStream(request=
            protobuf_request, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, TradesStreamResponse))

    @handle_aio_request_error_gen('OrderStateStream')
    async def order_state_stream(self, request: 'OrderStateStreamRequest'=
        OrderStateStreamRequest()) ->AsyncIterable['OrderStateStreamResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OrderStateStreamRequest())
        async for response in self._stub.OrderStateStream(request=
            protobuf_request, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, OrderStateStreamResponse))


class OrdersService(BaseService):
    """/* Сервис предназначен для работы с торговыми поручениями:<br/> **1**.
                        выставление;<br/> **2**. отмена;<br/> **3**. получение статуса;<br/> **4**.
                        расчет полной стоимости;<br/> **5**. получение списка заявок.*/"""
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersServiceStub

    @handle_request_error('PostOrder')
    def post_order(self, request: 'PostOrderRequest'=PostOrderRequest()
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response, call = self._stub.PostOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_request_error('PostOrderAsync')
    def post_order_async(self, request: 'PostOrderAsyncRequest'=
        PostOrderAsyncRequest()) ->'PostOrderAsyncResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderAsyncRequest())
        response, call = self._stub.PostOrderAsync.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostOrderAsync')
        return protobuf_to_dataclass(response, PostOrderAsyncResponse)

    @handle_request_error('CancelOrder')
    def cancel_order(self, request: 'CancelOrderRequest'=CancelOrderRequest()
        ) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response, call = self._stub.CancelOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CancelOrder')
        return protobuf_to_dataclass(response, CancelOrderResponse)

    @handle_request_error('GetOrderState')
    def get_order_state(self, request: 'GetOrderStateRequest'=
        GetOrderStateRequest()) ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response, call = self._stub.GetOrderState.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOrderState')
        return protobuf_to_dataclass(response, OrderState)

    @handle_request_error('GetOrders')
    def get_orders(self, request: 'GetOrdersRequest'=GetOrdersRequest()
        ) ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response, call = self._stub.GetOrders.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOrders')
        return protobuf_to_dataclass(response, GetOrdersResponse)

    @handle_request_error('ReplaceOrder')
    def replace_order(self, request: 'ReplaceOrderRequest'=
        ReplaceOrderRequest()) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response, call = self._stub.ReplaceOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'ReplaceOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_request_error('GetMaxLots')
    def get_max_lots(self, request: 'GetMaxLotsRequest'=GetMaxLotsRequest()
        ) ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response, call = self._stub.GetMaxLots.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetMaxLots')
        return protobuf_to_dataclass(response, GetMaxLotsResponse)

    @handle_request_error('GetOrderPrice')
    def get_order_price(self, request: 'GetOrderPriceRequest'=
        GetOrderPriceRequest()) ->'GetOrderPriceResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderPriceRequest())
        response, call = self._stub.GetOrderPrice.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOrderPrice')
        return protobuf_to_dataclass(response, GetOrderPriceResponse)


class AsyncOrdersService(BaseService):
    """//PostOrder — выставить заявку"""
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersServiceStub

    @handle_aio_request_error('PostOrder')
    async def post_order(self, request: 'PostOrderRequest'=PostOrderRequest()
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response_coro = self._stub.PostOrder(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'PostOrder'
            )
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_aio_request_error('PostOrderAsync')
    async def post_order_async(self, request: 'PostOrderAsyncRequest'=
        PostOrderAsyncRequest()) ->'PostOrderAsyncResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderAsyncRequest())
        response_coro = self._stub.PostOrderAsync(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'PostOrderAsync')
        return protobuf_to_dataclass(response, PostOrderAsyncResponse)

    @handle_aio_request_error('CancelOrder')
    async def cancel_order(self, request: 'CancelOrderRequest'=
        CancelOrderRequest()) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response_coro = self._stub.CancelOrder(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'CancelOrder')
        return protobuf_to_dataclass(response, CancelOrderResponse)

    @handle_aio_request_error('GetOrderState')
    async def get_order_state(self, request: 'GetOrderStateRequest'=
        GetOrderStateRequest()) ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response_coro = self._stub.GetOrderState(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetOrderState')
        return protobuf_to_dataclass(response, OrderState)

    @handle_aio_request_error('GetOrders')
    async def get_orders(self, request: 'GetOrdersRequest'=GetOrdersRequest()
        ) ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response_coro = self._stub.GetOrders(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'GetOrders'
            )
        return protobuf_to_dataclass(response, GetOrdersResponse)

    @handle_aio_request_error('ReplaceOrder')
    async def replace_order(self, request: 'ReplaceOrderRequest'=
        ReplaceOrderRequest()) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response_coro = self._stub.ReplaceOrder(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'ReplaceOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_aio_request_error('GetMaxLots')
    async def get_max_lots(self, request: 'GetMaxLotsRequest'=
        GetMaxLotsRequest()) ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response_coro = self._stub.GetMaxLots(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetMaxLots')
        return protobuf_to_dataclass(response, GetMaxLotsResponse)

    @handle_aio_request_error('GetOrderPrice')
    async def get_order_price(self, request: 'GetOrderPriceRequest'=
        GetOrderPriceRequest()) ->'GetOrderPriceResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderPriceRequest())
        response_coro = self._stub.GetOrderPrice(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetOrderPrice')
        return protobuf_to_dataclass(response, GetOrderPriceResponse)
