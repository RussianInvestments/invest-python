from dataclasses import dataclass
from typing import Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest.grpc import sandbox_pb2, sandbox_pb2_grpc
from tinkoff.invest.grpc.common import MoneyValue
from tinkoff.invest.grpc.operations import (
    GetOperationsByCursorRequest,
    GetOperationsByCursorResponse,
    OperationsRequest,
    OperationsResponse,
    PortfolioRequest,
    PortfolioResponse,
    PositionsRequest,
    PositionsResponse,
    WithdrawLimitsRequest,
    WithdrawLimitsResponse,
)
from tinkoff.invest.grpc.orders import (
    CancelOrderRequest,
    CancelOrderResponse,
    GetMaxLotsRequest,
    GetMaxLotsResponse,
    GetOrdersRequest,
    GetOrdersResponse,
    GetOrderStateRequest,
    OrderState,
    PostOrderRequest,
    PostOrderResponse,
    ReplaceOrderRequest,
)
from tinkoff.invest.grpc.users import GetAccountsRequest, GetAccountsResponse


class SandboxService(BaseService):
    """// Методы для работы с песочницей T-Invest API"""
    _protobuf = sandbox_pb2
    _protobuf_grpc = sandbox_pb2_grpc
    _protobuf_stub = _protobuf_grpc.SandboxServiceStub

    def OpenSandboxAccount(self, request: 'OpenSandboxAccountRequest'
        ) ->'OpenSandboxAccountResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OpenSandboxAccountRequest())
        response, call = self._stub.OpenSandboxAccount.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, OpenSandboxAccountResponse)

    def GetSandboxAccounts(self, request: 'GetAccountsRequest'
        ) ->'GetAccountsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetSandboxAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccountsResponse)

    def CloseSandboxAccount(self, request: 'CloseSandboxAccountRequest'
        ) ->'CloseSandboxAccountResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CloseSandboxAccountRequest())
        response, call = self._stub.CloseSandboxAccount.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, CloseSandboxAccountResponse)

    def PostSandboxOrder(self, request: 'PostOrderRequest'
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response, call = self._stub.PostSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PostOrderResponse)

    def ReplaceSandboxOrder(self, request: 'ReplaceOrderRequest'
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response, call = self._stub.ReplaceSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PostOrderResponse)

    def GetSandboxOrders(self, request: 'GetOrdersRequest'
        ) ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response, call = self._stub.GetSandboxOrders.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetOrdersResponse)

    def CancelSandboxOrder(self, request: 'CancelOrderRequest'
        ) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response, call = self._stub.CancelSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, CancelOrderResponse)

    def GetSandboxOrderState(self, request: 'GetOrderStateRequest'
        ) ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response, call = self._stub.GetSandboxOrderState.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, OrderState)

    def GetSandboxPositions(self, request: 'PositionsRequest'
        ) ->'PositionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsRequest())
        response, call = self._stub.GetSandboxPositions.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PositionsResponse)

    def GetSandboxOperations(self, request: 'OperationsRequest'
        ) ->'OperationsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OperationsRequest())
        response, call = self._stub.GetSandboxOperations.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, OperationsResponse)

    def GetSandboxOperationsByCursor(self, request:
        'GetOperationsByCursorRequest') ->'GetOperationsByCursorResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOperationsByCursorRequest())
        response, call = self._stub.GetSandboxOperationsByCursor.with_call(
            request=protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetOperationsByCursorResponse)

    def GetSandboxPortfolio(self, request: 'PortfolioRequest'
        ) ->'PortfolioResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioRequest())
        response, call = self._stub.GetSandboxPortfolio.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PortfolioResponse)

    def SandboxPayIn(self, request: 'SandboxPayInRequest'
        ) ->'SandboxPayInResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            SandboxPayInRequest())
        response, call = self._stub.SandboxPayIn.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, SandboxPayInResponse)

    def GetSandboxWithdrawLimits(self, request: 'WithdrawLimitsRequest'
        ) ->'WithdrawLimitsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            WithdrawLimitsRequest())
        response, call = self._stub.GetSandboxWithdrawLimits.with_call(request
            =protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, WithdrawLimitsResponse)

    def GetSandboxMaxLots(self, request: 'GetMaxLotsRequest'
        ) ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response, call = self._stub.GetSandboxMaxLots.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetMaxLotsResponse)


@dataclass
class OpenSandboxAccountRequest:
    name: Optional[str] = None


@dataclass
class OpenSandboxAccountResponse:
    account_id: str


@dataclass
class CloseSandboxAccountRequest:
    account_id: str


@dataclass
class CloseSandboxAccountResponse:
    pass


@dataclass
class SandboxPayInRequest:
    account_id: str
    amount: 'MoneyValue'


@dataclass
class SandboxPayInResponse:
    balance: 'MoneyValue'
