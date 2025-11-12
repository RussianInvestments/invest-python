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
from tinkoff.invest.grpc import operations_pb2, operations_pb2_grpc
from tinkoff.invest.grpc.common import (
    InstrumentType,
    MoneyValue,
    Ping,
    PingDelaySettings,
    Quotation,
)
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


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


class PortfolioSubscriptionStatus(IntEnum):
    PORTFOLIO_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    PORTFOLIO_SUBSCRIPTION_STATUS_SUCCESS = 1
    PORTFOLIO_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    PORTFOLIO_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


class PositionsAccountSubscriptionStatus(IntEnum):
    POSITIONS_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    POSITIONS_SUBSCRIPTION_STATUS_SUCCESS = 1
    POSITIONS_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    POSITIONS_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


@dataclass
class OperationsRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    from_: Optional[datetime] = _grpc_helpers.message_field(2, optional=True)
    to: Optional[datetime] = _grpc_helpers.message_field(3, optional=True)
    state: Optional['OperationState'] = _grpc_helpers.message_field(4,
        optional=True)
    figi: Optional[str] = _grpc_helpers.string_field(5, optional=True)


@dataclass
class OperationsResponse(_grpc_helpers.Message):
    operations: List['Operation'] = _grpc_helpers.message_field(1)


@dataclass
class Operation(_grpc_helpers.Message):
    id: str = _grpc_helpers.string_field(1)
    parent_operation_id: str = _grpc_helpers.string_field(2)
    currency: str = _grpc_helpers.string_field(3)
    payment: 'MoneyValue' = _grpc_helpers.message_field(4)
    price: 'MoneyValue' = _grpc_helpers.message_field(5)
    state: 'OperationState' = _grpc_helpers.message_field(6)
    quantity: int = _grpc_helpers.int64_field(7)
    quantity_rest: int = _grpc_helpers.int64_field(8)
    figi: str = _grpc_helpers.string_field(9)
    instrument_type: str = _grpc_helpers.string_field(10)
    date: datetime = _grpc_helpers.message_field(11)
    type: str = _grpc_helpers.string_field(12)
    operation_type: 'OperationType' = _grpc_helpers.message_field(13)
    trades: List['OperationTrade'] = _grpc_helpers.message_field(14)
    asset_uid: str = _grpc_helpers.string_field(16)
    position_uid: str = _grpc_helpers.string_field(17)
    instrument_uid: str = _grpc_helpers.string_field(18)
    child_operations: List['ChildOperationItem'] = _grpc_helpers.message_field(
        19)


@dataclass
class OperationTrade(_grpc_helpers.Message):
    trade_id: str = _grpc_helpers.string_field(1)
    date_time: datetime = _grpc_helpers.message_field(2)
    quantity: int = _grpc_helpers.int64_field(3)
    price: 'MoneyValue' = _grpc_helpers.message_field(4)


@dataclass
class PortfolioRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    currency: Optional['CurrencyRequest'] = _grpc_helpers.message_field(2,
        optional=True)


    class CurrencyRequest(IntEnum):
        RUB = 0
        USD = 1
        EUR = 2


@dataclass
class PortfolioResponse(_grpc_helpers.Message):
    total_amount_shares: 'MoneyValue' = _grpc_helpers.message_field(1)
    total_amount_bonds: 'MoneyValue' = _grpc_helpers.message_field(2)
    total_amount_etf: 'MoneyValue' = _grpc_helpers.message_field(3)
    total_amount_currencies: 'MoneyValue' = _grpc_helpers.message_field(4)
    total_amount_futures: 'MoneyValue' = _grpc_helpers.message_field(5)
    expected_yield: 'Quotation' = _grpc_helpers.message_field(6)
    positions: List['PortfolioPosition'] = _grpc_helpers.message_field(7)
    account_id: str = _grpc_helpers.string_field(8)
    total_amount_options: 'MoneyValue' = _grpc_helpers.message_field(9)
    total_amount_sp: 'MoneyValue' = _grpc_helpers.message_field(10)
    total_amount_portfolio: 'MoneyValue' = _grpc_helpers.message_field(11)
    virtual_positions: List['VirtualPortfolioPosition'
        ] = _grpc_helpers.message_field(12)
    daily_yield: 'MoneyValue' = _grpc_helpers.message_field(15)
    daily_yield_relative: 'Quotation' = _grpc_helpers.message_field(16)


