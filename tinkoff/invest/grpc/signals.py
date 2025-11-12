from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest import _grpc_helpers
from tinkoff.invest._errors import handle_aio_request_error, handle_request_error
from tinkoff.invest.grpc import signals_pb2, signals_pb2_grpc
from tinkoff.invest.grpc.common import Page, PageResponse, Quotation
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


class StrategyType(IntEnum):
    STRATEGY_TYPE_UNSPECIFIED = 0
    STRATEGY_TYPE_TECHNICAL = 1
    STRATEGY_TYPE_FUNDAMENTAL = 2


class SignalDirection(IntEnum):
    SIGNAL_DIRECTION_UNSPECIFIED = 0
    SIGNAL_DIRECTION_BUY = 1
    SIGNAL_DIRECTION_SELL = 2


class SignalState(IntEnum):
    SIGNAL_STATE_UNSPECIFIED = 0
    SIGNAL_STATE_ACTIVE = 1
    SIGNAL_STATE_CLOSED = 2
    SIGNAL_STATE_ALL = 3


@dataclass
class GetStrategiesRequest(_grpc_helpers.Message):
    strategy_id: Optional[str] = _grpc_helpers.string_field(1, optional=True)


@dataclass
class GetStrategiesResponse(_grpc_helpers.Message):
    strategies: List['Strategy'] = _grpc_helpers.message_field(1)


@dataclass
class Strategy(_grpc_helpers.Message):
    strategy_id: str = _grpc_helpers.string_field(1)
    strategy_name: str = _grpc_helpers.string_field(2)
    strategy_description: Optional[str] = _grpc_helpers.string_field(3,
        optional=True)
    strategy_url: Optional[str] = _grpc_helpers.string_field(4, optional=True)
    strategy_type: 'StrategyType' = _grpc_helpers.message_field(5)
    active_signals: int = _grpc_helpers.int32_field(6)
    total_signals: int = _grpc_helpers.int32_field(7)
    time_in_position: int = _grpc_helpers.int64_field(8)
    average_signal_yield: 'Quotation' = _grpc_helpers.message_field(9)
    average_signal_yield_year: 'Quotation' = _grpc_helpers.message_field(10)
    yield_: 'Quotation' = _grpc_helpers.message_field(11)
    yield_year: 'Quotation' = _grpc_helpers.message_field(12)


@dataclass
class GetSignalsRequest(_grpc_helpers.Message):
    signal_id: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    strategy_id: Optional[str] = _grpc_helpers.string_field(2, optional=True)
    strategy_type: Optional['StrategyType'] = _grpc_helpers.message_field(3,
        optional=True)
    instrument_uid: Optional[str] = _grpc_helpers.string_field(4, optional=True
        )
    from_: Optional[datetime] = _grpc_helpers.message_field(5, optional=True)
    to: Optional[datetime] = _grpc_helpers.message_field(6, optional=True)
    direction: Optional['SignalDirection'] = _grpc_helpers.message_field(7,
        optional=True)
    active: Optional['SignalState'] = _grpc_helpers.message_field(8,
        optional=True)
    paging: Optional['Page'] = _grpc_helpers.message_field(9, optional=True)


@dataclass
class GetSignalsResponse(_grpc_helpers.Message):
    signals: List['Signal'] = _grpc_helpers.message_field(1)
    paging: 'PageResponse' = _grpc_helpers.message_field(2)


@dataclass
class Signal(_grpc_helpers.Message):
    signal_id: str = _grpc_helpers.string_field(1)
    strategy_id: str = _grpc_helpers.string_field(2)
    strategy_name: str = _grpc_helpers.string_field(3)
    instrument_uid: str = _grpc_helpers.string_field(4)
    create_dt: datetime = _grpc_helpers.message_field(5)
    direction: 'SignalDirection' = _grpc_helpers.message_field(6)
    initial_price: 'Quotation' = _grpc_helpers.message_field(7)
    info: Optional[str] = _grpc_helpers.string_field(8, optional=True)
    name: str = _grpc_helpers.string_field(9)
    target_price: 'Quotation' = _grpc_helpers.message_field(10)
    end_dt: datetime = _grpc_helpers.message_field(11)
    probability: Optional[int] = _grpc_helpers.int32_field(12, optional=True)
    stoploss: Optional['Quotation'] = _grpc_helpers.message_field(13,
        optional=True)
    close_price: Optional['Quotation'] = _grpc_helpers.message_field(14,
        optional=True)
    close_dt: Optional[datetime] = _grpc_helpers.message_field(15, optional
        =True)


class SignalService(BaseService):
    """//Сервис для получения технических сигналов и мнений аналитиков по инструментам."""
    _protobuf = signals_pb2
    _protobuf_grpc = signals_pb2_grpc
    _protobuf_stub = _protobuf_grpc.SignalServiceStub

    @handle_request_error('GetStrategies')
    def get_strategies(self, request: 'GetStrategiesRequest'=
        GetStrategiesRequest()) ->'GetStrategiesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetStrategiesRequest())
        response, call = self._stub.GetStrategies.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetStrategies')
        return protobuf_to_dataclass(response, GetStrategiesResponse)

    @handle_request_error('GetSignals')
    def get_signals(self, request: 'GetSignalsRequest'=GetSignalsRequest()
        ) ->'GetSignalsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetSignalsRequest())
        response, call = self._stub.GetSignals.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSignals')
        return protobuf_to_dataclass(response, GetSignalsResponse)


class AsyncSignalService(BaseService):
    """//GetStrategies — стратегии"""
    _protobuf = signals_pb2
    _protobuf_grpc = signals_pb2_grpc
    _protobuf_stub = _protobuf_grpc.SignalServiceStub

    @handle_aio_request_error('GetStrategies')
    async def get_strategies(self, request: 'GetStrategiesRequest'=
        GetStrategiesRequest()) ->'GetStrategiesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetStrategiesRequest())
        response_coro = self._stub.GetStrategies(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetStrategies')
        return protobuf_to_dataclass(response, GetStrategiesResponse)

    @handle_aio_request_error('GetSignals')
    async def get_signals(self, request: 'GetSignalsRequest'=
        GetSignalsRequest()) ->'GetSignalsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetSignalsRequest())
        response_coro = self._stub.GetSignals(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSignals')
        return protobuf_to_dataclass(response, GetSignalsResponse)
