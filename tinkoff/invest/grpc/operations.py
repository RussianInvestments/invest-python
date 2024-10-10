from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Iterable, List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest.grpc import operations_pb2, operations_pb2_grpc
from tinkoff.invest.grpc.common import InstrumentType, MoneyValue, Ping, Quotation


class OperationsService(BaseService):
    """/*С помощью методов сервиса можно получить:</br></br> **1**. Список операций по счёту.</br> **2**.
                              Портфель по счёту.</br> **3**. Позиции ценных бумаг на счёте.</br> **4**.
                              Доступный остаток для вывода средств.</br> **5**. Различные отчёты.*/"""
    _protobuf = operations_pb2
    _protobuf_grpc = operations_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OperationsServiceStub

    def GetOperations(self, request: 'OperationsRequest'
        ) ->'OperationsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OperationsRequest())
        response, call = self._stub.GetOperations.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, OperationsResponse)

    def GetPortfolio(self, request: 'PortfolioRequest') ->'PortfolioResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioRequest())
        response, call = self._stub.GetPortfolio.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PortfolioResponse)

    def GetPositions(self, request: 'PositionsRequest') ->'PositionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsRequest())
        response, call = self._stub.GetPositions.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, PositionsResponse)

    def GetWithdrawLimits(self, request: 'WithdrawLimitsRequest'
        ) ->'WithdrawLimitsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            WithdrawLimitsRequest())
        response, call = self._stub.GetWithdrawLimits.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, WithdrawLimitsResponse)

    def GetBrokerReport(self, request: 'BrokerReportRequest'
        ) ->'BrokerReportResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            BrokerReportRequest())
        response, call = self._stub.GetBrokerReport.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, BrokerReportResponse)

    def GetDividendsForeignIssuer(self, request:
        'GetDividendsForeignIssuerRequest'
        ) ->'GetDividendsForeignIssuerResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetDividendsForeignIssuerRequest())
        response, call = self._stub.GetDividendsForeignIssuer.with_call(request
            =protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response,
            GetDividendsForeignIssuerResponse)

    def GetOperationsByCursor(self, request: 'GetOperationsByCursorRequest'
        ) ->'GetOperationsByCursorResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOperationsByCursorRequest())
        response, call = self._stub.GetOperationsByCursor.with_call(request
            =protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetOperationsByCursorResponse)


class OperationsStreamService(BaseService):
    """//Server-side stream обновлений портфеля."""
    _protobuf = operations_pb2
    _protobuf_grpc = operations_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OperationsStreamServiceStub

    def PortfolioStream(self, request: 'PortfolioStreamRequest') ->Iterable[
        'PortfolioStreamResponse']:
        for response in self._stub.PortfolioStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            PortfolioStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, PortfolioStreamResponse)

    def PositionsStream(self, request: 'PositionsStreamRequest') ->Iterable[
        'PositionsStreamResponse']:
        for response in self._stub.PositionsStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            PositionsStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, PositionsStreamResponse)


@dataclass
class OperationsRequest:
    account_id: str
    from_: Optional[datetime] = None
    to: Optional[datetime] = None
    state: Optional['OperationState'] = None
    figi: Optional[str] = None


@dataclass
class OperationsResponse:
    operations: List['Operation']


@dataclass
class Operation:
    id: str
    parent_operation_id: str
    currency: str
    payment: 'MoneyValue'
    price: 'MoneyValue'
    state: 'OperationState'
    quantity: int
    quantity_rest: int
    figi: str
    instrument_type: str
    date: datetime
    type: str
    operation_type: 'OperationType'
    trades: List['OperationTrade']
    asset_uid: str
    position_uid: str
    instrument_uid: str
    child_operations: List['ChildOperationItem']


@dataclass
class OperationTrade:
    trade_id: str
    date_time: datetime
    quantity: int
    price: 'MoneyValue'


@dataclass
class PortfolioRequest:
    account_id: str
    currency: Optional['CurrencyRequest'] = None


    class CurrencyRequest(IntEnum):
        RUB = 0
        USD = 1
        EUR = 2


@dataclass
class PortfolioResponse:
    total_amount_shares: 'MoneyValue'
    total_amount_bonds: 'MoneyValue'
    total_amount_etf: 'MoneyValue'
    total_amount_currencies: 'MoneyValue'
    total_amount_futures: 'MoneyValue'
    expected_yield: 'Quotation'
    positions: List['PortfolioPosition']
    account_id: str
    total_amount_options: 'MoneyValue'
    total_amount_sp: 'MoneyValue'
    total_amount_portfolio: 'MoneyValue'
    virtual_positions: List['VirtualPortfolioPosition']