@dataclass
class PositionsRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass
class PositionsResponse(_grpc_helpers.Message):
    money: List['MoneyValue'] = _grpc_helpers.message_field(1)
    blocked: List['MoneyValue'] = _grpc_helpers.message_field(2)
    securities: List['PositionsSecurities'] = _grpc_helpers.message_field(3)
    limits_loading_in_progress: bool = _grpc_helpers.bool_field(4)
    futures: List['PositionsFutures'] = _grpc_helpers.message_field(5)
    options: List['PositionsOptions'] = _grpc_helpers.message_field(6)
    account_id: str = _grpc_helpers.string_field(15)


@dataclass
class WithdrawLimitsRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass
class WithdrawLimitsResponse(_grpc_helpers.Message):
    money: List['MoneyValue'] = _grpc_helpers.message_field(1)
    blocked: List['MoneyValue'] = _grpc_helpers.message_field(2)
    blocked_guarantee: List['MoneyValue'] = _grpc_helpers.message_field(3)


@dataclass
class PortfolioPosition(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_type: str = _grpc_helpers.string_field(2)
    quantity: 'Quotation' = _grpc_helpers.message_field(3)
    average_position_price: 'MoneyValue' = _grpc_helpers.message_field(4)
    expected_yield: 'Quotation' = _grpc_helpers.message_field(5)
    current_nkd: 'MoneyValue' = _grpc_helpers.message_field(6)
    average_position_price_pt: 'Quotation' = _grpc_helpers.message_field(7)
    current_price: 'MoneyValue' = _grpc_helpers.message_field(8)
    average_position_price_fifo: 'MoneyValue' = _grpc_helpers.message_field(9)
    quantity_lots: 'Quotation' = _grpc_helpers.message_field(10)
    blocked: bool = _grpc_helpers.bool_field(21)
    blocked_lots: 'Quotation' = _grpc_helpers.message_field(22)
    position_uid: str = _grpc_helpers.string_field(24)
    instrument_uid: str = _grpc_helpers.string_field(25)
    var_margin: 'MoneyValue' = _grpc_helpers.message_field(26)
    expected_yield_fifo: 'Quotation' = _grpc_helpers.message_field(27)
    daily_yield: 'MoneyValue' = _grpc_helpers.message_field(31)
    ticker: str = _grpc_helpers.string_field(32)


@dataclass
class VirtualPortfolioPosition(_grpc_helpers.Message):
    position_uid: str = _grpc_helpers.string_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)
    figi: str = _grpc_helpers.string_field(3)
    instrument_type: str = _grpc_helpers.string_field(4)
    quantity: 'Quotation' = _grpc_helpers.message_field(5)
    average_position_price: 'MoneyValue' = _grpc_helpers.message_field(6)
    expected_yield: 'Quotation' = _grpc_helpers.message_field(7)
    expected_yield_fifo: 'Quotation' = _grpc_helpers.message_field(8)
    expire_date: datetime = _grpc_helpers.message_field(9)
    current_price: 'MoneyValue' = _grpc_helpers.message_field(10)
    average_position_price_fifo: 'MoneyValue' = _grpc_helpers.message_field(11)
    daily_yield: 'MoneyValue' = _grpc_helpers.message_field(31)
    ticker: str = _grpc_helpers.string_field(32)


