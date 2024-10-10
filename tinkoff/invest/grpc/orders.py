from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Iterable, List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
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


class OrdersStreamService(BaseService):
    """//Stream сделок пользователя"""
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersStreamServiceStub

    def TradesStream(self, request: 'TradesStreamRequest') ->Iterable[
        'TradesStreamResponse']:
        for response in self._stub.TradesStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            TradesStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, TradesStreamResponse)

    def OrderStateStream(self, request: 'OrderStateStreamRequest') ->Iterable[
        'OrderStateStreamResponse']:
        for response in self._stub.OrderStateStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            OrderStateStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, OrderStateStreamResponse)


class OrdersService(BaseService):
    """/* Сервис предназначен для работы с торговыми поручениями:</br> **1**.
                        выставление;</br> **2**. отмена;</br> **3**. получение статуса;</br> **4**.
                        расчёт полной стоимости;</br> **5**. получение списка заявок.*/"""
    _protobuf = orders_pb2
    _protobuf_grpc = orders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OrdersServiceStub

    def PostOrder(self, request: 'PostOrderRequest') ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response, call = self._stub.PostOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PostOrderResponse)

    def PostOrderAsync(self, request: 'PostOrderAsyncRequest'
        ) ->'PostOrderAsyncResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderAsyncRequest())
        response, call = self._stub.PostOrderAsync.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PostOrderAsyncResponse)

    def CancelOrder(self, request: 'CancelOrderRequest'
        ) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response, call = self._stub.CancelOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, CancelOrderResponse)

    def GetOrderState(self, request: 'GetOrderStateRequest') ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response, call = self._stub.GetOrderState.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, OrderState)

    def GetOrders(self, request: 'GetOrdersRequest') ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response, call = self._stub.GetOrders.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetOrdersResponse)

    def ReplaceOrder(self, request: 'ReplaceOrderRequest'
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response, call = self._stub.ReplaceOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PostOrderResponse)

    def GetMaxLots(self, request: 'GetMaxLotsRequest') ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response, call = self._stub.GetMaxLots.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetMaxLotsResponse)

    def GetOrderPrice(self, request: 'GetOrderPriceRequest'
        ) ->'GetOrderPriceResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderPriceRequest())
        response, call = self._stub.GetOrderPrice.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetOrderPriceResponse)


@dataclass
class TradesStreamRequest:
    accounts: List[str]


@dataclass
class TradesStreamResponse:
    order_trades: Optional['OrderTrades'] = None
    ping: Optional['Ping'] = None
    subscription: Optional['SubscriptionResponse'] = None


@dataclass
class OrderTrades:
    order_id: str
    created_at: datetime
    direction: 'OrderDirection'
    figi: str
    trades: List['OrderTrade']
    account_id: str
    instrument_uid: str


@dataclass
class OrderTrade:
    date_time: datetime
    price: 'Quotation'
    quantity: int
    trade_id: str


@dataclass
class PostOrderRequest:
    quantity: int
    direction: 'OrderDirection'
    account_id: str
    order_type: 'OrderType'
    order_id: str
    instrument_id: str
    time_in_force: 'TimeInForceType'
    price_type: 'PriceType'
    figi: Optional[str] = None
    price: Optional['Quotation'] = None


@dataclass
class PostOrderResponse:
    order_id: str
    execution_report_status: 'OrderExecutionReportStatus'
    lots_requested: int
    lots_executed: int
    initial_order_price: 'MoneyValue'
    executed_order_price: 'MoneyValue'
    total_order_amount: 'MoneyValue'
    initial_commission: 'MoneyValue'
    executed_commission: 'MoneyValue'
    aci_value: 'MoneyValue'
    figi: str
    direction: 'OrderDirection'
    initial_security_price: 'MoneyValue'
    order_type: 'OrderType'
    message: str
    initial_order_price_pt: 'Quotation'
    instrument_uid: str
    order_request_id: str
    response_metadata: 'ResponseMetadata'


@dataclass
class PostOrderAsyncRequest:
    instrument_id: str
    quantity: int
    direction: 'OrderDirection'
    account_id: str
    order_type: 'OrderType'
    order_id: str
    price: Optional['Quotation'] = None
    time_in_force: Optional['TimeInForceType'] = None
    price_type: Optional['PriceType'] = None


@dataclass
class PostOrderAsyncResponse:
    order_request_id: str
    execution_report_status: 'OrderExecutionReportStatus'
    trade_intent_id: Optional[str] = None