@dataclass
class PositionsRequest:
    account_id: str


@dataclass
class PositionsResponse:
    money: List['MoneyValue']
    blocked: List['MoneyValue']
    securities: List['PositionsSecurities']
    limits_loading_in_progress: bool
    futures: List['PositionsFutures']
    options: List['PositionsOptions']


@dataclass
class WithdrawLimitsRequest:
    account_id: str


@dataclass
class WithdrawLimitsResponse:
    money: List['MoneyValue']
    blocked: List['MoneyValue']
    blocked_guarantee: List['MoneyValue']


@dataclass
class PortfolioPosition:
    figi: str
    instrument_type: str
    quantity: 'Quotation'
    average_position_price: 'MoneyValue'
    expected_yield: 'Quotation'
    current_nkd: 'MoneyValue'
    average_position_price_pt: 'Quotation'
    current_price: 'MoneyValue'
    average_position_price_fifo: 'MoneyValue'
    quantity_lots: 'Quotation'
    blocked: bool
    blocked_lots: 'Quotation'
    position_uid: str
    instrument_uid: str
    var_margin: 'MoneyValue'
    expected_yield_fifo: 'Quotation'


@dataclass
class VirtualPortfolioPosition:
    position_uid: str
    instrument_uid: str
    figi: str
    instrument_type: str
    quantity: 'Quotation'
    average_position_price: 'MoneyValue'
    expected_yield: 'Quotation'
    expected_yield_fifo: 'Quotation'
    expire_date: datetime
    current_price: 'MoneyValue'
    average_position_price_fifo: 'MoneyValue'


@dataclass
class PositionsSecurities:
    figi: str
    blocked: int
    balance: int
    position_uid: str
    instrument_uid: str
    exchange_blocked: bool
    instrument_type: str


@dataclass
class PositionsFutures:
    figi: str
    blocked: int
    balance: int
    position_uid: str
    instrument_uid: str


@dataclass
class PositionsOptions:
    position_uid: str
    instrument_uid: str
    blocked: int
    balance: int


@dataclass
class BrokerReportRequest:
    generate_broker_report_request: Optional['GenerateBrokerReportRequest'
        ] = None
    get_broker_report_request: Optional['GetBrokerReportRequest'] = None


@dataclass
class BrokerReportResponse:
    generate_broker_report_response: Optional['GenerateBrokerReportResponse'
        ] = None
    get_broker_report_response: Optional['GetBrokerReportResponse'] = None


@dataclass
class GenerateBrokerReportRequest:
    account_id: str
    from_: datetime
    to: datetime


@dataclass
class GenerateBrokerReportResponse:
    task_id: str


@dataclass
class GetBrokerReportRequest:
    task_id: str
    page: Optional[int] = None


@dataclass
class GetBrokerReportResponse:
    broker_report: List['BrokerReport']
    itemsCount: int
    pagesCount: int
    page: int


@dataclass
class BrokerReport:
    trade_id: str
    order_id: str
    figi: str
    execute_sign: str
    trade_datetime: datetime
    exchange: str
    class_code: str
    direction: str
    name: str
    ticker: str
    price: 'MoneyValue'
    quantity: int
    order_amount: 'MoneyValue'
    aci_value: 'Quotation'
    total_order_amount: 'MoneyValue'
    broker_commission: 'MoneyValue'
    exchange_commission: 'MoneyValue'
    exchange_clearing_commission: 'MoneyValue'
    repo_rate: 'Quotation'
    party: str
    clear_value_date: datetime
    sec_value_date: datetime
    broker_status: str
    separate_agreement_type: str
    separate_agreement_number: str
    separate_agreement_date: str
    delivery_type: str


class OperationState(IntEnum):
    OPERATION_STATE_UNSPECIFIED = 0
    OPERATION_STATE_EXECUTED = 1
    OPERATION_STATE_CANCELED = 2
    OPERATION_STATE_PROGRESS = 3