@dataclass
class PositionsSecurities(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    blocked: int = _grpc_helpers.int64_field(2)
    balance: int = _grpc_helpers.int64_field(3)
    position_uid: str = _grpc_helpers.string_field(4)
    instrument_uid: str = _grpc_helpers.string_field(5)
    ticker: str = _grpc_helpers.string_field(6)
    exchange_blocked: bool = _grpc_helpers.bool_field(11)
    instrument_type: str = _grpc_helpers.string_field(16)


@dataclass
class PositionsFutures(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    blocked: int = _grpc_helpers.int64_field(2)
    balance: int = _grpc_helpers.int64_field(3)
    position_uid: str = _grpc_helpers.string_field(4)
    instrument_uid: str = _grpc_helpers.string_field(5)
    ticker: str = _grpc_helpers.string_field(6)


@dataclass
class PositionsOptions(_grpc_helpers.Message):
    position_uid: str = _grpc_helpers.string_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)
    ticker: str = _grpc_helpers.string_field(3)
    blocked: int = _grpc_helpers.int64_field(11)
    balance: int = _grpc_helpers.int64_field(21)


@dataclass
class BrokerReportRequest(_grpc_helpers.Message):
    generate_broker_report_request: Optional['GenerateBrokerReportRequest'
        ] = _grpc_helpers.message_field(1, optional=True)
    get_broker_report_request: Optional['GetBrokerReportRequest'
        ] = _grpc_helpers.message_field(2, optional=True)


@dataclass
class BrokerReportResponse(_grpc_helpers.Message):
    generate_broker_report_response: Optional['GenerateBrokerReportResponse'
        ] = _grpc_helpers.message_field(1, optional=True)
    get_broker_report_response: Optional['GetBrokerReportResponse'
        ] = _grpc_helpers.message_field(2, optional=True)


@dataclass
class GenerateBrokerReportRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)


@dataclass
class GenerateBrokerReportResponse(_grpc_helpers.Message):
    task_id: str = _grpc_helpers.string_field(1)


@dataclass
class GetBrokerReportRequest(_grpc_helpers.Message):
    task_id: str = _grpc_helpers.string_field(1)
    page: Optional[int] = _grpc_helpers.int32_field(2, optional=True)


@dataclass
class GetBrokerReportResponse(_grpc_helpers.Message):
    broker_report: List['BrokerReport'] = _grpc_helpers.message_field(1)
    itemsCount: int = _grpc_helpers.int32_field(2)
    pagesCount: int = _grpc_helpers.int32_field(3)
    page: int = _grpc_helpers.int32_field(4)


@dataclass
class BrokerReport(_grpc_helpers.Message):
    trade_id: str = _grpc_helpers.string_field(1)
    order_id: str = _grpc_helpers.string_field(2)
    figi: str = _grpc_helpers.string_field(3)
    execute_sign: str = _grpc_helpers.string_field(4)
    trade_datetime: datetime = _grpc_helpers.message_field(5)
    exchange: str = _grpc_helpers.string_field(6)
    class_code: str = _grpc_helpers.string_field(7)
    direction: str = _grpc_helpers.string_field(8)
    name: str = _grpc_helpers.string_field(9)
    ticker: str = _grpc_helpers.string_field(10)
    price: 'MoneyValue' = _grpc_helpers.message_field(11)
    quantity: int = _grpc_helpers.int64_field(12)
    order_amount: 'MoneyValue' = _grpc_helpers.message_field(13)
    aci_value: 'Quotation' = _grpc_helpers.message_field(14)
    total_order_amount: 'MoneyValue' = _grpc_helpers.message_field(15)
    broker_commission: 'MoneyValue' = _grpc_helpers.message_field(16)
    exchange_commission: 'MoneyValue' = _grpc_helpers.message_field(17)
    exchange_clearing_commission: 'MoneyValue' = _grpc_helpers.message_field(18
        )
    repo_rate: 'Quotation' = _grpc_helpers.message_field(19)
    party: str = _grpc_helpers.string_field(20)
    clear_value_date: datetime = _grpc_helpers.message_field(21)
    sec_value_date: datetime = _grpc_helpers.message_field(22)
    broker_status: str = _grpc_helpers.string_field(23)
    separate_agreement_type: str = _grpc_helpers.string_field(24)
    separate_agreement_number: str = _grpc_helpers.string_field(25)
    separate_agreement_date: str = _grpc_helpers.string_field(26)
    delivery_type: str = _grpc_helpers.string_field(27)


@dataclass
class GetDividendsForeignIssuerRequest(_grpc_helpers.Message):
    generate_div_foreign_issuer_report: Optional[
        'GenerateDividendsForeignIssuerReportRequest'
        ] = _grpc_helpers.message_field(1, optional=True)
    get_div_foreign_issuer_report: Optional[
        'GetDividendsForeignIssuerReportRequest'
        ] = _grpc_helpers.message_field(2, optional=True)


