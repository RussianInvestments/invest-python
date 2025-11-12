from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest import _grpc_helpers
from tinkoff.invest._errors import handle_aio_request_error, handle_request_error
from tinkoff.invest.grpc import users_pb2, users_pb2_grpc
from tinkoff.invest.grpc.common import MoneyValue, Quotation
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


class AccountType(IntEnum):
    ACCOUNT_TYPE_UNSPECIFIED = 0
    ACCOUNT_TYPE_TINKOFF = 1
    ACCOUNT_TYPE_TINKOFF_IIS = 2
    ACCOUNT_TYPE_INVEST_BOX = 3
    ACCOUNT_TYPE_INVEST_FUND = 4


class AccountStatus(IntEnum):
    ACCOUNT_STATUS_UNSPECIFIED = 0
    ACCOUNT_STATUS_NEW = 1
    ACCOUNT_STATUS_OPEN = 2
    ACCOUNT_STATUS_CLOSED = 3
    ACCOUNT_STATUS_ALL = 4


class AccessLevel(IntEnum):
    ACCOUNT_ACCESS_LEVEL_UNSPECIFIED = 0
    ACCOUNT_ACCESS_LEVEL_FULL_ACCESS = 1
    ACCOUNT_ACCESS_LEVEL_READ_ONLY = 2
    ACCOUNT_ACCESS_LEVEL_NO_ACCESS = 3


@dataclass
class GetAccountsRequest(_grpc_helpers.Message):
    status: Optional['AccountStatus'] = _grpc_helpers.message_field(1,
        optional=True)


@dataclass
class GetAccountsResponse(_grpc_helpers.Message):
    accounts: List['Account'] = _grpc_helpers.message_field(1)


@dataclass
class Account(_grpc_helpers.Message):
    id: str = _grpc_helpers.string_field(1)
    type: 'AccountType' = _grpc_helpers.message_field(2)
    name: str = _grpc_helpers.string_field(3)
    status: 'AccountStatus' = _grpc_helpers.message_field(4)
    opened_date: datetime = _grpc_helpers.message_field(5)
    closed_date: datetime = _grpc_helpers.message_field(6)
    access_level: 'AccessLevel' = _grpc_helpers.message_field(7)


@dataclass
class GetMarginAttributesRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass
class GetMarginAttributesResponse(_grpc_helpers.Message):
    liquid_portfolio: 'MoneyValue' = _grpc_helpers.message_field(1)
    starting_margin: 'MoneyValue' = _grpc_helpers.message_field(2)
    minimal_margin: 'MoneyValue' = _grpc_helpers.message_field(3)
    funds_sufficiency_level: 'Quotation' = _grpc_helpers.message_field(4)
    amount_of_missing_funds: 'MoneyValue' = _grpc_helpers.message_field(5)
    corrected_margin: 'MoneyValue' = _grpc_helpers.message_field(6)


@dataclass
class GetUserTariffRequest(_grpc_helpers.Message):
    pass


@dataclass
class GetUserTariffResponse(_grpc_helpers.Message):
    unary_limits: List['UnaryLimit'] = _grpc_helpers.message_field(1)
    stream_limits: List['StreamLimit'] = _grpc_helpers.message_field(2)


@dataclass
class UnaryLimit(_grpc_helpers.Message):
    limit_per_minute: int = _grpc_helpers.int32_field(1)
    methods: List[str] = _grpc_helpers.string_field(2)


@dataclass
class StreamLimit(_grpc_helpers.Message):
    limit: int = _grpc_helpers.int32_field(1)
    streams: List[str] = _grpc_helpers.string_field(2)
    open: int = _grpc_helpers.int32_field(3)


@dataclass
class GetInfoRequest(_grpc_helpers.Message):
    pass


@dataclass
class GetInfoResponse(_grpc_helpers.Message):
    prem_status: bool = _grpc_helpers.bool_field(1)
    qual_status: bool = _grpc_helpers.bool_field(2)
    qualified_for_work_with: List[str] = _grpc_helpers.string_field(3)
    tariff: str = _grpc_helpers.string_field(4)
    user_id: str = _grpc_helpers.string_field(9)
    risk_level_code: str = _grpc_helpers.string_field(12)


class UsersService(BaseService):
    """/*С помощью сервиса можно получить: <br/> 1.
                       список счетов пользователя; <br/> 2. маржинальные показатели по счeту.*/"""
    _protobuf = users_pb2
    _protobuf_grpc = users_pb2_grpc
    _protobuf_stub = _protobuf_grpc.UsersServiceStub

    @handle_request_error('GetAccounts')
    def get_accounts(self, request: 'GetAccountsRequest'=GetAccountsRequest()
        ) ->'GetAccountsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAccounts')
        return protobuf_to_dataclass(response, GetAccountsResponse)

    @handle_request_error('GetMarginAttributes')
    def get_margin_attributes(self, request: 'GetMarginAttributesRequest'=
        GetMarginAttributesRequest()) ->'GetMarginAttributesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMarginAttributesRequest())
        response, call = self._stub.GetMarginAttributes.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetMarginAttributes')
        return protobuf_to_dataclass(response, GetMarginAttributesResponse)

    @handle_request_error('GetUserTariff')
    def get_user_tariff(self, request: 'GetUserTariffRequest'=
        GetUserTariffRequest()) ->'GetUserTariffResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetUserTariffRequest())
        response, call = self._stub.GetUserTariff.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetUserTariff')
        return protobuf_to_dataclass(response, GetUserTariffResponse)

    @handle_request_error('GetInfo')
    def get_info(self, request: 'GetInfoRequest'=GetInfoRequest()
        ) ->'GetInfoResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetInfoRequest())
        response, call = self._stub.GetInfo.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetInfo')
        return protobuf_to_dataclass(response, GetInfoResponse)


class AsyncUsersService(BaseService):
    """//GetAccounts — счета пользователя"""
    _protobuf = users_pb2
    _protobuf_grpc = users_pb2_grpc
    _protobuf_stub = _protobuf_grpc.UsersServiceStub

    @handle_aio_request_error('GetAccounts')
    async def get_accounts(self, request: 'GetAccountsRequest'=
        GetAccountsRequest()) ->'GetAccountsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response_coro = self._stub.GetAccounts(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetAccounts')
        return protobuf_to_dataclass(response, GetAccountsResponse)

    @handle_aio_request_error('GetMarginAttributes')
    async def get_margin_attributes(self, request:
        'GetMarginAttributesRequest'=GetMarginAttributesRequest()
        ) ->'GetMarginAttributesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMarginAttributesRequest())
        response_coro = self._stub.GetMarginAttributes(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetMarginAttributes')
        return protobuf_to_dataclass(response, GetMarginAttributesResponse)

    @handle_aio_request_error('GetUserTariff')
    async def get_user_tariff(self, request: 'GetUserTariffRequest'=
        GetUserTariffRequest()) ->'GetUserTariffResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetUserTariffRequest())
        response_coro = self._stub.GetUserTariff(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetUserTariff')
        return protobuf_to_dataclass(response, GetUserTariffResponse)

    @handle_aio_request_error('GetInfo')
    async def get_info(self, request: 'GetInfoRequest'=GetInfoRequest()
        ) ->'GetInfoResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetInfoRequest())
        response_coro = self._stub.GetInfo(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'GetInfo')
        return protobuf_to_dataclass(response, GetInfoResponse)