@dataclass
class CancelOrderRequest:
    account_id: str
    order_id: str
    order_id_type: Optional['OrderIdType'] = None


@dataclass
class CancelOrderResponse:
    time: datetime
    response_metadata: 'ResponseMetadata'


@dataclass
class GetOrderStateRequest:
    account_id: str
    order_id: str
    price_type: 'PriceType'
    order_id_type: Optional['OrderIdType'] = None


@dataclass
class GetOrdersRequest:
    account_id: str


@dataclass
class GetOrdersResponse:
    orders: List['OrderState']


@dataclass
class OrderState:
    order_id: str
    execution_report_status: 'OrderExecutionReportStatus'
    lots_requested: int
    lots_executed: int
    initial_order_price: 'MoneyValue'
    executed_order_price: 'MoneyValue'
    total_order_amount: 'MoneyValue'
    average_position_price: 'MoneyValue'
    initial_commission: 'MoneyValue'
    executed_commission: 'MoneyValue'
    figi: str
    direction: 'OrderDirection'
    initial_security_price: 'MoneyValue'
    stages: List['OrderStage']
    service_commission: 'MoneyValue'
    currency: str
    order_type: 'OrderType'
    order_date: datetime
    instrument_uid: str
    order_request_id: str


@dataclass
class OrderStage:
    price: 'MoneyValue'
    quantity: int
    trade_id: str
    execution_time: datetime


@dataclass
class ReplaceOrderRequest:
    account_id: str
    order_id: str
    idempotency_key: str
    quantity: int
    price: Optional['Quotation'] = None
    price_type: Optional['PriceType'] = None


@dataclass
class GetMaxLotsRequest:
    account_id: str
    instrument_id: str
    price: Optional['Quotation'] = None


@dataclass
class GetMaxLotsResponse:
    currency: str
    buy_limits: 'BuyLimitsView'
    buy_margin_limits: 'BuyLimitsView'
    sell_limits: 'SellLimitsView'
    sell_margin_limits: 'SellLimitsView'


    @dataclass
    class BuyLimitsView:
        buy_money_amount: 'Quotation'
        buy_max_lots: int
        buy_max_market_lots: int


    @dataclass
    class SellLimitsView:
        sell_max_lots: int


@dataclass
class GetOrderPriceRequest:
    account_id: str
    instrument_id: str
    price: 'Quotation'
    direction: 'OrderDirection'
    quantity: int


@dataclass
class GetOrderPriceResponse:
    total_order_amount: 'MoneyValue'
    initial_order_amount: 'MoneyValue'
    lots_requested: int
    executed_commission: 'MoneyValue'
    executed_commission_rub: 'MoneyValue'
    service_commission: 'MoneyValue'
    deal_commission: 'MoneyValue'
    extra_bond: Optional['ExtraBond'] = None
    extra_future: Optional['ExtraFuture'] = None


    @dataclass
    class ExtraBond:
        aci_value: 'MoneyValue'
        nominal_conversion_rate: 'Quotation'


    @dataclass
    class ExtraFuture:
        initial_margin: 'MoneyValue'


@dataclass
class OrderStateStreamRequest:
    accounts: List[str]
    ping_delay_millis: Optional[int] = None


@dataclass
class SubscriptionResponse:
    tracking_id: str
    status: 'ResultSubscriptionStatus'
    stream_id: str
    accounts: List[str]
    error: Optional['ErrorDetail'] = None


@dataclass
class OrderStateStreamResponse:
    order_state: Optional['OrderState'] = None
    ping: Optional['Ping'] = None
    subscription: Optional['SubscriptionResponse'] = None


    @dataclass
    class OrderState:
        order_id: str
        client_code: str
        created_at: datetime
        execution_report_status: 'OrderExecutionReportStatus'
        ticker: str
        class_code: str
        lot_size: int
        direction: 'OrderDirection'
        time_in_force: 'TimeInForceType'
        order_type: 'OrderType'
        account_id: str
        initial_order_price: 'MoneyValue'
        order_price: 'MoneyValue'
        executed_order_price: 'MoneyValue'
        currency: str
        lots_requested: int
        lots_executed: int
        lots_left: int
        lots_cancelled: int
        trades: List['OrderTrade']
        completion_time: datetime
        exchange: str
        instrument_uid: str
        order_request_id: Optional[str] = None
        status_info: Optional['StatusCauseInfo'] = None
        amount: Optional['MoneyValue'] = None
        marker: Optional['MarkerType'] = None


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