@dataclass
class GetDividendsForeignIssuerResponse(_grpc_helpers.Message):
    generate_div_foreign_issuer_report_response: Optional[
        'GenerateDividendsForeignIssuerReportResponse'
        ] = _grpc_helpers.message_field(1, optional=True)
    div_foreign_issuer_report: Optional[
        'GetDividendsForeignIssuerReportResponse'
        ] = _grpc_helpers.message_field(2, optional=True)


@dataclass
class GenerateDividendsForeignIssuerReportRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)


@dataclass
class GetDividendsForeignIssuerReportRequest(_grpc_helpers.Message):
    task_id: str = _grpc_helpers.string_field(1)
    page: Optional[int] = _grpc_helpers.int32_field(2, optional=True)


@dataclass
class GenerateDividendsForeignIssuerReportResponse(_grpc_helpers.Message):
    task_id: str = _grpc_helpers.string_field(1)


@dataclass
class GetDividendsForeignIssuerReportResponse(_grpc_helpers.Message):
    dividends_foreign_issuer_report: List['DividendsForeignIssuerReport'
        ] = _grpc_helpers.message_field(1)
    itemsCount: int = _grpc_helpers.int32_field(2)
    pagesCount: int = _grpc_helpers.int32_field(3)
    page: int = _grpc_helpers.int32_field(4)


@dataclass
class DividendsForeignIssuerReport(_grpc_helpers.Message):
    record_date: datetime = _grpc_helpers.message_field(1)
    payment_date: datetime = _grpc_helpers.message_field(2)
    security_name: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    issuer_country: str = _grpc_helpers.string_field(5)
    quantity: int = _grpc_helpers.int64_field(6)
    dividend: 'Quotation' = _grpc_helpers.message_field(7)
    external_commission: 'Quotation' = _grpc_helpers.message_field(8)
    dividend_gross: 'Quotation' = _grpc_helpers.message_field(9)
    tax: 'Quotation' = _grpc_helpers.message_field(10)
    dividend_amount: 'Quotation' = _grpc_helpers.message_field(11)
    currency: str = _grpc_helpers.string_field(12)


@dataclass
class PortfolioStreamRequest(_grpc_helpers.Message):
    accounts: List[str] = _grpc_helpers.string_field(1)
    ping_settings: 'PingDelaySettings' = _grpc_helpers.message_field(15)


@dataclass
class PortfolioStreamResponse(_grpc_helpers.Message):
    subscriptions: Optional['PortfolioSubscriptionResult'
        ] = _grpc_helpers.message_field(1, optional=True)
    portfolio: Optional['PortfolioResponse'] = _grpc_helpers.message_field(
        2, optional=True)
    ping: Optional['Ping'] = _grpc_helpers.message_field(3, optional=True)


@dataclass
class PortfolioSubscriptionResult(_grpc_helpers.Message):
    accounts: List['AccountSubscriptionStatus'] = _grpc_helpers.message_field(1
        )
    tracking_id: str = _grpc_helpers.string_field(7)
    stream_id: str = _grpc_helpers.string_field(8)


