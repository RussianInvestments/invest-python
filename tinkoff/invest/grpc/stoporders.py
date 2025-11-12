from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest import _grpc_helpers
from tinkoff.invest._errors import handle_aio_request_error, handle_request_error
from tinkoff.invest.grpc import stoporders_pb2, stoporders_pb2_grpc
from tinkoff.invest.grpc.common import (
    MoneyValue,
    PriceType,
    Quotation,
    ResponseMetadata,
)
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


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


@dataclass
class PostStopOrderRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    quantity: int = _grpc_helpers.int64_field(2)
    price: Optional['Quotation'] = _grpc_helpers.message_field(3, optional=True
        )
    stop_price: Optional['Quotation'] = _grpc_helpers.message_field(4,
        optional=True)
    direction: 'StopOrderDirection' = _grpc_helpers.message_field(5)
    account_id: str = _grpc_helpers.string_field(6)
    expiration_type: 'StopOrderExpirationType' = _grpc_helpers.message_field(7)
    stop_order_type: 'StopOrderType' = _grpc_helpers.message_field(8)
    expire_date: Optional[datetime] = _grpc_helpers.message_field(9,
        optional=True)
    instrument_id: str = _grpc_helpers.string_field(10)
    exchange_order_type: 'ExchangeOrderType' = _grpc_helpers.message_field(11)
    take_profit_type: 'TakeProfitType' = _grpc_helpers.message_field(12)
    trailing_data: 'TrailingData' = _grpc_helpers.message_field(13)
    price_type: 'PriceType' = _grpc_helpers.message_field(14)
    order_id: str = _grpc_helpers.string_field(15)
    confirm_margin_trade: bool = _grpc_helpers.bool_field(16)


    @dataclass
    class TrailingData(_grpc_helpers.Message):
        indent: 'Quotation' = _grpc_helpers.message_field(1)
        indent_type: 'TrailingValueType' = _grpc_helpers.message_field(2)
        spread: 'Quotation' = _grpc_helpers.message_field(3)
        spread_type: 'TrailingValueType' = _grpc_helpers.message_field(4)


@dataclass
class PostStopOrderResponse(_grpc_helpers.Message):
    stop_order_id: str = _grpc_helpers.string_field(1)
    order_request_id: str = _grpc_helpers.string_field(2)
    response_metadata: 'ResponseMetadata' = _grpc_helpers.message_field(254)


@dataclass
class GetStopOrdersRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    status: 'StopOrderStatusOption' = _grpc_helpers.message_field(2)
    from_: datetime = _grpc_helpers.message_field(3)
    to: datetime = _grpc_helpers.message_field(4)


@dataclass
class GetStopOrdersResponse(_grpc_helpers.Message):
    stop_orders: List['StopOrder'] = _grpc_helpers.message_field(1)


@dataclass
class CancelStopOrderRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    stop_order_id: str = _grpc_helpers.string_field(2)


@dataclass
class CancelStopOrderResponse(_grpc_helpers.Message):
    time: datetime = _grpc_helpers.message_field(1)


@dataclass
class StopOrder(_grpc_helpers.Message):
    stop_order_id: str = _grpc_helpers.string_field(1)
    lots_requested: int = _grpc_helpers.int64_field(2)
    figi: str = _grpc_helpers.string_field(3)
    direction: 'StopOrderDirection' = _grpc_helpers.message_field(4)
    currency: str = _grpc_helpers.string_field(5)
    order_type: 'StopOrderType' = _grpc_helpers.message_field(6)
    create_date: datetime = _grpc_helpers.message_field(7)
    activation_date_time: datetime = _grpc_helpers.message_field(8)
    expiration_time: datetime = _grpc_helpers.message_field(9)
    price: 'MoneyValue' = _grpc_helpers.message_field(10)
    stop_price: 'MoneyValue' = _grpc_helpers.message_field(11)
    instrument_uid: str = _grpc_helpers.string_field(12)
    take_profit_type: 'TakeProfitType' = _grpc_helpers.message_field(13)
    trailing_data: 'TrailingData' = _grpc_helpers.message_field(14)
    status: 'StopOrderStatusOption' = _grpc_helpers.message_field(15)
    exchange_order_type: 'ExchangeOrderType' = _grpc_helpers.message_field(16)
    exchange_order_id: Optional[str] = _grpc_helpers.string_field(17,
        optional=True)


    @dataclass
    class TrailingData(_grpc_helpers.Message):
        indent: 'Quotation' = _grpc_helpers.message_field(1)
        indent_type: 'TrailingValueType' = _grpc_helpers.message_field(2)
        spread: 'Quotation' = _grpc_helpers.message_field(3)
        spread_type: 'TrailingValueType' = _grpc_helpers.message_field(4)
        status: 'TrailingStopStatus' = _grpc_helpers.message_field(5)
        price: 'Quotation' = _grpc_helpers.message_field(7)
        extr: 'Quotation' = _grpc_helpers.message_field(8)


class StopOrdersService(BaseService):
    """/* Сервис для работы со стоп-заявками: выставление, отмена, получение списка стоп-заявок.*/"""
    _protobuf = stoporders_pb2
    _protobuf_grpc = stoporders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.StopOrdersServiceStub

    @handle_request_error('PostStopOrder')
    def post_stop_order(self, request: 'PostStopOrderRequest'=
        PostStopOrderRequest()) ->'PostStopOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostStopOrderRequest())
        response, call = self._stub.PostStopOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostStopOrder')
        return protobuf_to_dataclass(response, PostStopOrderResponse)

    @handle_request_error('GetStopOrders')
    def get_stop_orders(self, request: 'GetStopOrdersRequest'=
        GetStopOrdersRequest()) ->'GetStopOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetStopOrdersRequest())
        response, call = self._stub.GetStopOrders.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetStopOrders')
        return protobuf_to_dataclass(response, GetStopOrdersResponse)

    @handle_request_error('CancelStopOrder')
    def cancel_stop_order(self, request: 'CancelStopOrderRequest'=
        CancelStopOrderRequest()) ->'CancelStopOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelStopOrderRequest())
        response, call = self._stub.CancelStopOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CancelStopOrder')
        return protobuf_to_dataclass(response, CancelStopOrderResponse)


class AsyncStopOrdersService(BaseService):
    """//PostStopOrder — выставить стоп-заявку"""
    _protobuf = stoporders_pb2
    _protobuf_grpc = stoporders_pb2_grpc
    _protobuf_stub = _protobuf_grpc.StopOrdersServiceStub

    @handle_aio_request_error('PostStopOrder')
    async def post_stop_order(self, request: 'PostStopOrderRequest'=
        PostStopOrderRequest()) ->'PostStopOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostStopOrderRequest())
        response_coro = self._stub.PostStopOrder(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'PostStopOrder')
        return protobuf_to_dataclass(response, PostStopOrderResponse)

    @handle_aio_request_error('GetStopOrders')
    async def get_stop_orders(self, request: 'GetStopOrdersRequest'=
        GetStopOrdersRequest()) ->'GetStopOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetStopOrdersRequest())
        response_coro = self._stub.GetStopOrders(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetStopOrders')
        return protobuf_to_dataclass(response, GetStopOrdersResponse)

    @handle_aio_request_error('CancelStopOrder')
    async def cancel_stop_order(self, request: 'CancelStopOrderRequest'=
        CancelStopOrderRequest()) ->'CancelStopOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelStopOrderRequest())
        response_coro = self._stub.CancelStopOrder(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'CancelStopOrder')
        return protobuf_to_dataclass(response, CancelStopOrderResponse)