class OperationType(IntEnum):
    OPERATION_TYPE_UNSPECIFIED = 0
    OPERATION_TYPE_INPUT = 1
    OPERATION_TYPE_BOND_TAX = 2
    OPERATION_TYPE_OUTPUT_SECURITIES = 3
    OPERATION_TYPE_OVERNIGHT = 4
    OPERATION_TYPE_TAX = 5
    OPERATION_TYPE_BOND_REPAYMENT_FULL = 6
    OPERATION_TYPE_SELL_CARD = 7
    OPERATION_TYPE_DIVIDEND_TAX = 8
    OPERATION_TYPE_OUTPUT = 9
    OPERATION_TYPE_BOND_REPAYMENT = 10
    OPERATION_TYPE_TAX_CORRECTION = 11
    OPERATION_TYPE_SERVICE_FEE = 12
    OPERATION_TYPE_BENEFIT_TAX = 13
    OPERATION_TYPE_MARGIN_FEE = 14
    OPERATION_TYPE_BUY = 15
    OPERATION_TYPE_BUY_CARD = 16
    OPERATION_TYPE_INPUT_SECURITIES = 17
    OPERATION_TYPE_SELL_MARGIN = 18
    OPERATION_TYPE_BROKER_FEE = 19
    OPERATION_TYPE_BUY_MARGIN = 20
    OPERATION_TYPE_DIVIDEND = 21
    OPERATION_TYPE_SELL = 22
    OPERATION_TYPE_COUPON = 23
    OPERATION_TYPE_SUCCESS_FEE = 24
    OPERATION_TYPE_DIVIDEND_TRANSFER = 25
    OPERATION_TYPE_ACCRUING_VARMARGIN = 26
    OPERATION_TYPE_WRITING_OFF_VARMARGIN = 27
    OPERATION_TYPE_DELIVERY_BUY = 28
    OPERATION_TYPE_DELIVERY_SELL = 29
    OPERATION_TYPE_TRACK_MFEE = 30
    OPERATION_TYPE_TRACK_PFEE = 31
    OPERATION_TYPE_TAX_PROGRESSIVE = 32
    OPERATION_TYPE_BOND_TAX_PROGRESSIVE = 33
    OPERATION_TYPE_DIVIDEND_TAX_PROGRESSIVE = 34
    OPERATION_TYPE_BENEFIT_TAX_PROGRESSIVE = 35
    OPERATION_TYPE_TAX_CORRECTION_PROGRESSIVE = 36
    OPERATION_TYPE_TAX_REPO_PROGRESSIVE = 37
    OPERATION_TYPE_TAX_REPO = 38
    OPERATION_TYPE_TAX_REPO_HOLD = 39
    OPERATION_TYPE_TAX_REPO_REFUND = 40
    OPERATION_TYPE_TAX_REPO_HOLD_PROGRESSIVE = 41
    OPERATION_TYPE_TAX_REPO_REFUND_PROGRESSIVE = 42
    OPERATION_TYPE_DIV_EXT = 43
    OPERATION_TYPE_TAX_CORRECTION_COUPON = 44
    OPERATION_TYPE_CASH_FEE = 45
    OPERATION_TYPE_OUT_FEE = 46
    OPERATION_TYPE_OUT_STAMP_DUTY = 47
    OPERATION_TYPE_OUTPUT_SWIFT = 50
    OPERATION_TYPE_INPUT_SWIFT = 51
    OPERATION_TYPE_OUTPUT_ACQUIRING = 53
    OPERATION_TYPE_INPUT_ACQUIRING = 54
    OPERATION_TYPE_OUTPUT_PENALTY = 55
    OPERATION_TYPE_ADVICE_FEE = 56
    OPERATION_TYPE_TRANS_IIS_BS = 57
    OPERATION_TYPE_TRANS_BS_BS = 58
    OPERATION_TYPE_OUT_MULTI = 59
    OPERATION_TYPE_INP_MULTI = 60
    OPERATION_TYPE_OVER_PLACEMENT = 61
    OPERATION_TYPE_OVER_COM = 62
    OPERATION_TYPE_OVER_INCOME = 63
    OPERATION_TYPE_OPTION_EXPIRATION = 64
    OPERATION_TYPE_FUTURE_EXPIRATION = 65


@dataclass
class GetDividendsForeignIssuerRequest:
    generate_div_foreign_issuer_report: Optional[
        'GenerateDividendsForeignIssuerReportRequest'] = None
    get_div_foreign_issuer_report: Optional[
        'GetDividendsForeignIssuerReportRequest'] = None


@dataclass
class GetDividendsForeignIssuerResponse:
    generate_div_foreign_issuer_report_response: Optional[
        'GenerateDividendsForeignIssuerReportResponse'] = None
    div_foreign_issuer_report: Optional[
        'GetDividendsForeignIssuerReportResponse'] = None


@dataclass
class GenerateDividendsForeignIssuerReportRequest:
    account_id: str
    from_: datetime
    to: datetime


