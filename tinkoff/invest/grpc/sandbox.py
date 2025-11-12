from dataclasses import dataclass
from typing import Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest import _grpc_helpers
from tinkoff.invest._errors import handle_aio_request_error, handle_request_error
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
    PostOrderAsyncRequest,
    PostOrderAsyncResponse,
    PostOrderRequest,
    PostOrderResponse,
    ReplaceOrderRequest,
)
from tinkoff.invest.grpc.users import GetAccountsRequest, GetAccountsResponse
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


@dataclass
class OpenSandboxAccountRequest(_grpc_helpers.Message):
    name: Optional[str] = _grpc_helpers.string_field(1, optional=True)


@dataclass
class OpenSandboxAccountResponse(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass
class CloseSandboxAccountRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass
class CloseSandboxAccountResponse(_grpc_helpers.Message):
    pass


@dataclass
class SandboxPayInRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    amount: 'MoneyValue' = _grpc_helpers.message_field(2)


@dataclass
class SandboxPayInResponse(_grpc_helpers.Message):
    balance: 'MoneyValue' = _grpc_helpers.message_field(1)


class SandboxService(BaseService):
    """// Методы для работы с песочницей T-Invest API"""
    _protobuf = sandbox_pb2
    _protobuf_grpc = sandbox_pb2_grpc
    _protobuf_stub = _protobuf_grpc.SandboxServiceStub

    @handle_request_error('OpenSandboxAccount')
    def open_sandbox_account(self, request: 'OpenSandboxAccountRequest'=
        OpenSandboxAccountRequest()) ->'OpenSandboxAccountResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OpenSandboxAccountRequest())
        response, call = self._stub.OpenSandboxAccount.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'OpenSandboxAccount')
        return protobuf_to_dataclass(response, OpenSandboxAccountResponse)

    @handle_request_error('GetSandboxAccounts')
    def get_sandbox_accounts(self, request: 'GetAccountsRequest'=
        GetAccountsRequest()) ->'GetAccountsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response, call = self._stub.GetSandboxAccounts.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxAccounts')
        return protobuf_to_dataclass(response, GetAccountsResponse)

    @handle_request_error('CloseSandboxAccount')
    def close_sandbox_account(self, request: 'CloseSandboxAccountRequest'=
        CloseSandboxAccountRequest()) ->'CloseSandboxAccountResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CloseSandboxAccountRequest())
        response, call = self._stub.CloseSandboxAccount.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CloseSandboxAccount')
        return protobuf_to_dataclass(response, CloseSandboxAccountResponse)

    @handle_request_error('PostSandboxOrder')
    def post_sandbox_order(self, request: 'PostOrderRequest'=PostOrderRequest()
        ) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response, call = self._stub.PostSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostSandboxOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_request_error('PostSandboxOrderAsync')
    def post_sandbox_order_async(self, request: 'PostOrderAsyncRequest'=
        PostOrderAsyncRequest()) ->'PostOrderAsyncResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderAsyncRequest())
        response, call = self._stub.PostSandboxOrderAsync.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'PostSandboxOrderAsync')
        return protobuf_to_dataclass(response, PostOrderAsyncResponse)

    @handle_request_error('ReplaceSandboxOrder')
    def replace_sandbox_order(self, request: 'ReplaceOrderRequest'=
        ReplaceOrderRequest()) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response, call = self._stub.ReplaceSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'ReplaceSandboxOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_request_error('GetSandboxOrders')
    def get_sandbox_orders(self, request: 'GetOrdersRequest'=GetOrdersRequest()
        ) ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response, call = self._stub.GetSandboxOrders.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxOrders')
        return protobuf_to_dataclass(response, GetOrdersResponse)

    @handle_request_error('CancelSandboxOrder')
    def cancel_sandbox_order(self, request: 'CancelOrderRequest'=
        CancelOrderRequest()) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response, call = self._stub.CancelSandboxOrder.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CancelSandboxOrder')
        return protobuf_to_dataclass(response, CancelOrderResponse)

    @handle_request_error('GetSandboxOrderState')
    def get_sandbox_order_state(self, request: 'GetOrderStateRequest'=
        GetOrderStateRequest()) ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response, call = self._stub.GetSandboxOrderState.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxOrderState')
        return protobuf_to_dataclass(response, OrderState)

    @handle_request_error('GetSandboxPositions')
    def get_sandbox_positions(self, request: 'PositionsRequest'=
        PositionsRequest()) ->'PositionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsRequest())
        response, call = self._stub.GetSandboxPositions.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxPositions')
        return protobuf_to_dataclass(response, PositionsResponse)

    @handle_request_error('GetSandboxOperations')
    def get_sandbox_operations(self, request: 'OperationsRequest'=
        OperationsRequest()) ->'OperationsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OperationsRequest())
        response, call = self._stub.GetSandboxOperations.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxOperations')
        return protobuf_to_dataclass(response, OperationsResponse)

    @handle_request_error('GetSandboxOperationsByCursor')
    def get_sandbox_operations_by_cursor(self, request:
        'GetOperationsByCursorRequest'=GetOperationsByCursorRequest()
        ) ->'GetOperationsByCursorResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOperationsByCursorRequest())
        response, call = self._stub.GetSandboxOperationsByCursor.with_call(
            request=protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call),
            'GetSandboxOperationsByCursor')
        return protobuf_to_dataclass(response, GetOperationsByCursorResponse)

    @handle_request_error('GetSandboxPortfolio')
    def get_sandbox_portfolio(self, request: 'PortfolioRequest'=
        PortfolioRequest()) ->'PortfolioResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioRequest())
        response, call = self._stub.GetSandboxPortfolio.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxPortfolio')
        return protobuf_to_dataclass(response, PortfolioResponse)

    @handle_request_error('SandboxPayIn')
    def sandbox_pay_in(self, request: 'SandboxPayInRequest'=
        SandboxPayInRequest()) ->'SandboxPayInResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            SandboxPayInRequest())
        response, call = self._stub.SandboxPayIn.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'SandboxPayIn')
        return protobuf_to_dataclass(response, SandboxPayInResponse)

    @handle_request_error('GetSandboxWithdrawLimits')
    def get_sandbox_withdraw_limits(self, request: 'WithdrawLimitsRequest'=
        WithdrawLimitsRequest()) ->'WithdrawLimitsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            WithdrawLimitsRequest())
        response, call = self._stub.GetSandboxWithdrawLimits.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxWithdrawLimits'
            )
        return protobuf_to_dataclass(response, WithdrawLimitsResponse)

    @handle_request_error('GetSandboxMaxLots')
    def get_sandbox_max_lots(self, request: 'GetMaxLotsRequest'=
        GetMaxLotsRequest()) ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response, call = self._stub.GetSandboxMaxLots.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetSandboxMaxLots')
        return protobuf_to_dataclass(response, GetMaxLotsResponse)


