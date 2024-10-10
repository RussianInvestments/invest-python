from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest.grpc import users_pb2, users_pb2_grpc
from tinkoff.invest.grpc.common import MoneyValue, Quotation


class UsersService(BaseService):
    """/*С помощью сервиса можно получить: </br> 1.
                       список счетов пользователя; </br> 2. маржинальные показатели по счёту.*/"""
    _protobuf = users_pb2
    _protobuf_grpc = users_pb2_grpc
    _protobuf_stub = _protobuf_grpc.UsersServiceStub

    def GetAccounts(self, request: 'GetAccountsRequest'
        ) ->'GetAccountsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def GetMarginAttributes(self, request: 'GetMarginAttributesRequest'
        ) ->'GetMarginAttributesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMarginAttributesRequest())
        response, call = self._stub.GetMarginAttributes.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetMarginAttributesResponse)

    def GetUserTariff(self, request: 'GetUserTariffRequest'
        ) ->'GetUserTariffResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetUserTariffRequest())
        response, call = self._stub.GetUserTariff.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetUserTariffResponse)

    def GetInfo(self, request: 'GetInfoRequest') ->'GetInfoResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetInfoRequest())
        response, call = self._stub.GetInfo.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetInfoResponse)


@dataclass
class GetAccountsRequest:
    status: Optional['AccountStatus'] = None


@dataclass
class GetAccountsResponse:
    accounts: List['Account']


@dataclass
class Account:
    id: str
    type: 'AccountType'
    name: str
    status: 'AccountStatus'
    opened_date: datetime
    closed_date: datetime
    access_level: 'AccessLevel'


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


@dataclass
class GetMarginAttributesRequest:
    account_id: str


@dataclass
class GetMarginAttributesResponse:
    liquid_portfolio: 'MoneyValue'
    starting_margin: 'MoneyValue'
    minimal_margin: 'MoneyValue'
    funds_sufficiency_level: 'Quotation'
    amount_of_missing_funds: 'MoneyValue'
    corrected_margin: 'MoneyValue'


@dataclass
class GetUserTariffRequest:
    pass


@dataclass
class GetUserTariffResponse:
    unary_limits: List['UnaryLimit']
    stream_limits: List['StreamLimit']


@dataclass
class UnaryLimit:
    limit_per_minute: int
    methods: List[str]


@dataclass
class StreamLimit:
    limit: int
    streams: List[str]
    open: int


@dataclass
class GetInfoRequest:
    pass


@dataclass
class GetInfoResponse:
    prem_status: bool
    qual_status: bool
    qualified_for_work_with: List[str]
    tariff: str


class AccessLevel(IntEnum):
    ACCOUNT_ACCESS_LEVEL_UNSPECIFIED = 0
    ACCOUNT_ACCESS_LEVEL_FULL_ACCESS = 1
    ACCOUNT_ACCESS_LEVEL_READ_ONLY = 2
    ACCOUNT_ACCESS_LEVEL_NO_ACCESS = 3