@dataclass
class GetDividendsForeignIssuerReportRequest:
    task_id: str
    page: Optional[int] = None


@dataclass
class GenerateDividendsForeignIssuerReportResponse:
    task_id: str


@dataclass
class GetDividendsForeignIssuerReportResponse:
    dividends_foreign_issuer_report: List['DividendsForeignIssuerReport']
    itemsCount: int
    pagesCount: int
    page: int


@dataclass
class DividendsForeignIssuerReport:
    record_date: datetime
    payment_date: datetime
    security_name: str
    isin: str
    issuer_country: str
    quantity: int
    dividend: 'Quotation'
    external_commission: 'Quotation'
    dividend_gross: 'Quotation'
    tax: 'Quotation'
    dividend_amount: 'Quotation'
    currency: str


@dataclass
class PortfolioStreamRequest:
    accounts: List[str]


@dataclass
class PortfolioStreamResponse:
    subscriptions: Optional['PortfolioSubscriptionResult'] = None
    portfolio: Optional['PortfolioResponse'] = None
    ping: Optional['Ping'] = None


@dataclass
class PortfolioSubscriptionResult:
    accounts: List['AccountSubscriptionStatus']
    tracking_id: str
    stream_id: str


@dataclass
class AccountSubscriptionStatus:
    account_id: str
    subscription_status: 'PortfolioSubscriptionStatus'


class PortfolioSubscriptionStatus(IntEnum):
    PORTFOLIO_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    PORTFOLIO_SUBSCRIPTION_STATUS_SUCCESS = 1
    PORTFOLIO_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    PORTFOLIO_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


@dataclass
class GetOperationsByCursorRequest:
    account_id: str
    operation_types: List['OperationType']
    instrument_id: Optional[str] = None
    from_: Optional[datetime] = None
    to: Optional[datetime] = None
    cursor: Optional[str] = None
    limit: Optional[int] = None
    state: Optional['OperationState'] = None
    without_commissions: Optional[bool] = None
    without_trades: Optional[bool] = None
    without_overnights: Optional[bool] = None


@dataclass
class GetOperationsByCursorResponse:
    has_next: bool
    next_cursor: str
    items: List['OperationItem']


@dataclass
class OperationItem:
    cursor: str
    broker_account_id: str
    id: str
    parent_operation_id: str
    name: str
    date: datetime
    type: 'OperationType'
    description: str
    state: 'OperationState'
    instrument_uid: str
    figi: str
    instrument_type: str
    instrument_kind: 'InstrumentType'
    position_uid: str
    payment: 'MoneyValue'
    price: 'MoneyValue'
    commission: 'MoneyValue'
    yield_: 'MoneyValue'
    yield_relative: 'Quotation'
    accrued_int: 'MoneyValue'
    quantity: int
    quantity_rest: int
    quantity_done: int
    cancel_date_time: datetime
    cancel_reason: str
    trades_info: 'OperationItemTrades'
    asset_uid: str
    child_operations: List['ChildOperationItem']


@dataclass
class OperationItemTrades:
    trades: List['OperationItemTrade']


@dataclass
class OperationItemTrade:
    num: str
    date: datetime
    quantity: int
    price: 'MoneyValue'
    yield_: 'MoneyValue'
    yield_relative: 'Quotation'


@dataclass
class PositionsStreamRequest:
    accounts: List[str]


@dataclass
class PositionsStreamResponse:
    subscriptions: Optional['PositionsSubscriptionResult'] = None
    position: Optional['PositionData'] = None
    ping: Optional['Ping'] = None


@dataclass
class PositionsSubscriptionResult:
    accounts: List['PositionsSubscriptionStatus']
    tracking_id: str
    stream_id: str


@dataclass
class PositionsSubscriptionStatus:
    account_id: str
    subscription_status: 'PositionsAccountSubscriptionStatus'


class PositionsAccountSubscriptionStatus(IntEnum):
    POSITIONS_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    POSITIONS_SUBSCRIPTION_STATUS_SUCCESS = 1
    POSITIONS_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    POSITIONS_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


@dataclass
class PositionData:
    account_id: str
    money: List['PositionsMoney']
    securities: List['PositionsSecurities']
    futures: List['PositionsFutures']
    options: List['PositionsOptions']
    date: datetime


@dataclass
class PositionsMoney:
    available_value: 'MoneyValue'
    blocked_value: 'MoneyValue'


@dataclass
class ChildOperationItem:
    instrument_uid: str
    payment: 'MoneyValue'