class AsyncSandboxService(BaseService):
    """//OpenSandboxAccount — зарегистрировать счет"""
    _protobuf = sandbox_pb2
    _protobuf_grpc = sandbox_pb2_grpc
    _protobuf_stub = _protobuf_grpc.SandboxServiceStub

    @handle_aio_request_error('OpenSandboxAccount')
    async def open_sandbox_account(self, request:
        'OpenSandboxAccountRequest'=OpenSandboxAccountRequest()
        ) ->'OpenSandboxAccountResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OpenSandboxAccountRequest())
        response_coro = self._stub.OpenSandboxAccount(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'OpenSandboxAccount')
        return protobuf_to_dataclass(response, OpenSandboxAccountResponse)

    @handle_aio_request_error('GetSandboxAccounts')
    async def get_sandbox_accounts(self, request: 'GetAccountsRequest'=
        GetAccountsRequest()) ->'GetAccountsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccountsRequest())
        response_coro = self._stub.GetSandboxAccounts(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxAccounts')
        return protobuf_to_dataclass(response, GetAccountsResponse)

    @handle_aio_request_error('CloseSandboxAccount')
    async def close_sandbox_account(self, request:
        'CloseSandboxAccountRequest'=CloseSandboxAccountRequest()
        ) ->'CloseSandboxAccountResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CloseSandboxAccountRequest())
        response_coro = self._stub.CloseSandboxAccount(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'CloseSandboxAccount')
        return protobuf_to_dataclass(response, CloseSandboxAccountResponse)

    @handle_aio_request_error('PostSandboxOrder')
    async def post_sandbox_order(self, request: 'PostOrderRequest'=
        PostOrderRequest()) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderRequest())
        response_coro = self._stub.PostSandboxOrder(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'PostSandboxOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_aio_request_error('PostSandboxOrderAsync')
    async def post_sandbox_order_async(self, request:
        'PostOrderAsyncRequest'=PostOrderAsyncRequest()
        ) ->'PostOrderAsyncResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PostOrderAsyncRequest())
        response_coro = self._stub.PostSandboxOrderAsync(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'PostSandboxOrderAsync')
        return protobuf_to_dataclass(response, PostOrderAsyncResponse)

    @handle_aio_request_error('ReplaceSandboxOrder')
    async def replace_sandbox_order(self, request: 'ReplaceOrderRequest'=
        ReplaceOrderRequest()) ->'PostOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            ReplaceOrderRequest())
        response_coro = self._stub.ReplaceSandboxOrder(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'ReplaceSandboxOrder')
        return protobuf_to_dataclass(response, PostOrderResponse)

    @handle_aio_request_error('GetSandboxOrders')
    async def get_sandbox_orders(self, request: 'GetOrdersRequest'=
        GetOrdersRequest()) ->'GetOrdersResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrdersRequest())
        response_coro = self._stub.GetSandboxOrders(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxOrders')
        return protobuf_to_dataclass(response, GetOrdersResponse)

    @handle_aio_request_error('CancelSandboxOrder')
    async def cancel_sandbox_order(self, request: 'CancelOrderRequest'=
        CancelOrderRequest()) ->'CancelOrderResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CancelOrderRequest())
        response_coro = self._stub.CancelSandboxOrder(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'CancelSandboxOrder')
        return protobuf_to_dataclass(response, CancelOrderResponse)

    @handle_aio_request_error('GetSandboxOrderState')
    async def get_sandbox_order_state(self, request: 'GetOrderStateRequest'
        =GetOrderStateRequest()) ->'OrderState':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderStateRequest())
        response_coro = self._stub.GetSandboxOrderState(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxOrderState')
        return protobuf_to_dataclass(response, OrderState)

    @handle_aio_request_error('GetSandboxPositions')
    async def get_sandbox_positions(self, request: 'PositionsRequest'=
        PositionsRequest()) ->'PositionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsRequest())
        response_coro = self._stub.GetSandboxPositions(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxPositions')
        return protobuf_to_dataclass(response, PositionsResponse)

    @handle_aio_request_error('GetSandboxOperations')
    async def get_sandbox_operations(self, request: 'OperationsRequest'=
        OperationsRequest()) ->'OperationsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OperationsRequest())
        response_coro = self._stub.GetSandboxOperations(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxOperations')
        return protobuf_to_dataclass(response, OperationsResponse)

    @handle_aio_request_error('GetSandboxOperationsByCursor')
    async def get_sandbox_operations_by_cursor(self, request:
        'GetOperationsByCursorRequest'=GetOperationsByCursorRequest()
        ) ->'GetOperationsByCursorResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOperationsByCursorRequest())
        response_coro = self._stub.GetSandboxOperationsByCursor(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxOperationsByCursor')
        return protobuf_to_dataclass(response, GetOperationsByCursorResponse)

    @handle_aio_request_error('GetSandboxPortfolio')
    async def get_sandbox_portfolio(self, request: 'PortfolioRequest'=
        PortfolioRequest()) ->'PortfolioResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioRequest())
        response_coro = self._stub.GetSandboxPortfolio(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxPortfolio')
        return protobuf_to_dataclass(response, PortfolioResponse)

    @handle_aio_request_error('SandboxPayIn')
    async def sandbox_pay_in(self, request: 'SandboxPayInRequest'=
        SandboxPayInRequest()) ->'SandboxPayInResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            SandboxPayInRequest())
        response_coro = self._stub.SandboxPayIn(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'SandboxPayIn')
        return protobuf_to_dataclass(response, SandboxPayInResponse)

    @handle_aio_request_error('GetSandboxWithdrawLimits')
    async def get_sandbox_withdraw_limits(self, request:
        'WithdrawLimitsRequest'=WithdrawLimitsRequest()
        ) ->'WithdrawLimitsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            WithdrawLimitsRequest())
        response_coro = self._stub.GetSandboxWithdrawLimits(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxWithdrawLimits')
        return protobuf_to_dataclass(response, WithdrawLimitsResponse)

    @handle_aio_request_error('GetSandboxMaxLots')
    async def get_sandbox_max_lots(self, request: 'GetMaxLotsRequest'=
        GetMaxLotsRequest()) ->'GetMaxLotsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMaxLotsRequest())
        response_coro = self._stub.GetSandboxMaxLots(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetSandboxMaxLots')
        return protobuf_to_dataclass(response, GetMaxLotsResponse)
