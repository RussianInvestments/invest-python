from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest.grpc import stoporders_pb2, stoporders_pb2_grpc
from tinkoff.invest.grpc.common import (
    MoneyValue,
    PriceType,
    Quotation,
    ResponseMetadata,
)


class StopOrdersService(BaseService):
    """/* Сервис для работы со стоп-заявками: выставление, отмена, получение списка стоп-заявок.*/"""
    _protobuf = stoporders_pb2
    _protobuf_grpc = stoporders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.StopOrdersServiceStub

    def PostStopOrder(self, request: 'PostStopOrderRequest'
        ) ->'PostStopOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostStopOrderRequest())
        response, call = self._stub.PostStopOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PostStopOrderResponse)

    def GetStopOrders(self, request: 'GetStopOrdersRequest'
        ) ->'GetStopOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetStopOrdersRequest())
        response, call = self._stub.GetStopOrders.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetStopOrdersResponse)

    def CancelStopOrder(self, request: 'CancelStopOrderRequest'
        ) ->'CancelStopOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelStopOrderRequest())
        response, call = self._stub.CancelStopOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, CancelStopOrderResponse)


@dataclass
class PostStopOrderRequest:
    quantity: int
    direction: 'StopOrderDirection'
    account_id: str
    expiration_type: 'StopOrderExpirationType'
    stop_order_type: 'StopOrderType'
    instrument_id: str
    exchange_order_type: 'ExchangeOrderType'
    take_profit_type: 'TakeProfitType'
    trailing_data: 'TrailingData'
    price_type: 'PriceType'
    order_id: str
    figi: Optional[str] = None
    price: Optional['Quotation'] = None
    stop_price: Optional['Quotation'] = None
    expire_date: Optional[datetime] = None


    @dataclass
    class TrailingData:
        indent: 'Quotation'
        indent_type: 'TrailingValueType'
        spread: 'Quotation'
        spread_type: 'TrailingValueType'


@dataclass
class PostStopOrderResponse:
    stop_order_id: str
    order_request_id: str
    response_metadata: 'ResponseMetadata'


@dataclass
class GetStopOrdersRequest:
    account_id: str
    status: 'StopOrderStatusOption'
    from_: datetime
    to: datetime


@dataclass
class GetStopOrdersResponse:
    stop_orders: List['StopOrder']


@dataclass
class CancelStopOrderRequest:
    account_id: str
    stop_order_id: str


@dataclass
class CancelStopOrderResponse:
    time: datetime


@dataclass
class StopOrder:
    stop_order_id: str
    lots_requested: int
    figi: str
    direction: 'StopOrderDirection'
    currency: str
    order_type: 'StopOrderType'
    create_date: datetime
    activation_date_time: datetime
    expiration_time: datetime
    price: 'MoneyValue'
    stop_price: 'MoneyValue'
    instrument_uid: str
    take_profit_type: 'TakeProfitType'
    trailing_data: 'TrailingData'
    status: 'StopOrderStatusOption'
    exchange_order_type: 'ExchangeOrderType'
    exchange_order_id: Optional[str] = None


    @dataclass
    class TrailingData:
        indent: 'Quotation'
        indent_type: 'TrailingValueType'
        spread: 'Quotation'
        spread_type: 'TrailingValueType'
        status: 'TrailingStopStatus'
        price: 'Quotation'
        extr: 'Quotation'


class StopOrderDirection(IntEnum):
    STOP_ORDER_DIRECTION_UNSPECIFIED = 0
    STOP_ORDER_DIRECTION_BUY = 1
    STOP_ORDER_DIRECTION_SELL = 2


class StopOrderExpirationType(IntEnum):
    STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED = 0
    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL = 1
    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE = 2


class StopOrderType(IntEnum):
    STOP_ORDER_TYPE_UNSPECIFIED = 0
    STOP_ORDER_TYPE_TAKE_PROFIT = 1
    STOP_ORDER_TYPE_STOP_LOSS = 2
    STOP_ORDER_TYPE_STOP_LIMIT = 3


class StopOrderStatusOption(IntEnum):
    STOP_ORDER_STATUS_UNSPECIFIED = 0
    STOP_ORDER_STATUS_ALL = 1
    STOP_ORDER_STATUS_ACTIVE = 2
    STOP_ORDER_STATUS_EXECUTED = 3
    STOP_ORDER_STATUS_CANCELED = 4
    STOP_ORDER_STATUS_EXPIRED = 5


class ExchangeOrderType(IntEnum):
    EXCHANGE_ORDER_TYPE_UNSPECIFIED = 0
    EXCHANGE_ORDER_TYPE_MARKET = 1
    EXCHANGE_ORDER_TYPE_LIMIT = 2


class TakeProfitType(IntEnum):
    TAKE_PROFIT_TYPE_UNSPECIFIED = 0
    TAKE_PROFIT_TYPE_REGULAR = 1
    TAKE_PROFIT_TYPE_TRAILING = 2


class TrailingValueType(IntEnum):
    TRAILING_VALUE_UNSPECIFIED = 0
    TRAILING_VALUE_ABSOLUTE = 1
    TRAILING_VALUE_RELATIVE = 2


class TrailingStopStatus(IntEnum):
    TRAILING_STOP_UNSPECIFIED = 0
    TRAILING_STOP_ACTIVE = 1
    TRAILING_STOP_ACTIVATED = 2