@dataclass
class AccountSubscriptionStatus(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    subscription_status: 'PortfolioSubscriptionStatus' = (_grpc_helpers.
        message_field(6))


@dataclass
class GetOperationsByCursorRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    instrument_id: Optional[str] = _grpc_helpers.string_field(2, optional=True)
    from_: Optional[datetime] = _grpc_helpers.message_field(6, optional=True)
    to: Optional[datetime] = _grpc_helpers.message_field(7, optional=True)
    cursor: Optional[str] = _grpc_helpers.string_field(11, optional=True)
    limit: Optional[int] = _grpc_helpers.int32_field(12, optional=True)
    operation_types: List['OperationType'] = _grpc_helpers.message_field(13)
    state: Optional['OperationState'] = _grpc_helpers.message_field(14,
        optional=True)
    without_commissions: Optional[bool] = _grpc_helpers.bool_field(15,
        optional=True)
    without_trades: Optional[bool] = _grpc_helpers.bool_field(16, optional=True
        )
    without_overnights: Optional[bool] = _grpc_helpers.bool_field(17,
        optional=True)


@dataclass
class GetOperationsByCursorResponse(_grpc_helpers.Message):
    has_next: bool = _grpc_helpers.bool_field(1)
    next_cursor: str = _grpc_helpers.string_field(2)
    items: List['OperationItem'] = _grpc_helpers.message_field(6)


@dataclass
class OperationItem(_grpc_helpers.Message):
    cursor: str = _grpc_helpers.string_field(1)
    broker_account_id: str = _grpc_helpers.string_field(6)
    id: str = _grpc_helpers.string_field(16)
    parent_operation_id: str = _grpc_helpers.string_field(17)
    name: str = _grpc_helpers.string_field(18)
    date: datetime = _grpc_helpers.message_field(21)
    type: 'OperationType' = _grpc_helpers.message_field(22)
    description: str = _grpc_helpers.string_field(23)
    state: 'OperationState' = _grpc_helpers.message_field(24)
    instrument_uid: str = _grpc_helpers.string_field(31)
    figi: str = _grpc_helpers.string_field(32)
    instrument_type: str = _grpc_helpers.string_field(33)
    instrument_kind: 'InstrumentType' = _grpc_helpers.message_field(34)
    position_uid: str = _grpc_helpers.string_field(35)
    payment: 'MoneyValue' = _grpc_helpers.message_field(41)
    price: 'MoneyValue' = _grpc_helpers.message_field(42)
    commission: 'MoneyValue' = _grpc_helpers.message_field(43)
    yield_: 'MoneyValue' = _grpc_helpers.message_field(44)
    yield_relative: 'Quotation' = _grpc_helpers.message_field(45)
    accrued_int: 'MoneyValue' = _grpc_helpers.message_field(46)
    quantity: int = _grpc_helpers.int64_field(51)
    quantity_rest: int = _grpc_helpers.int64_field(52)
    quantity_done: int = _grpc_helpers.int64_field(53)
    cancel_date_time: datetime = _grpc_helpers.message_field(56)
    cancel_reason: str = _grpc_helpers.string_field(57)
    trades_info: 'OperationItemTrades' = _grpc_helpers.message_field(61)
    asset_uid: str = _grpc_helpers.string_field(64)
    child_operations: List['ChildOperationItem'] = _grpc_helpers.message_field(
        65)


@dataclass
class OperationItemTrades(_grpc_helpers.Message):
    trades: List['OperationItemTrade'] = _grpc_helpers.message_field(6)


@dataclass
class OperationItemTrade(_grpc_helpers.Message):
    num: str = _grpc_helpers.string_field(1)
    date: datetime = _grpc_helpers.message_field(6)
    quantity: int = _grpc_helpers.int64_field(11)
    price: 'MoneyValue' = _grpc_helpers.message_field(16)
    yield_: 'MoneyValue' = _grpc_helpers.message_field(21)
    yield_relative: 'Quotation' = _grpc_helpers.message_field(22)


@dataclass
class PositionsStreamRequest(_grpc_helpers.Message):
    accounts: List[str] = _grpc_helpers.string_field(1)
    with_initial_positions: bool = _grpc_helpers.bool_field(3)
    ping_settings: 'PingDelaySettings' = _grpc_helpers.message_field(15)


@dataclass
class PositionsStreamResponse(_grpc_helpers.Message):
    subscriptions: Optional['PositionsSubscriptionResult'
        ] = _grpc_helpers.message_field(1, optional=True)
    position: Optional['PositionData'] = _grpc_helpers.message_field(2,
        optional=True)
    ping: Optional['Ping'] = _grpc_helpers.message_field(3, optional=True)
    initial_positions: Optional['PositionsResponse'
        ] = _grpc_helpers.message_field(5, optional=True)


@dataclass
class PositionsSubscriptionResult(_grpc_helpers.Message):
    accounts: List['PositionsSubscriptionStatus'
        ] = _grpc_helpers.message_field(1)
    tracking_id: str = _grpc_helpers.string_field(7)
    stream_id: str = _grpc_helpers.string_field(8)


@dataclass
class PositionsSubscriptionStatus(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    subscription_status: 'PositionsAccountSubscriptionStatus' = (_grpc_helpers
        .message_field(6))


@dataclass
class PositionData(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    money: List['PositionsMoney'] = _grpc_helpers.message_field(2)
    securities: List['PositionsSecurities'] = _grpc_helpers.message_field(3)
    futures: List['PositionsFutures'] = _grpc_helpers.message_field(4)
    options: List['PositionsOptions'] = _grpc_helpers.message_field(5)
    date: datetime = _grpc_helpers.message_field(6)


@dataclass
class PositionsMoney(_grpc_helpers.Message):
    available_value: 'MoneyValue' = _grpc_helpers.message_field(1)
    blocked_value: 'MoneyValue' = _grpc_helpers.message_field(2)


@dataclass
class ChildOperationItem(_grpc_helpers.Message):
    instrument_uid: str = _grpc_helpers.string_field(1)
    payment: 'MoneyValue' = _grpc_helpers.message_field(2)


class OperationsService(BaseService):
    """/*С помощью методов сервиса можно получить:<br/><br/> **1**. Список операций по счету.<br/> **2**.
                              Портфель по счету.<br/> **3**. Позиции ценных бумаг на счете.<br/> **4**.
                              Доступный остаток для вывода средств.<br/> **5**. Различные отчеты.*/"""
    _protobuf = operations_pb2
    _protobuf_grpc = operations_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OperationsServiceStub

    @handle_request_error('GetOperations')
    def get_operations(self, request: 'OperationsRequest'=OperationsRequest()
        ) ->'OperationsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OperationsRequest())
        response, call = self._stub.GetOperations.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOperations')
        return protobuf_to_dataclass(response, OperationsResponse)

    @handle_request_error('GetPortfolio')
    def get_portfolio(self, request: 'PortfolioRequest'=PortfolioRequest()
        ) ->'PortfolioResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioRequest())
        response, call = self._stub.GetPortfolio.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetPortfolio')
        return protobuf_to_dataclass(response, PortfolioResponse)

    @handle_request_error('GetPositions')
    def get_positions(self, request: 'PositionsRequest'=PositionsRequest()
        ) ->'PositionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsRequest())
        response, call = self._stub.GetPositions.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetPositions')
        return protobuf_to_dataclass(response, PositionsResponse)

    @handle_request_error('GetWithdrawLimits')
    def get_withdraw_limits(self, request: 'WithdrawLimitsRequest'=
        WithdrawLimitsRequest()) ->'WithdrawLimitsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            WithdrawLimitsRequest())
        response, call = self._stub.GetWithdrawLimits.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetWithdrawLimits')
        return protobuf_to_dataclass(response, WithdrawLimitsResponse)

    @handle_request_error('GetBrokerReport')
    def get_broker_report(self, request: 'BrokerReportRequest'=
        BrokerReportRequest()) ->'BrokerReportResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            BrokerReportRequest())
        response, call = self._stub.GetBrokerReport.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBrokerReport')
        return protobuf_to_dataclass(response, BrokerReportResponse)

    @handle_request_error('GetDividendsForeignIssuer')
    def get_dividends_foreign_issuer(self, request:
        'GetDividendsForeignIssuerRequest'=GetDividendsForeignIssuerRequest()
        ) ->'GetDividendsForeignIssuerResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetDividendsForeignIssuerRequest())
        response, call = self._stub.GetDividendsForeignIssuer.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call),
            'GetDividendsForeignIssuer')
        return protobuf_to_dataclass(response,
            GetDividendsForeignIssuerResponse)

    @handle_request_error('GetOperationsByCursor')
    def get_operations_by_cursor(self, request:
        'GetOperationsByCursorRequest'=GetOperationsByCursorRequest()
        ) ->'GetOperationsByCursorResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOperationsByCursorRequest())
        response, call = self._stub.GetOperationsByCursor.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOperationsByCursor')
        return protobuf_to_dataclass(response, GetOperationsByCursorResponse)


class AsyncOperationsService(BaseService):
    """//GetOperations — список операций по счету"""
    _protobuf = operations_pb2
    _protobuf_grpc = operations_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OperationsServiceStub

    @handle_aio_request_error('GetOperations')
    async def get_operations(self, request: 'OperationsRequest'=
        OperationsRequest()) ->'OperationsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            OperationsRequest())
        response_coro = self._stub.GetOperations(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetOperations')
        return protobuf_to_dataclass(response, OperationsResponse)

    @handle_aio_request_error('GetPortfolio')
    async def get_portfolio(self, request: 'PortfolioRequest'=
        PortfolioRequest()) ->'PortfolioResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioRequest())
        response_coro = self._stub.GetPortfolio(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetPortfolio')
        return protobuf_to_dataclass(response, PortfolioResponse)

    @handle_aio_request_error('GetPositions')
    async def get_positions(self, request: 'PositionsRequest'=
        PositionsRequest()) ->'PositionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsRequest())
        response_coro = self._stub.GetPositions(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetPositions')
        return protobuf_to_dataclass(response, PositionsResponse)

    @handle_aio_request_error('GetWithdrawLimits')
    async def get_withdraw_limits(self, request: 'WithdrawLimitsRequest'=
        WithdrawLimitsRequest()) ->'WithdrawLimitsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            WithdrawLimitsRequest())
        response_coro = self._stub.GetWithdrawLimits(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetWithdrawLimits')
        return protobuf_to_dataclass(response, WithdrawLimitsResponse)

    @handle_aio_request_error('GetBrokerReport')
    async def get_broker_report(self, request: 'BrokerReportRequest'=
        BrokerReportRequest()) ->'BrokerReportResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            BrokerReportRequest())
        response_coro = self._stub.GetBrokerReport(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetBrokerReport')
        return protobuf_to_dataclass(response, BrokerReportResponse)

    @handle_aio_request_error('GetDividendsForeignIssuer')
    async def get_dividends_foreign_issuer(self, request:
        'GetDividendsForeignIssuerRequest'=GetDividendsForeignIssuerRequest()
        ) ->'GetDividendsForeignIssuerResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetDividendsForeignIssuerRequest())
        response_coro = self._stub.GetDividendsForeignIssuer(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetDividendsForeignIssuer')
        return protobuf_to_dataclass(response,
            GetDividendsForeignIssuerResponse)

    @handle_aio_request_error('GetOperationsByCursor')
    async def get_operations_by_cursor(self, request:
        'GetOperationsByCursorRequest'=GetOperationsByCursorRequest()
        ) ->'GetOperationsByCursorResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOperationsByCursorRequest())
        response_coro = self._stub.GetOperationsByCursor(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetOperationsByCursor')
        return protobuf_to_dataclass(response, GetOperationsByCursorResponse)


class OperationsStreamService(BaseService):
    """//PortfolioStream — стрим обновлений портфеля"""
    _protobuf = operations_pb2
    _protobuf_grpc = operations_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OperationsStreamServiceStub

    @handle_request_error_gen('PortfolioStream')
    def portfolio_stream(self, request: 'PortfolioStreamRequest'=
        PortfolioStreamRequest()) ->Iterable['PortfolioStreamResponse']:
        for response in self._stub.PortfolioStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            PortfolioStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, PortfolioStreamResponse)

    @handle_request_error_gen('PositionsStream')
    def positions_stream(self, request: 'PositionsStreamRequest'=
        PositionsStreamRequest()) ->Iterable['PositionsStreamResponse']:
        for response in self._stub.PositionsStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            PositionsStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, PositionsStreamResponse)


class AsyncOperationsStreamService(BaseService):
    _protobuf = operations_pb2
    _protobuf_grpc = operations_pb2_grpc
    _protobuf_stub = _protobuf_grpc.OperationsStreamServiceStub

    @handle_aio_request_error_gen('PortfolioStream')
    async def portfolio_stream(self, request: 'PortfolioStreamRequest'=
        PortfolioStreamRequest()) ->AsyncIterable['PortfolioStreamResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PortfolioStreamRequest())
        async for response in self._stub.PortfolioStream(request=
            protobuf_request, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, PortfolioStreamResponse))

    @handle_aio_request_error_gen('PositionsStream')
    async def positions_stream(self, request: 'PositionsStreamRequest'=
        PositionsStreamRequest()) ->AsyncIterable['PositionsStreamResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            PositionsStreamRequest())
        async for response in self._stub.PositionsStream(request=
            protobuf_request, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, PositionsStreamResponse))
