# pylint:disable=too-many-lines
# pylint:disable=too-many-instance-attributes
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, SupportsAbs

from . import _grpc_helpers


class SecurityTradingStatus(_grpc_helpers.Enum):
    SECURITY_TRADING_STATUS_UNSPECIFIED = 0
    SECURITY_TRADING_STATUS_NOT_AVAILABLE_FOR_TRADING = 1
    SECURITY_TRADING_STATUS_OPENING_PERIOD = 2
    SECURITY_TRADING_STATUS_CLOSING_PERIOD = 3
    SECURITY_TRADING_STATUS_BREAK_IN_TRADING = 4
    SECURITY_TRADING_STATUS_NORMAL_TRADING = 5
    SECURITY_TRADING_STATUS_CLOSING_AUCTION = 6
    SECURITY_TRADING_STATUS_DARK_POOL_AUCTION = 7
    SECURITY_TRADING_STATUS_DISCRETE_AUCTION = 8
    SECURITY_TRADING_STATUS_OPENING_AUCTION_PERIOD = 9
    SECURITY_TRADING_STATUS_TRADING_AT_CLOSING_AUCTION_PRICE = 10
    SECURITY_TRADING_STATUS_SESSION_ASSIGNED = 11
    SECURITY_TRADING_STATUS_SESSION_CLOSE = 12
    SECURITY_TRADING_STATUS_SESSION_OPEN = 13
    SECURITY_TRADING_STATUS_DEALER_NORMAL_TRADING = 14
    SECURITY_TRADING_STATUS_DEALER_BREAK_IN_TRADING = 15
    SECURITY_TRADING_STATUS_DEALER_NOT_AVAILABLE_FOR_TRADING = 16


class InstrumentIdType(_grpc_helpers.Enum):
    INSTRUMENT_ID_UNSPECIFIED = 0
    INSTRUMENT_ID_TYPE_FIGI = 1
    INSTRUMENT_ID_TYPE_TICKER = 2
    INSTRUMENT_ID_TYPE_UID = 3
    INSTRUMENT_ID_TYPE_POSITION_UID = 4


class InstrumentStatus(_grpc_helpers.Enum):
    INSTRUMENT_STATUS_UNSPECIFIED = 0
    INSTRUMENT_STATUS_BASE = 1
    INSTRUMENT_STATUS_ALL = 2


class ShareType(_grpc_helpers.Enum):
    SHARE_TYPE_UNSPECIFIED = 0
    SHARE_TYPE_COMMON = 1
    SHARE_TYPE_PREFERRED = 2
    SHARE_TYPE_ADR = 3
    SHARE_TYPE_GDR = 4
    SHARE_TYPE_MLP = 5
    SHARE_TYPE_NY_REG_SHRS = 6
    SHARE_TYPE_CLOSED_END_FUND = 7
    SHARE_TYPE_REIT = 8


class SubscriptionAction(_grpc_helpers.Enum):
    SUBSCRIPTION_ACTION_UNSPECIFIED = 0
    SUBSCRIPTION_ACTION_SUBSCRIBE = 1
    SUBSCRIPTION_ACTION_UNSUBSCRIBE = 2


class SubscriptionInterval(_grpc_helpers.Enum):
    SUBSCRIPTION_INTERVAL_UNSPECIFIED = 0
    SUBSCRIPTION_INTERVAL_ONE_MINUTE = 1
    SUBSCRIPTION_INTERVAL_FIVE_MINUTES = 2
    SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES = 3
    SUBSCRIPTION_INTERVAL_ONE_HOUR = 4
    SUBSCRIPTION_INTERVAL_ONE_DAY = 5
    SUBSCRIPTION_INTERVAL_2_MIN = 6
    SUBSCRIPTION_INTERVAL_3_MIN = 7
    SUBSCRIPTION_INTERVAL_10_MIN = 8
    SUBSCRIPTION_INTERVAL_30_MIN = 9
    SUBSCRIPTION_INTERVAL_2_HOUR = 10
    SUBSCRIPTION_INTERVAL_4_HOUR = 11
    SUBSCRIPTION_INTERVAL_WEEK = 12
    SUBSCRIPTION_INTERVAL_MONTH = 13


class SubscriptionStatus(_grpc_helpers.Enum):
    SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    SUBSCRIPTION_STATUS_SUCCESS = 1
    SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND = 2
    SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID = 3
    SUBSCRIPTION_STATUS_DEPTH_IS_INVALID = 4
    SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID = 5
    SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED = 6
    SUBSCRIPTION_STATUS_INTERNAL_ERROR = 7
    SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS = 8
    SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND = 9
    SUBSCRIPTION_STATUS_SOURCE_IS_INVALID = 10


class TradeDirection(_grpc_helpers.Enum):
    TRADE_DIRECTION_UNSPECIFIED = 0
    TRADE_DIRECTION_BUY = 1
    TRADE_DIRECTION_SELL = 2


class CandleInterval(_grpc_helpers.Enum):
    CANDLE_INTERVAL_UNSPECIFIED = 0
    CANDLE_INTERVAL_5_SEC = 14
    CANDLE_INTERVAL_10_SEC = 15
    CANDLE_INTERVAL_30_SEC = 16
    CANDLE_INTERVAL_1_MIN = 1
    CANDLE_INTERVAL_2_MIN = 6
    CANDLE_INTERVAL_3_MIN = 7
    CANDLE_INTERVAL_5_MIN = 2
    CANDLE_INTERVAL_10_MIN = 8
    CANDLE_INTERVAL_15_MIN = 3
    CANDLE_INTERVAL_30_MIN = 9
    CANDLE_INTERVAL_HOUR = 4
    CANDLE_INTERVAL_2_HOUR = 10
    CANDLE_INTERVAL_4_HOUR = 11
    CANDLE_INTERVAL_DAY = 5
    CANDLE_INTERVAL_WEEK = 12
    CANDLE_INTERVAL_MONTH = 13


class CandleSource(_grpc_helpers.Enum):
    CANDLE_SOURCE_UNSPECIFIED = 0
    CANDLE_SOURCE_EXCHANGE = 1
    CANDLE_SOURCE_DEALER_WEEKEND = 2
    CANDLE_SOURCE_INCLUDE_WEEKEND = 3


class OperationState(_grpc_helpers.Enum):
    OPERATION_STATE_UNSPECIFIED = 0
    OPERATION_STATE_EXECUTED = 1
    OPERATION_STATE_CANCELED = 2
    OPERATION_STATE_PROGRESS = 3


class OrderDirection(_grpc_helpers.Enum):
    ORDER_DIRECTION_UNSPECIFIED = 0
    ORDER_DIRECTION_BUY = 1
    ORDER_DIRECTION_SELL = 2


class OrderType(_grpc_helpers.Enum):
    ORDER_TYPE_UNSPECIFIED = 0
    ORDER_TYPE_LIMIT = 1
    ORDER_TYPE_MARKET = 2
    ORDER_TYPE_BESTPRICE = 3


class OrderExecutionReportStatus(_grpc_helpers.Enum):
    EXECUTION_REPORT_STATUS_UNSPECIFIED = 0
    EXECUTION_REPORT_STATUS_FILL = 1
    EXECUTION_REPORT_STATUS_REJECTED = 2
    EXECUTION_REPORT_STATUS_CANCELLED = 3
    EXECUTION_REPORT_STATUS_NEW = 4
    EXECUTION_REPORT_STATUS_PARTIALLYFILL = 5


class AccountType(_grpc_helpers.Enum):
    ACCOUNT_TYPE_UNSPECIFIED = 0
    ACCOUNT_TYPE_TINKOFF = 1
    ACCOUNT_TYPE_TINKOFF_IIS = 2
    ACCOUNT_TYPE_INVEST_BOX = 3
    ACCOUNT_TYPE_INVEST_FUND = 4


class AccountStatus(_grpc_helpers.Enum):
    ACCOUNT_STATUS_UNSPECIFIED = 0
    ACCOUNT_STATUS_NEW = 1
    ACCOUNT_STATUS_OPEN = 2
    ACCOUNT_STATUS_CLOSED = 3


class StopOrderDirection(_grpc_helpers.Enum):
    STOP_ORDER_DIRECTION_UNSPECIFIED = 0
    STOP_ORDER_DIRECTION_BUY = 1
    STOP_ORDER_DIRECTION_SELL = 2


class StopOrderExpirationType(_grpc_helpers.Enum):
    STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED = 0
    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL = 1
    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE = 2


class StopOrderType(_grpc_helpers.Enum):
    STOP_ORDER_TYPE_UNSPECIFIED = 0
    STOP_ORDER_TYPE_TAKE_PROFIT = 1
    STOP_ORDER_TYPE_STOP_LOSS = 2
    STOP_ORDER_TYPE_STOP_LIMIT = 3


class OperationType(_grpc_helpers.Enum):
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


class AccessLevel(_grpc_helpers.Enum):
    ACCOUNT_ACCESS_LEVEL_UNSPECIFIED = 0
    ACCOUNT_ACCESS_LEVEL_FULL_ACCESS = 1
    ACCOUNT_ACCESS_LEVEL_READ_ONLY = 2
    ACCOUNT_ACCESS_LEVEL_NO_ACCESS = 3


class CouponType(_grpc_helpers.Enum):
    COUPON_TYPE_UNSPECIFIED = 0
    COUPON_TYPE_CONSTANT = 1
    COUPON_TYPE_FLOATING = 2
    COUPON_TYPE_DISCOUNT = 3
    COUPON_TYPE_MORTGAGE = 4
    COUPON_TYPE_FIX = 5
    COUPON_TYPE_VARIABLE = 6
    COUPON_TYPE_OTHER = 7


class AssetType(_grpc_helpers.Enum):
    ASSET_TYPE_UNSPECIFIED = 0
    ASSET_TYPE_CURRENCY = 1
    ASSET_TYPE_COMMODITY = 2
    ASSET_TYPE_INDEX = 3
    ASSET_TYPE_SECURITY = 4


class StructuredProductType(_grpc_helpers.Enum):
    SP_TYPE_UNSPECIFIED = 0
    SP_TYPE_DELIVERABLE = 1
    SP_TYPE_NON_DELIVERABLE = 2


class EditFavoritesActionType(_grpc_helpers.Enum):
    EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED = 0
    EDIT_FAVORITES_ACTION_TYPE_ADD = 1
    EDIT_FAVORITES_ACTION_TYPE_DEL = 2


class RealExchange(_grpc_helpers.Enum):
    REAL_EXCHANGE_UNSPECIFIED = 0
    REAL_EXCHANGE_MOEX = 1
    REAL_EXCHANGE_RTS = 2
    REAL_EXCHANGE_OTC = 3
    REAL_EXCHANGE_DEALER = 4


class PortfolioSubscriptionStatus(_grpc_helpers.Enum):
    PORTFOLIO_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    PORTFOLIO_SUBSCRIPTION_STATUS_SUCCESS = 1
    PORTFOLIO_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    PORTFOLIO_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


class InstrumentType(_grpc_helpers.Enum):
    INSTRUMENT_TYPE_UNSPECIFIED = 0
    INSTRUMENT_TYPE_BOND = 1
    INSTRUMENT_TYPE_SHARE = 2
    INSTRUMENT_TYPE_CURRENCY = 3
    INSTRUMENT_TYPE_ETF = 4
    INSTRUMENT_TYPE_FUTURES = 5
    INSTRUMENT_TYPE_SP = 6
    INSTRUMENT_TYPE_OPTION = 7
    INSTRUMENT_TYPE_CLEARING_CERTIFICATE = 8
    INSTRUMENT_TYPE_INDEX = 9
    INSTRUMENT_TYPE_COMMODITY = 10


class OptionDirection(_grpc_helpers.Enum):
    OPTION_DIRECTION_UNSPECIFIED = 0
    OPTION_DIRECTION_PUT = 1
    OPTION_DIRECTION_CALL = 2


class OptionPaymentType(_grpc_helpers.Enum):
    OPTION_PAYMENT_TYPE_UNSPECIFIED = 0
    OPTION_PAYMENT_TYPE_PREMIUM = 1
    OPTION_PAYMENT_TYPE_MARGINAL = 2


class OptionStyle(_grpc_helpers.Enum):
    OPTION_STYLE_UNSPECIFIED = 0
    OPTION_STYLE_AMERICAN = 1
    OPTION_STYLE_EUROPEAN = 2


class OptionSettlementType(_grpc_helpers.Enum):
    OPTION_EXECUTION_TYPE_UNSPECIFIED = 0
    OPTION_EXECUTION_TYPE_PHYSICAL_DELIVERY = 1
    OPTION_EXECUTION_TYPE_CASH_SETTLEMENT = 2


class PositionsAccountSubscriptionStatus(_grpc_helpers.Enum):
    POSITIONS_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    POSITIONS_SUBSCRIPTION_STATUS_SUCCESS = 1
    POSITIONS_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    POSITIONS_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


class RiskLevel(_grpc_helpers.Enum):
    RISK_LEVEL_UNSPECIFIED = 0
    RISK_LEVEL_LOW = 1
    RISK_LEVEL_MODERATE = 2
    RISK_LEVEL_HIGH = 3


class StopOrderStatusOption(_grpc_helpers.Enum):
    STOP_ORDER_STATUS_UNSPECIFIED = 0
    STOP_ORDER_STATUS_ALL = 1
    STOP_ORDER_STATUS_ACTIVE = 2
    STOP_ORDER_STATUS_EXECUTED = 3
    STOP_ORDER_STATUS_CANCELED = 4
    STOP_ORDER_STATUS_EXPIRED = 5


class ExchangeOrderType(_grpc_helpers.Enum):
    EXCHANGE_ORDER_TYPE_UNSPECIFIED = 0
    EXCHANGE_ORDER_TYPE_MARKET = 1
    EXCHANGE_ORDER_TYPE_LIMIT = 2


class TakeProfitType(_grpc_helpers.Enum):
    TAKE_PROFIT_TYPE_UNSPECIFIED = 0
    TAKE_PROFIT_TYPE_REGULAR = 1
    TAKE_PROFIT_TYPE_TRAILING = 2


class TrailingValueType(_grpc_helpers.Enum):
    TRAILING_VALUE_UNSPECIFIED = 0
    TRAILING_VALUE_ABSOLUTE = 1
    TRAILING_VALUE_RELATIVE = 2


class TrailingStopStatus(_grpc_helpers.Enum):
    TRAILING_STOP_UNSPECIFIED = 0
    TRAILING_STOP_ACTIVE = 1
    TRAILING_STOP_ACTIVATED = 2


class PriceType(_grpc_helpers.Enum):
    PRICE_TYPE_UNSPECIFIED = 0
    PRICE_TYPE_POINT = 1
    PRICE_TYPE_CURRENCY = 2


class TimeInForceType(_grpc_helpers.Enum):
    TIME_IN_FORCE_UNSPECIFIED = 0
    TIME_IN_FORCE_DAY = 1
    TIME_IN_FORCE_FILL_AND_KILL = 2
    TIME_IN_FORCE_FILL_OR_KILL = 3


class OrderIdType(_grpc_helpers.Enum):
    ORDER_ID_TYPE_UNSPECIFIED = 0
    ORDER_ID_TYPE_EXCHANGE = 1
    ORDER_ID_TYPE_REQUEST = 2


class EventType(_grpc_helpers.Enum):
    EVENT_TYPE_UNSPECIFIED = 0
    EVENT_TYPE_CPN = 1
    EVENT_TYPE_CALL = 2
    EVENT_TYPE_MTY = 3
    EVENT_TYPE_CONV = 4


class AssetReportPeriodType(_grpc_helpers.Enum):
    PERIOD_TYPE_UNSPECIFIED = 0
    PERIOD_TYPE_QUARTER = 1
    PERIOD_TYPE_SEMIANNUAL = 2
    PERIOD_TYPE_ANNUAL = 3


class Recommendation(_grpc_helpers.Enum):
    RECOMMENDATION_UNSPECIFIED = 0
    RECOMMENDATION_BUY = 1
    RECOMMENDATION_HOLD = 2
    RECOMMENDATION_SELL = 3


class OrderBookType(_grpc_helpers.Enum):
    ORDERBOOK_TYPE_UNSPECIFIED = 0
    ORDERBOOK_TYPE_EXCHANGE = 1
    ORDERBOOK_TYPE_DEALER = 2
    ORDERBOOK_TYPE_ALL = 3


class BondType(_grpc_helpers.Enum):
    BOND_TYPE_UNSPECIFIED = 0
    BOND_TYPE_REPLACED = 1


class InstrumentExchangeType(_grpc_helpers.Enum):
    INSTRUMENT_EXCHANGE_UNSPECIFIED = 0
    INSTRUMENT_EXCHANGE_DEALER = 1


class TradeSourceType(_grpc_helpers.Enum):
    TRADE_SOURCE_UNSPECIFIED = 0
    TRADE_SOURCE_EXCHANGE = 1
    TRADE_SOURCE_DEALER = 2
    TRADE_SOURCE_ALL = 3


class ResultSubscriptionStatus(_grpc_helpers.Enum):
    RESULT_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    RESULT_SUBSCRIPTION_STATUS_OK = 1
    RESULT_SUBSCRIPTION_STATUS_ERROR = 13


class MarkerType(_grpc_helpers.Enum):
    MARKER_UNKNOWN = 0
    MARKER_BROKER = 1
    MARKER_CHAT = 2
    MARKER_PAPER = 3
    MARKER_MARGIN = 4
    MARKER_TKBNM = 5
    MARKER_SHORT = 6
    MARKER_SPECMM = 7
    MARKER_PO = 8


class StatusCauseInfo(_grpc_helpers.Enum):
    CAUSE_UNSPECIFIED = 0
    CAUSE_CANCELLED_BY_CLIENT = 15
    CAUSE_CANCELLED_BY_EXCHANGE = 1
    CAUSE_CANCELLED_NOT_ENOUGH_POSITION = 2
    CAUSE_CANCELLED_BY_CLIENT_BLOCK = 3
    CAUSE_REJECTED_BY_BROKER = 4
    CAUSE_REJECTED_BY_EXCHANGE = 5
    CAUSE_CANCELLED_BY_BROKER = 6


class LastPriceType(_grpc_helpers.Enum):
    LAST_PRICE_UNSPECIFIED = 0
    LAST_PRICE_EXCHANGE = 1
    LAST_PRICE_DEALER = 2


class StrategyType(_grpc_helpers.Enum):
    STRATEGY_TYPE_UNSPECIFIED = 0
    STRATEGY_TYPE_TECHNICAL = 1
    STRATEGY_TYPE_FUNDAMENTAL = 2


class SignalDirection(_grpc_helpers.Enum):
    SIGNAL_DIRECTION_UNSPECIFIED = 0
    SIGNAL_DIRECTION_BUY = 1
    SIGNAL_DIRECTION_SELL = 2


class SignalState(_grpc_helpers.Enum):
    SIGNAL_STATE_UNSPECIFIED = 0
    SIGNAL_STATE_ACTIVE = 1
    SIGNAL_STATE_CLOSED = 2
    SIGNAL_STATE_ALL = 3


@dataclass(eq=False, repr=True)
class MoneyValue(_grpc_helpers.Message):
    currency: str = _grpc_helpers.string_field(1)
    units: int = _grpc_helpers.int64_field(2)
    nano: int = _grpc_helpers.int32_field(3)


@dataclass(eq=False, repr=True)
class Quotation(_grpc_helpers.Message, SupportsAbs):
    units: int = _grpc_helpers.int64_field(1)
    nano: int = _grpc_helpers.int32_field(2)

    def __init__(self, units: int, nano: int):
        max_quotation_nano = 1_000_000_000
        self.units = units + nano // max_quotation_nano
        self.nano = nano % max_quotation_nano

    def __add__(self, other: "Quotation") -> "Quotation":
        return Quotation(
            units=self.units + other.units,
            nano=self.nano + other.nano,
        )

    def __sub__(self, other: "Quotation") -> "Quotation":
        return Quotation(
            units=self.units - other.units,
            nano=self.nano - other.nano,
        )

    def __hash__(self) -> int:
        return hash((self.units, self.nano))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quotation):
            return NotImplemented
        return self.units == other.units and self.nano == other.nano

    def __lt__(self, other: "Quotation") -> bool:
        return self.units < other.units or (
            self.units == other.units and self.nano < other.nano
        )

    def __le__(self, other: "Quotation") -> bool:
        return self.units < other.units or (
            self.units == other.units and self.nano <= other.nano
        )

    def __gt__(self, other: "Quotation") -> bool:
        return self.units > other.units or (
            self.units == other.units and self.nano > other.nano
        )

    def __ge__(self, other: "Quotation") -> bool:
        return self.units > other.units or (
            self.units == other.units and self.nano >= other.nano
        )

    def __abs__(self) -> "Quotation":
        return Quotation(units=abs(self.units), nano=abs(self.nano))


@dataclass(eq=False, repr=True)
class PingRequest(_grpc_helpers.Message):
    time: Optional[datetime] = _grpc_helpers.message_field(1, optional=True)


@dataclass(eq=False, repr=True)
class PingDelaySettings(_grpc_helpers.Message):
    ping_delay_ms: Optional[int] = _grpc_helpers.int32_field(1, optional=True)


@dataclass(eq=False, repr=True)
class Ping(_grpc_helpers.Message):
    time: datetime = _grpc_helpers.int64_field(1)
    stream_id: str = _grpc_helpers.string_field(2)
    ping_request_time: Optional[datetime] = _grpc_helpers.message_field(
        4, optional=True
    )


@dataclass(eq=False, repr=True)
class TradingSchedulesRequest(_grpc_helpers.Message):
    exchange: Optional[str] = _grpc_helpers.string_field(1)
    from_: Optional[datetime] = _grpc_helpers.message_field(2)
    to: Optional[datetime] = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class TradingSchedulesResponse(_grpc_helpers.Message):
    exchanges: List["TradingSchedule"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class TradingSchedule(_grpc_helpers.Message):
    exchange: str = _grpc_helpers.string_field(1)
    days: List["TradingDay"] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class TradingDay(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    date: datetime = _grpc_helpers.message_field(1)
    is_trading_day: bool = _grpc_helpers.bool_field(2)
    start_time: datetime = _grpc_helpers.message_field(3)
    end_time: datetime = _grpc_helpers.message_field(4)
    # reserved 5,6
    opening_auction_start_time: datetime = _grpc_helpers.message_field(7)
    closing_auction_end_time: datetime = _grpc_helpers.message_field(8)
    evening_opening_auction_start_time: datetime = _grpc_helpers.message_field(9)
    evening_start_time: datetime = _grpc_helpers.message_field(10)
    evening_end_time: datetime = _grpc_helpers.message_field(11)
    clearing_start_time: datetime = _grpc_helpers.message_field(12)
    clearing_end_time: datetime = _grpc_helpers.message_field(13)
    premarket_start_time: datetime = _grpc_helpers.message_field(14)
    premarket_end_time: datetime = _grpc_helpers.message_field(15)
    closing_auction_start_time: datetime = _grpc_helpers.message_field(16)
    opening_auction_end_time: datetime = _grpc_helpers.message_field(17)
    intervals: List["TradingInterval"] = _grpc_helpers.message_field(18)


@dataclass(eq=False, repr=True)
class InstrumentRequest(_grpc_helpers.Message):
    id_type: "InstrumentIdType" = _grpc_helpers.enum_field(1)
    class_code: Optional[str] = _grpc_helpers.string_field(2)
    id: str = _grpc_helpers.string_field(3)


@dataclass(eq=False, repr=True)
class InstrumentsRequest(_grpc_helpers.Message):
    instrument_status: Optional["InstrumentStatus"] = _grpc_helpers.enum_field(1)
    instrument_exchange: Optional["InstrumentExchangeType"] = _grpc_helpers.enum_field(
        2
    )


@dataclass(eq=False, repr=True)
class FilterOptionsRequest(_grpc_helpers.Message):
    basic_asset_uid: Optional[str] = _grpc_helpers.string_field(1)
    basic_asset_position_uid: Optional[str] = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class BondResponse(_grpc_helpers.Message):
    instrument: "Bond" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class BondsResponse(_grpc_helpers.Message):
    instruments: List["Bond"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetBondCouponsRequest(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    from_: Optional[datetime] = _grpc_helpers.message_field(2)
    to: Optional[datetime] = _grpc_helpers.message_field(3)
    instrument_id: str = _grpc_helpers.string_field(4)


@dataclass(eq=False, repr=True)
class GetBondCouponsResponse(_grpc_helpers.Message):
    events: List["Coupon"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetBondEventsRequest(_grpc_helpers.Message):
    from_: Optional[datetime] = _grpc_helpers.message_field(2)
    to: Optional[datetime] = _grpc_helpers.message_field(3)
    instrument_id: str = _grpc_helpers.string_field(4)
    type: "EventType" = _grpc_helpers.enum_field(5)


@dataclass(eq=False, repr=True)
class BondEvent(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(2)
    event_number: int = _grpc_helpers.int32_field(3)
    event_date: datetime = _grpc_helpers.message_field(4)
    event_type: "EventType" = _grpc_helpers.enum_field(5)
    event_total_vol: "Quotation" = _grpc_helpers.message_field(6)
    fix_date: datetime = _grpc_helpers.message_field(7)
    rate_date: datetime = _grpc_helpers.message_field(8)
    default_date: datetime = _grpc_helpers.message_field(9)
    real_pay_date: datetime = _grpc_helpers.message_field(10)
    pay_date: datetime = _grpc_helpers.message_field(11)
    pay_one_bond: "MoneyValue" = _grpc_helpers.message_field(12)
    money_flow_val: "MoneyValue" = _grpc_helpers.message_field(13)
    execution: str = _grpc_helpers.string_field(14)
    operation_type: str = _grpc_helpers.string_field(15)
    value: "Quotation" = _grpc_helpers.message_field(16)
    note: str = _grpc_helpers.string_field(17)
    convert_to_fin_tool_id: str = _grpc_helpers.string_field(18)
    coupon_start_date: datetime = _grpc_helpers.message_field(19)
    coupon_end_date: datetime = _grpc_helpers.message_field(20)
    coupon_period: int = _grpc_helpers.int32_field(21)
    coupon_interest_rate: "Quotation" = _grpc_helpers.message_field(22)


@dataclass(eq=False, repr=True)
class GetBondEventsResponse(_grpc_helpers.Message):
    events: List["BondEvent"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class Coupon(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    coupon_date: datetime = _grpc_helpers.message_field(2)
    coupon_number: int = _grpc_helpers.int64_field(3)
    fix_date: datetime = _grpc_helpers.message_field(4)
    pay_one_bond: "MoneyValue" = _grpc_helpers.message_field(5)
    coupon_type: "CouponType" = _grpc_helpers.enum_field(6)
    coupon_start_date: datetime = _grpc_helpers.message_field(7)
    coupon_end_date: datetime = _grpc_helpers.message_field(8)
    coupon_period: int = _grpc_helpers.int32_field(9)


@dataclass(eq=False, repr=True)
class CurrencyResponse(_grpc_helpers.Message):
    instrument: "Currency" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class CurrenciesResponse(_grpc_helpers.Message):
    instruments: List["Currency"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class EtfResponse(_grpc_helpers.Message):
    instrument: "Etf" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class EtfsResponse(_grpc_helpers.Message):
    instruments: List["Etf"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class FutureResponse(_grpc_helpers.Message):
    instrument: "Future" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class FuturesResponse(_grpc_helpers.Message):
    instruments: List["Future"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class OptionResponse(_grpc_helpers.Message):
    instrument: "Option" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class OptionsResponse(_grpc_helpers.Message):
    instruments: List["Option"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class Option(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    position_uid: str = _grpc_helpers.string_field(2)
    ticker: str = _grpc_helpers.string_field(3)
    class_code: str = _grpc_helpers.string_field(4)
    basic_asset_position_uid: str = _grpc_helpers.string_field(5)

    trading_status: "SecurityTradingStatus" = _grpc_helpers.message_field(21)
    real_exchange: "RealExchange" = _grpc_helpers.message_field(31)
    direction: "OptionDirection" = _grpc_helpers.message_field(41)
    payment_type: "OptionPaymentType" = _grpc_helpers.message_field(42)
    style: "OptionStyle" = _grpc_helpers.message_field(43)
    settlement_type: "OptionSettlementType" = _grpc_helpers.message_field(44)

    name: str = _grpc_helpers.string_field(101)
    currency: str = _grpc_helpers.string_field(111)
    settlement_currency: str = _grpc_helpers.string_field(112)
    asset_type: str = _grpc_helpers.string_field(131)
    basic_asset: str = _grpc_helpers.string_field(132)
    exchange: str = _grpc_helpers.string_field(141)
    country_of_risk: str = _grpc_helpers.string_field(151)
    country_of_risk_name: str = _grpc_helpers.string_field(152)
    sector: str = _grpc_helpers.string_field(161)
    brand: "BrandData" = _grpc_helpers.message_field(162)

    lot: int = _grpc_helpers.int32_field(201)
    basic_asset_size: "Quotation" = _grpc_helpers.message_field(211)
    klong: "Quotation" = _grpc_helpers.message_field(221)
    kshort: "Quotation" = _grpc_helpers.message_field(222)
    dlong: "Quotation" = _grpc_helpers.message_field(223)
    dshort: "Quotation" = _grpc_helpers.message_field(224)
    dlong_min: "Quotation" = _grpc_helpers.message_field(225)
    dshort_min: "Quotation" = _grpc_helpers.message_field(226)
    min_price_increment: "Quotation" = _grpc_helpers.message_field(231)
    strike_price: "MoneyValue" = _grpc_helpers.message_field(241)

    dlong_client: "Quotation" = _grpc_helpers.message_field(290)
    dshort_client: "Quotation" = _grpc_helpers.message_field(291)

    expiration_date: datetime = _grpc_helpers.message_field(301)
    first_trade_date: datetime = _grpc_helpers.message_field(311)
    last_trade_date: datetime = _grpc_helpers.message_field(312)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(321)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(322)

    short_enabled_flag: bool = _grpc_helpers.bool_field(401)
    for_iis_flag: bool = _grpc_helpers.bool_field(402)
    otc_flag: bool = _grpc_helpers.bool_field(403)
    buy_available_flag: bool = _grpc_helpers.bool_field(404)
    sell_available_flag: bool = _grpc_helpers.bool_field(405)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(406)
    weekend_flag: bool = _grpc_helpers.bool_field(407)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(408)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(409)
    required_tests: List[str] = _grpc_helpers.string_field(410)


@dataclass(eq=False, repr=True)
class ShareResponse(_grpc_helpers.Message):
    instrument: "Share" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class SharesResponse(_grpc_helpers.Message):
    instruments: List["Share"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class Bond(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: "Quotation" = _grpc_helpers.message_field(7)
    kshort: "Quotation" = _grpc_helpers.message_field(8)
    dlong: "Quotation" = _grpc_helpers.message_field(9)
    dshort: "Quotation" = _grpc_helpers.message_field(10)
    dlong_min: "Quotation" = _grpc_helpers.message_field(11)
    dshort_min: "Quotation" = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(15)
    exchange: str = _grpc_helpers.string_field(16)
    coupon_quantity_per_year: int = _grpc_helpers.int32_field(17)
    maturity_date: datetime = _grpc_helpers.message_field(18)
    nominal: "MoneyValue" = _grpc_helpers.message_field(19)
    initial_nominal: "MoneyValue" = _grpc_helpers.message_field(20)
    state_reg_date: datetime = _grpc_helpers.message_field(21)
    placement_date: datetime = _grpc_helpers.message_field(22)
    placement_price: "MoneyValue" = _grpc_helpers.message_field(23)
    aci_value: "MoneyValue" = _grpc_helpers.message_field(24)
    country_of_risk: str = _grpc_helpers.string_field(25)
    country_of_risk_name: str = _grpc_helpers.string_field(26)
    sector: str = _grpc_helpers.string_field(27)
    issue_kind: str = _grpc_helpers.string_field(28)
    issue_size: int = _grpc_helpers.int64_field(29)
    issue_size_plan: int = _grpc_helpers.int64_field(30)
    trading_status: "SecurityTradingStatus" = _grpc_helpers.enum_field(31)
    otc_flag: bool = _grpc_helpers.bool_field(32)
    buy_available_flag: bool = _grpc_helpers.bool_field(33)
    sell_available_flag: bool = _grpc_helpers.bool_field(34)
    floating_coupon_flag: bool = _grpc_helpers.bool_field(35)
    perpetual_flag: bool = _grpc_helpers.bool_field(36)
    amortization_flag: bool = _grpc_helpers.bool_field(37)
    min_price_increment: "Quotation" = _grpc_helpers.message_field(38)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(39)
    uid: str = _grpc_helpers.string_field(40)
    real_exchange: "RealExchange" = _grpc_helpers.message_field(41)
    position_uid: str = _grpc_helpers.string_field(42)
    asset_uid: str = _grpc_helpers.string_field(43)
    for_iis_flag: bool = _grpc_helpers.bool_field(51)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(52)
    weekend_flag: bool = _grpc_helpers.bool_field(53)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(54)
    subordinated_flag: bool = _grpc_helpers.bool_field(55)
    liquidity_flag: bool = _grpc_helpers.bool_field(56)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(61)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(62)
    risk_level: "RiskLevel" = _grpc_helpers.enum_field(63)
    brand: "BrandData" = _grpc_helpers.message_field(64)
    bond_type: "BondType" = _grpc_helpers.message_field(65)
    call_date: datetime = _grpc_helpers.message_field(69)
    dlong_client: "Quotation" = _grpc_helpers.message_field(90)
    dshort_client: "Quotation" = _grpc_helpers.message_field(91)
    required_tests: List[str] = _grpc_helpers.string_field(44)


@dataclass(eq=False, repr=True)
class Currency(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: "Quotation" = _grpc_helpers.message_field(7)
    kshort: "Quotation" = _grpc_helpers.message_field(8)
    dlong: "Quotation" = _grpc_helpers.message_field(9)
    dshort: "Quotation" = _grpc_helpers.message_field(10)
    dlong_min: "Quotation" = _grpc_helpers.message_field(11)
    dshort_min: "Quotation" = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(15)
    exchange: str = _grpc_helpers.string_field(16)
    nominal: "MoneyValue" = _grpc_helpers.message_field(17)
    country_of_risk: str = _grpc_helpers.string_field(18)
    country_of_risk_name: str = _grpc_helpers.string_field(19)
    trading_status: "SecurityTradingStatus" = _grpc_helpers.enum_field(20)
    otc_flag: bool = _grpc_helpers.bool_field(21)
    buy_available_flag: bool = _grpc_helpers.bool_field(22)
    sell_available_flag: bool = _grpc_helpers.bool_field(23)
    iso_currency_name: str = _grpc_helpers.string_field(24)
    min_price_increment: "Quotation" = _grpc_helpers.message_field(25)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(26)
    uid: str = _grpc_helpers.string_field(27)
    real_exchange: "RealExchange" = _grpc_helpers.message_field(28)
    position_uid: str = _grpc_helpers.string_field(29)
    required_tests: List[str] = _grpc_helpers.string_field(30)
    for_iis_flag: bool = _grpc_helpers.bool_field(41)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(52)
    weekend_flag: bool = _grpc_helpers.bool_field(53)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(54)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    brand: "BrandData" = _grpc_helpers.message_field(60)
    dlong_client: "Quotation" = _grpc_helpers.message_field(90)
    dshort_client: "Quotation" = _grpc_helpers.message_field(91)


@dataclass(eq=False, repr=True)
class Etf(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: "Quotation" = _grpc_helpers.message_field(7)
    kshort: "Quotation" = _grpc_helpers.message_field(8)
    dlong: "Quotation" = _grpc_helpers.message_field(9)
    dshort: "Quotation" = _grpc_helpers.message_field(10)
    dlong_min: "Quotation" = _grpc_helpers.message_field(11)
    dshort_min: "Quotation" = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(15)
    exchange: str = _grpc_helpers.string_field(16)
    fixed_commission: "Quotation" = _grpc_helpers.message_field(17)
    focus_type: str = _grpc_helpers.string_field(18)
    released_date: datetime = _grpc_helpers.message_field(19)
    num_shares: "Quotation" = _grpc_helpers.message_field(20)
    country_of_risk: str = _grpc_helpers.string_field(21)
    country_of_risk_name: str = _grpc_helpers.string_field(22)
    sector: str = _grpc_helpers.string_field(23)
    rebalancing_freq: str = _grpc_helpers.string_field(24)
    trading_status: "SecurityTradingStatus" = _grpc_helpers.enum_field(25)
    otc_flag: bool = _grpc_helpers.bool_field(26)
    buy_available_flag: bool = _grpc_helpers.bool_field(27)
    sell_available_flag: bool = _grpc_helpers.bool_field(28)
    min_price_increment: "Quotation" = _grpc_helpers.message_field(29)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(30)
    uid: str = _grpc_helpers.string_field(31)
    real_exchange: "RealExchange" = _grpc_helpers.message_field(32)
    position_uid: str = _grpc_helpers.string_field(33)
    asset_uid: str = _grpc_helpers.string_field(34)
    instrument_exchange: "InstrumentExchangeType" = _grpc_helpers.message_field(35)
    required_tests: List[str] = _grpc_helpers.string_field(36)
    for_iis_flag: bool = _grpc_helpers.bool_field(41)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(42)
    weekend_flag: bool = _grpc_helpers.bool_field(43)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(44)
    liquidity_flag: bool = _grpc_helpers.bool_field(45)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    brand: "BrandData" = _grpc_helpers.message_field(60)
    dlong_client: "Quotation" = _grpc_helpers.message_field(90)
    dshort_client: "Quotation" = _grpc_helpers.message_field(91)


@dataclass(eq=False, repr=True)
class Future(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    lot: int = _grpc_helpers.int32_field(4)
    currency: str = _grpc_helpers.string_field(5)
    klong: "Quotation" = _grpc_helpers.message_field(6)
    kshort: "Quotation" = _grpc_helpers.message_field(7)
    dlong: "Quotation" = _grpc_helpers.message_field(8)
    dshort: "Quotation" = _grpc_helpers.message_field(9)
    dlong_min: "Quotation" = _grpc_helpers.message_field(10)
    dshort_min: "Quotation" = _grpc_helpers.message_field(11)
    short_enabled_flag: bool = _grpc_helpers.bool_field(12)
    name: str = _grpc_helpers.string_field(13)
    exchange: str = _grpc_helpers.string_field(14)
    first_trade_date: datetime = _grpc_helpers.message_field(15)
    last_trade_date: datetime = _grpc_helpers.message_field(16)
    futures_type: str = _grpc_helpers.string_field(17)
    asset_type: str = _grpc_helpers.string_field(18)
    basic_asset: str = _grpc_helpers.string_field(19)
    basic_asset_size: "Quotation" = _grpc_helpers.message_field(20)
    country_of_risk: str = _grpc_helpers.string_field(21)
    country_of_risk_name: str = _grpc_helpers.string_field(22)
    sector: str = _grpc_helpers.string_field(23)
    expiration_date: datetime = _grpc_helpers.message_field(24)
    trading_status: "SecurityTradingStatus" = _grpc_helpers.enum_field(25)
    otc_flag: bool = _grpc_helpers.bool_field(26)
    buy_available_flag: bool = _grpc_helpers.bool_field(27)
    sell_available_flag: bool = _grpc_helpers.bool_field(28)
    min_price_increment: "Quotation" = _grpc_helpers.message_field(29)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(30)
    uid: str = _grpc_helpers.string_field(31)
    real_exchange: "RealExchange" = _grpc_helpers.message_field(32)
    position_uid: str = _grpc_helpers.string_field(33)
    basic_asset_position_uid: str = _grpc_helpers.string_field(34)
    required_tests: List[str] = _grpc_helpers.string_field(35)
    for_iis_flag: bool = _grpc_helpers.bool_field(41)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(42)
    weekend_flag: bool = _grpc_helpers.bool_field(43)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(44)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    initial_margin_on_buy: "MoneyValue" = _grpc_helpers.message_field(61)
    initial_margin_on_sell: "MoneyValue" = _grpc_helpers.message_field(62)
    min_price_increment_amount: "Quotation" = _grpc_helpers.message_field(63)
    brand: "BrandData" = _grpc_helpers.message_field(64)
    dlong_client: "Quotation" = _grpc_helpers.message_field(90)
    dshort_client: "Quotation" = _grpc_helpers.message_field(91)


@dataclass(eq=False, repr=True)
class Share(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: "Quotation" = _grpc_helpers.message_field(7)
    kshort: "Quotation" = _grpc_helpers.message_field(8)
    dlong: "Quotation" = _grpc_helpers.message_field(9)
    dshort: "Quotation" = _grpc_helpers.message_field(10)
    dlong_min: "Quotation" = _grpc_helpers.message_field(11)
    dshort_min: "Quotation" = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(15)
    exchange: str = _grpc_helpers.string_field(16)
    ipo_date: datetime = _grpc_helpers.message_field(17)
    issue_size: int = _grpc_helpers.int64_field(18)
    country_of_risk: str = _grpc_helpers.string_field(19)
    country_of_risk_name: str = _grpc_helpers.string_field(20)
    sector: str = _grpc_helpers.string_field(21)
    issue_size_plan: int = _grpc_helpers.int64_field(22)
    nominal: "MoneyValue" = _grpc_helpers.message_field(23)
    trading_status: "SecurityTradingStatus" = _grpc_helpers.enum_field(25)
    otc_flag: bool = _grpc_helpers.bool_field(26)
    buy_available_flag: bool = _grpc_helpers.bool_field(27)
    sell_available_flag: bool = _grpc_helpers.bool_field(28)
    div_yield_flag: bool = _grpc_helpers.bool_field(29)
    share_type: "ShareType" = _grpc_helpers.enum_field(30)
    min_price_increment: "Quotation" = _grpc_helpers.message_field(31)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(32)
    uid: str = _grpc_helpers.string_field(33)
    real_exchange: "RealExchange" = _grpc_helpers.message_field(34)
    position_uid: str = _grpc_helpers.string_field(35)
    asset_uid: str = _grpc_helpers.string_field(36)
    instrument_exchange: "InstrumentExchangeType" = _grpc_helpers.message_field(37)
    required_tests: List[str] = _grpc_helpers.string_field(38)
    for_iis_flag: bool = _grpc_helpers.bool_field(46)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(47)
    weekend_flag: bool = _grpc_helpers.bool_field(48)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(49)
    liquidity_flag: bool = _grpc_helpers.bool_field(50)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    brand: "BrandData" = _grpc_helpers.message_field(60)
    dlong_client: "Quotation" = _grpc_helpers.message_field(90)
    dshort_client: "Quotation" = _grpc_helpers.message_field(91)


@dataclass(eq=False, repr=True)
class GetAccruedInterestsRequest(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)
    instrument_id: str = _grpc_helpers.string_field(4)


@dataclass(eq=False, repr=True)
class GetAccruedInterestsResponse(_grpc_helpers.Message):
    accrued_interests: List["AccruedInterest"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class AccruedInterest(_grpc_helpers.Message):
    date: datetime = _grpc_helpers.message_field(1)
    value: "Quotation" = _grpc_helpers.message_field(2)
    value_percent: "Quotation" = _grpc_helpers.message_field(3)
    nominal: "Quotation" = _grpc_helpers.message_field(4)


@dataclass(eq=False, repr=True)
class GetFuturesMarginRequest(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(4)


@dataclass(eq=False, repr=True)
class GetFuturesMarginResponse(_grpc_helpers.Message):
    initial_margin_on_buy: "MoneyValue" = _grpc_helpers.message_field(1)
    initial_margin_on_sell: "MoneyValue" = _grpc_helpers.message_field(2)
    min_price_increment: "Quotation" = _grpc_helpers.message_field(3)
    min_price_increment_amount: "Quotation" = _grpc_helpers.message_field(4)


@dataclass(eq=False, repr=True)
class InstrumentResponse(_grpc_helpers.Message):
    instrument: "Instrument" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class Instrument(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: "Quotation" = _grpc_helpers.message_field(7)
    kshort: "Quotation" = _grpc_helpers.message_field(8)
    dlong: "Quotation" = _grpc_helpers.message_field(9)
    dshort: "Quotation" = _grpc_helpers.message_field(10)
    dlong_min: "Quotation" = _grpc_helpers.message_field(11)
    dshort_min: "Quotation" = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(14)
    exchange: str = _grpc_helpers.string_field(15)
    country_of_risk: str = _grpc_helpers.string_field(16)
    country_of_risk_name: str = _grpc_helpers.string_field(17)
    instrument_type: str = _grpc_helpers.string_field(18)
    trading_status: "SecurityTradingStatus" = _grpc_helpers.enum_field(19)
    otc_flag: bool = _grpc_helpers.bool_field(20)
    buy_available_flag: bool = _grpc_helpers.bool_field(21)
    sell_available_flag: bool = _grpc_helpers.bool_field(22)
    min_price_increment: "Quotation" = _grpc_helpers.message_field(23)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(24)
    uid: str = _grpc_helpers.string_field(25)
    real_exchange: "RealExchange" = _grpc_helpers.message_field(26)
    position_uid: str = _grpc_helpers.string_field(27)
    asset_uid: str = _grpc_helpers.string_field(28)
    required_tests: List[str] = _grpc_helpers.string_field(29)
    for_iis_flag: bool = _grpc_helpers.bool_field(36)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(37)
    weekend_flag: bool = _grpc_helpers.bool_field(38)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(39)
    instrument_kind: "InstrumentType" = _grpc_helpers.enum_field(40)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    brand: "BrandData" = _grpc_helpers.message_field(60)
    dlong_client: "Quotation" = _grpc_helpers.message_field(490)
    dshort_client: "Quotation" = _grpc_helpers.message_field(491)


@dataclass(eq=False, repr=True)
class GetDividendsRequest(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    from_: Optional[datetime] = _grpc_helpers.message_field(2)
    to: Optional[datetime] = _grpc_helpers.message_field(3)
    instrument_id: str = _grpc_helpers.string_field(4)


@dataclass(eq=False, repr=True)
class GetDividendsResponse(_grpc_helpers.Message):
    dividends: List["Dividend"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class Dividend(_grpc_helpers.Message):
    dividend_net: "MoneyValue" = _grpc_helpers.message_field(1)
    payment_date: datetime = _grpc_helpers.message_field(2)
    declared_date: datetime = _grpc_helpers.message_field(3)
    last_buy_date: datetime = _grpc_helpers.message_field(4)
    dividend_type: str = _grpc_helpers.string_field(5)
    record_date: datetime = _grpc_helpers.message_field(6)
    regularity: str = _grpc_helpers.string_field(7)
    close_price: "MoneyValue" = _grpc_helpers.message_field(8)
    yield_value: "Quotation" = _grpc_helpers.message_field(9)
    created_at: datetime = _grpc_helpers.message_field(10)


@dataclass(eq=False, repr=True)
class AssetRequest(_grpc_helpers.Message):
    id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class AssetResponse(_grpc_helpers.Message):
    asset: "AssetFull" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class AssetsRequest(_grpc_helpers.Message):
    instrument_type: Optional["InstrumentType"] = _grpc_helpers.enum_field(1)
    instrument_status: Optional["InstrumentStatus"] = _grpc_helpers.enum_field(2)


@dataclass(eq=False, repr=True)
class AssetsResponse(_grpc_helpers.Message):
    assets: List["Asset"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class AssetFull(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    type: "AssetType" = _grpc_helpers.enum_field(2)
    name: str = _grpc_helpers.string_field(3)
    name_brief: str = _grpc_helpers.string_field(4)
    description: str = _grpc_helpers.string_field(5)
    deleted_at: datetime = _grpc_helpers.message_field(6)
    required_tests: List[str] = _grpc_helpers.message_field(7)
    currency: "AssetCurrency" = _grpc_helpers.message_field(8, group="ext")
    security: "AssetSecurity" = _grpc_helpers.message_field(9, group="ext")
    gos_reg_code: str = _grpc_helpers.string_field(10)
    cfi: str = _grpc_helpers.string_field(11)
    code_nsd: str = _grpc_helpers.string_field(12)
    status: str = _grpc_helpers.string_field(13)
    brand: "Brand" = _grpc_helpers.message_field(14)
    updated_at: datetime = _grpc_helpers.message_field(15)
    br_code: str = _grpc_helpers.string_field(16)
    br_code_name: str = _grpc_helpers.string_field(17)
    instruments: List["AssetInstrument"] = _grpc_helpers.message_field(18)


@dataclass(eq=False, repr=True)
class Asset(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    type: "AssetType" = _grpc_helpers.enum_field(2)
    name: str = _grpc_helpers.string_field(3)
    instruments: List["AssetInstrument"] = _grpc_helpers.message_field(4)


@dataclass(eq=False, repr=True)
class AssetCurrency(_grpc_helpers.Message):
    base_currency: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class AssetSecurity(_grpc_helpers.Message):
    isin: str = _grpc_helpers.string_field(1)
    type: str = _grpc_helpers.string_field(2)
    instrument_kind: "InstrumentType" = _grpc_helpers.enum_field(10)
    share: "AssetShare" = _grpc_helpers.message_field(3, group="ext")
    bond: "AssetBond" = _grpc_helpers.message_field(4, group="ext")
    sp: "AssetStructuredProduct" = _grpc_helpers.message_field(5, group="ext")
    etf: "AssetEtf" = _grpc_helpers.message_field(6, group="ext")
    clearing_certificate: "AssetClearingCertificate" = _grpc_helpers.message_field(
        7, group="ext"
    )


@dataclass(eq=False, repr=True)
class AssetShare(_grpc_helpers.Message):
    type: "ShareType" = _grpc_helpers.enum_field(1)
    issue_size: "Quotation" = _grpc_helpers.message_field(2)
    nominal: "Quotation" = _grpc_helpers.message_field(3)
    nominal_currency: str = _grpc_helpers.string_field(4)
    primary_index: str = _grpc_helpers.string_field(5)
    dividend_rate: "Quotation" = _grpc_helpers.message_field(6)
    preferred_share_type: str = _grpc_helpers.string_field(7)
    ipo_date: datetime = _grpc_helpers.message_field(8)
    registry_date: datetime = _grpc_helpers.message_field(9)
    div_yield_flag: bool = _grpc_helpers.bool_field(10)
    issue_kind: str = _grpc_helpers.string_field(11)
    placement_date: datetime = _grpc_helpers.message_field(12)
    repres_isin: str = _grpc_helpers.string_field(13)
    issue_size_plan: "Quotation" = _grpc_helpers.message_field(14)
    total_float: "Quotation" = _grpc_helpers.message_field(15)


@dataclass(eq=False, repr=True)
class AssetBond(_grpc_helpers.Message):
    current_nominal: "Quotation" = _grpc_helpers.message_field(1)
    borrow_name: str = _grpc_helpers.string_field(2)
    issue_size: "Quotation" = _grpc_helpers.message_field(3)
    nominal: "Quotation" = _grpc_helpers.message_field(4)
    nominal_currency: str = _grpc_helpers.string_field(5)
    issue_kind: str = _grpc_helpers.string_field(6)
    interest_kind: str = _grpc_helpers.string_field(7)
    coupon_quantity_per_year: int = _grpc_helpers.int32_field(8)
    indexed_nominal_flag: bool = _grpc_helpers.bool_field(9)
    subordinated_flag: bool = _grpc_helpers.bool_field(10)
    collateral_flag: bool = _grpc_helpers.bool_field(11)
    tax_free_flag: bool = _grpc_helpers.bool_field(12)
    amortization_flag: bool = _grpc_helpers.bool_field(13)
    floating_coupon_flag: bool = _grpc_helpers.bool_field(14)
    perpetual_flag: bool = _grpc_helpers.bool_field(15)
    maturity_date: datetime = _grpc_helpers.message_field(16)
    return_condition: str = _grpc_helpers.string_field(17)
    state_reg_date: datetime = _grpc_helpers.message_field(18)
    placement_date: datetime = _grpc_helpers.message_field(19)
    placement_price: "Quotation" = _grpc_helpers.message_field(20)
    issue_size_plan: "Quotation" = _grpc_helpers.message_field(21)


@dataclass(eq=False, repr=True)
class AssetStructuredProduct(_grpc_helpers.Message):
    borrow_name: str = _grpc_helpers.string_field(1)
    nominal: "Quotation" = _grpc_helpers.message_field(2)
    nominal_currency: str = _grpc_helpers.string_field(3)
    type: "StructuredProductType" = _grpc_helpers.enum_field(4)
    logic_portfolio: str = _grpc_helpers.string_field(5)
    asset_type: "AssetType" = _grpc_helpers.enum_field(6)
    basic_asset: str = _grpc_helpers.string_field(7)
    safety_barrier: "Quotation" = _grpc_helpers.message_field(8)
    maturity_date: datetime = _grpc_helpers.message_field(9)
    issue_size_plan: "Quotation" = _grpc_helpers.message_field(10)
    issue_size: "Quotation" = _grpc_helpers.message_field(11)
    placement_date: datetime = _grpc_helpers.message_field(12)
    issue_kind: str = _grpc_helpers.string_field(13)


@dataclass(eq=False, repr=True)
class AssetEtf(_grpc_helpers.Message):
    total_expense: "Quotation" = _grpc_helpers.message_field(1)
    hurdle_rate: "Quotation" = _grpc_helpers.message_field(2)
    performance_fee: "Quotation" = _grpc_helpers.message_field(3)
    fixed_commission: "Quotation" = _grpc_helpers.message_field(4)
    payment_type: str = _grpc_helpers.string_field(5)
    watermark_flag: bool = _grpc_helpers.bool_field(6)
    buy_premium: "Quotation" = _grpc_helpers.message_field(7)
    sell_discount: "Quotation" = _grpc_helpers.message_field(8)
    rebalancing_flag: bool = _grpc_helpers.bool_field(9)
    rebalancing_freq: str = _grpc_helpers.string_field(10)
    management_type: str = _grpc_helpers.string_field(11)
    primary_index: str = _grpc_helpers.string_field(12)
    focus_type: str = _grpc_helpers.string_field(13)
    leveraged_flag: bool = _grpc_helpers.bool_field(14)
    num_share: "Quotation" = _grpc_helpers.message_field(15)
    ucits_flag: bool = _grpc_helpers.bool_field(16)
    released_date: datetime = _grpc_helpers.message_field(17)
    description: str = _grpc_helpers.string_field(18)
    primary_index_description: str = _grpc_helpers.string_field(19)
    primary_index_company: str = _grpc_helpers.string_field(20)
    index_recovery_period: "Quotation" = _grpc_helpers.message_field(21)
    inav_code: str = _grpc_helpers.string_field(22)
    div_yield_flag: bool = _grpc_helpers.bool_field(23)
    expense_commission: "Quotation" = _grpc_helpers.message_field(24)
    primary_index_tracking_error: "Quotation" = _grpc_helpers.message_field(25)
    rebalancing_plan: str = _grpc_helpers.string_field(26)
    tax_rate: str = _grpc_helpers.string_field(27)
    rebalancing_dates: List[datetime] = _grpc_helpers.message_field(28)
    issue_kind: str = _grpc_helpers.string_field(29)
    nominal: "Quotation" = _grpc_helpers.message_field(30)
    nominal_currency: str = _grpc_helpers.string_field(31)


@dataclass(eq=False, repr=True)
class AssetClearingCertificate(_grpc_helpers.Message):
    nominal: "Quotation" = _grpc_helpers.message_field(1)
    nominal_currency: str = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class Brand(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    name: str = _grpc_helpers.string_field(2)
    description: str = _grpc_helpers.string_field(3)
    info: str = _grpc_helpers.string_field(4)
    company: str = _grpc_helpers.string_field(5)
    sector: str = _grpc_helpers.string_field(6)
    country_of_risk: str = _grpc_helpers.string_field(7)
    country_of_risk_name: str = _grpc_helpers.string_field(8)


@dataclass(eq=False, repr=True)
class AssetInstrument(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    figi: str = _grpc_helpers.string_field(2)
    instrument_type: str = _grpc_helpers.string_field(3)
    ticker: str = _grpc_helpers.string_field(4)
    class_code: str = _grpc_helpers.string_field(5)
    links: List["InstrumentLink"] = _grpc_helpers.message_field(6)
    instrument_kind: "InstrumentType" = _grpc_helpers.enum_field(10)
    position_uid: str = _grpc_helpers.string_field(11)


@dataclass(eq=False, repr=True)
class InstrumentLink(_grpc_helpers.Message):
    type: str = _grpc_helpers.string_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class GetFavoritesRequest(_grpc_helpers.Message):
    group_id: Optional[str] = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class GetFavoritesResponse(_grpc_helpers.Message):
    favorite_instruments: List["FavoriteInstrument"] = _grpc_helpers.message_field(1)
    group_id: Optional[str] = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class FavoriteInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    instrument_type: str = _grpc_helpers.string_field(11)
    name: str = _grpc_helpers.string_field(12)
    uid: str = _grpc_helpers.string_field(13)
    otc_flag: bool = _grpc_helpers.bool_field(16)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(17)
    instrument_kind: "InstrumentType" = _grpc_helpers.enum_field(18)


@dataclass(eq=False, repr=True)
class EditFavoritesRequest(_grpc_helpers.Message):
    instruments: List["EditFavoritesRequestInstrument"] = _grpc_helpers.message_field(1)
    action_type: "EditFavoritesActionType" = _grpc_helpers.enum_field(6)
    group_id: Optional[str] = _grpc_helpers.string_field(7)


@dataclass(eq=False, repr=True)
class EditFavoritesRequestInstrument(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class EditFavoritesResponse(_grpc_helpers.Message):
    favorite_instruments: List["FavoriteInstrument"] = _grpc_helpers.message_field(1)
    group_id: Optional[str] = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class CreateFavoriteGroupRequest(_grpc_helpers.Message):
    group_name: str = _grpc_helpers.string_field(1)
    group_color: str = _grpc_helpers.string_field(2)
    note: Optional[str] = _grpc_helpers.string_field(3)


@dataclass(eq=False, repr=True)
class CreateFavoriteGroupResponse(_grpc_helpers.Message):
    group_id: str = _grpc_helpers.string_field(1)
    group_name: str = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class DeleteFavoriteGroupRequest(_grpc_helpers.Message):
    group_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class DeleteFavoriteGroupResponse(_grpc_helpers.Message):
    pass


@dataclass(eq=False, repr=True)
class GetFavoriteGroupsRequest(_grpc_helpers.Message):
    instrument_id: List[str] = _grpc_helpers.string_field(1)
    excluded_group_id: List[str] = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class GetFavoriteGroupsResponse(_grpc_helpers.Message):
    groups: List["FavoriteGroup"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class FavoriteGroup(_grpc_helpers.Message):
    group_id: str = _grpc_helpers.string_field(1)
    group_name: str = _grpc_helpers.string_field(2)
    color: str = _grpc_helpers.string_field(3)
    size: int = _grpc_helpers.int32_field(4)
    contains_instrument: Optional[bool] = _grpc_helpers.message_field(5)


@dataclass(eq=False, repr=True)
class GetCountriesRequest(_grpc_helpers.Message):
    pass


@dataclass(eq=False, repr=True)
class GetCountriesResponse(_grpc_helpers.Message):
    countries: List["CountryResponse"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class IndicativesRequest(_grpc_helpers.Message):
    pass


@dataclass(eq=False, repr=True)
class IndicativeResponse(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    currency: str = _grpc_helpers.string_field(4)
    instrument_kind: "InstrumentType" = _grpc_helpers.enum_field(10)
    name: str = _grpc_helpers.string_field(12)
    exchange: str = _grpc_helpers.string_field(13)
    uid: str = _grpc_helpers.string_field(14)
    buy_available_flag: bool = _grpc_helpers.bool_field(404)
    sell_available_flag: bool = _grpc_helpers.bool_field(405)


@dataclass(eq=False, repr=True)
class IndicativesResponse(_grpc_helpers.Message):
    instruments: List["IndicativeResponse"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class CountryResponse(_grpc_helpers.Message):
    alfa_two: str = _grpc_helpers.string_field(1)
    alfa_three: str = _grpc_helpers.string_field(2)
    name: str = _grpc_helpers.string_field(3)
    name_brief: str = _grpc_helpers.string_field(4)


@dataclass(eq=False, repr=True)
class FindInstrumentRequest(_grpc_helpers.Message):
    query: str = _grpc_helpers.string_field(1)
    instrument_kind: Optional["InstrumentType"] = _grpc_helpers.enum_field(2)
    api_trade_available_flag: Optional[bool] = _grpc_helpers.bool_field(3)


@dataclass(eq=False, repr=True)
class FindInstrumentResponse(_grpc_helpers.Message):
    instruments: List["InstrumentShort"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class InstrumentShort(_grpc_helpers.Message):
    isin: str = _grpc_helpers.string_field(1)
    figi: str = _grpc_helpers.string_field(2)
    ticker: str = _grpc_helpers.string_field(3)
    class_code: str = _grpc_helpers.string_field(4)
    instrument_type: str = _grpc_helpers.string_field(5)
    name: str = _grpc_helpers.string_field(6)
    uid: str = _grpc_helpers.string_field(7)
    position_uid: str = _grpc_helpers.string_field(8)
    instrument_kind: "InstrumentType" = _grpc_helpers.enum_field(10)
    api_trade_available_flag: str = _grpc_helpers.string_field(11)
    for_iis_flag: bool = _grpc_helpers.bool_field(12)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(26)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(27)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(28)
    weekend_flag: bool = _grpc_helpers.bool_field(29)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(30)
    lot: int = _grpc_helpers.int32_field(31)


@dataclass(eq=False, repr=True)
class GetBrandsRequest(_grpc_helpers.Message):
    paging: "Page" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetBrandRequest(_grpc_helpers.Message):
    id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class GetBrandsResponse(_grpc_helpers.Message):
    brands: List["Brand"] = _grpc_helpers.message_field(1)
    paging: "PageResponse" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class MarketDataRequest(_grpc_helpers.Message):
    subscribe_candles_request: "SubscribeCandlesRequest" = _grpc_helpers.message_field(
        1, group="payload"
    )
    subscribe_order_book_request: "SubscribeOrderBookRequest" = (
        _grpc_helpers.message_field(2, group="payload")
    )
    subscribe_trades_request: "SubscribeTradesRequest" = _grpc_helpers.message_field(
        3, group="payload"
    )
    subscribe_info_request: "SubscribeInfoRequest" = _grpc_helpers.message_field(
        4, group="payload"
    )
    subscribe_last_price_request: "SubscribeLastPriceRequest" = (
        _grpc_helpers.message_field(5, group="payload")
    )
    get_my_subscriptions: "GetMySubscriptions" = _grpc_helpers.message_field(
        6, group="payload"
    )
    ping: "PingRequest" = _grpc_helpers.message_field(7, group="payload")
    ping_settings: "PingDelaySettings" = _grpc_helpers.message_field(
        15, group="payload"
    )


@dataclass(eq=False, repr=True)
class MarketDataServerSideStreamRequest(_grpc_helpers.Message):
    subscribe_candles_request: "SubscribeCandlesRequest" = _grpc_helpers.message_field(
        1
    )
    subscribe_order_book_request: "SubscribeOrderBookRequest" = (
        _grpc_helpers.message_field(2)
    )
    subscribe_trades_request: "SubscribeTradesRequest" = _grpc_helpers.message_field(3)
    subscribe_info_request: "SubscribeInfoRequest" = _grpc_helpers.message_field(4)
    subscribe_last_price_request: "SubscribeLastPriceRequest" = (
        _grpc_helpers.message_field(5)
    )
    ping_settings: "PingDelaySettings" = _grpc_helpers.message_field(15)


@dataclass(eq=False, repr=True)
class MarketDataResponse(
    _grpc_helpers.Message
):  # pylint:disable=too-many-instance-attributes
    subscribe_candles_response: "SubscribeCandlesResponse" = (
        _grpc_helpers.message_field(1, group="payload")
    )
    subscribe_order_book_response: "SubscribeOrderBookResponse" = (
        _grpc_helpers.message_field(2, group="payload")
    )
    subscribe_trades_response: "SubscribeTradesResponse" = _grpc_helpers.message_field(
        3, group="payload"
    )
    subscribe_info_response: "SubscribeInfoResponse" = _grpc_helpers.message_field(
        4, group="payload"
    )
    candle: "Candle" = _grpc_helpers.message_field(5, group="payload")
    trade: "Trade" = _grpc_helpers.message_field(6, group="payload")
    orderbook: "OrderBook" = _grpc_helpers.message_field(7, group="payload")
    trading_status: "TradingStatus" = _grpc_helpers.message_field(8, group="payload")
    ping: "Ping" = _grpc_helpers.message_field(9, group="payload")
    subscribe_last_price_response: "SubscribeLastPriceResponse" = (
        _grpc_helpers.message_field(10, group="payload")
    )
    last_price: "LastPrice" = _grpc_helpers.message_field(11, group="payload")
    open_interest: "OpenInterest" = _grpc_helpers.message_field(12, group="payload")


@dataclass(eq=False, repr=True)
class SubscribeCandlesRequest(_grpc_helpers.Message):
    subscription_action: "SubscriptionAction" = _grpc_helpers.enum_field(1)
    instruments: List["CandleInstrument"] = _grpc_helpers.message_field(2)
    waiting_close: bool = _grpc_helpers.bool_field(3)
    candle_source_type: "CandleSource" = _grpc_helpers.enum_field(9)


@dataclass(eq=False, repr=True)
class CandleInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    interval: "SubscriptionInterval" = _grpc_helpers.enum_field(2)
    instrument_id: str = _grpc_helpers.string_field(3)


@dataclass(eq=False, repr=True)
class SubscribeCandlesResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    candles_subscriptions: List["CandleSubscription"] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class CandleSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    interval: "SubscriptionInterval" = _grpc_helpers.enum_field(2)
    subscription_status: "SubscriptionStatus" = _grpc_helpers.enum_field(3)
    instrument_uid: str = _grpc_helpers.string_field(4)
    waiting_close: bool = _grpc_helpers.bool_field(5)
    stream_id: str = _grpc_helpers.string_field(6)
    subscription_id: str = _grpc_helpers.string_field(7)
    subscription_action: "SubscriptionAction" = _grpc_helpers.enum_field(8)
    candle_source_type: Optional["CandleSource"] = _grpc_helpers.enum_field(
        9, optional=True
    )


@dataclass(eq=False, repr=True)
class SubscribeOrderBookRequest(_grpc_helpers.Message):
    subscription_action: "SubscriptionAction" = _grpc_helpers.enum_field(1)
    instruments: List["OrderBookInstrument"] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class OrderBookInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    instrument_id: str = _grpc_helpers.string_field(3)
    order_book_type: "OrderBookType" = _grpc_helpers.message_field(4)


@dataclass(eq=False, repr=True)
class SubscribeOrderBookResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    order_book_subscriptions: List[
        "OrderBookSubscription"
    ] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class OrderBookSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    subscription_status: "SubscriptionStatus" = _grpc_helpers.enum_field(3)
    instrument_uid: str = _grpc_helpers.string_field(4)
    stream_id: str = _grpc_helpers.string_field(5)
    subscription_id: str = _grpc_helpers.string_field(6)
    order_book_type: "OrderBookType" = _grpc_helpers.message_field(7)
    subscription_action: "SubscriptionAction" = _grpc_helpers.enum_field(8)


@dataclass(eq=False, repr=True)
class SubscribeTradesRequest(_grpc_helpers.Message):
    subscription_action: "SubscriptionAction" = _grpc_helpers.enum_field(1)
    instruments: List["TradeInstrument"] = _grpc_helpers.message_field(2)
    trade_source: "TradeSourceType" = _grpc_helpers.message_field(3)
    with_open_interest: bool = _grpc_helpers.bool_field(4)


@dataclass(eq=False, repr=True)
class SubscribeLastPriceRequest(_grpc_helpers.Message):
    subscription_action: "SubscriptionAction" = _grpc_helpers.message_field(1)
    instruments: List["LastPriceInstrument"] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class LastPriceInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class SubscribeLastPriceResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    last_price_subscriptions: List[
        "LastPriceSubscription"
    ] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class LastPriceSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    subscription_status: "SubscriptionStatus" = _grpc_helpers.message_field(2)
    instrument_uid: str = _grpc_helpers.string_field(3)
    stream_id: str = _grpc_helpers.string_field(4)
    subscription_id: str = _grpc_helpers.string_field(5)
    subscription_action: "SubscriptionAction" = _grpc_helpers.message_field(6)


@dataclass(eq=False, repr=True)
class TradeInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class SubscribeTradesResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    trade_subscriptions: List["TradeSubscription"] = _grpc_helpers.message_field(2)
    trade_source: "TradeSourceType" = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class TradeSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    subscription_status: "SubscriptionStatus" = _grpc_helpers.enum_field(2)
    instrument_uid: str = _grpc_helpers.string_field(3)
    stream_id: str = _grpc_helpers.string_field(4)
    subscription_id: str = _grpc_helpers.string_field(5)
    with_open_interest: bool = _grpc_helpers.bool_field(6)
    subscription_action: "SubscriptionAction" = _grpc_helpers.enum_field(7)


@dataclass(eq=False, repr=True)
class SubscribeInfoRequest(_grpc_helpers.Message):
    subscription_action: "SubscriptionAction" = _grpc_helpers.enum_field(1)
    instruments: List["InfoInstrument"] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class InfoInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class SubscribeInfoResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    info_subscriptions: List["InfoSubscription"] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class InfoSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    subscription_status: "SubscriptionStatus" = _grpc_helpers.enum_field(2)
    instrument_uid: str = _grpc_helpers.string_field(3)
    stream_id: str = _grpc_helpers.string_field(4)
    subscription_id: str = _grpc_helpers.string_field(5)
    subscription_action: "SubscriptionAction" = _grpc_helpers.enum_field(6)


@dataclass(eq=False, repr=True)
class Candle(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    interval: "SubscriptionInterval" = _grpc_helpers.enum_field(2)
    open: "Quotation" = _grpc_helpers.message_field(3)
    high: "Quotation" = _grpc_helpers.message_field(4)
    low: "Quotation" = _grpc_helpers.message_field(5)
    close: "Quotation" = _grpc_helpers.message_field(6)
    volume: int = _grpc_helpers.int64_field(7)
    time: datetime = _grpc_helpers.message_field(8)
    last_trade_ts: datetime = _grpc_helpers.message_field(9)
    instrument_uid: str = _grpc_helpers.string_field(10)
    candle_source_type: "CandleSource" = _grpc_helpers.enum_field(19)


@dataclass(eq=False, repr=True)
class OrderBook(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    is_consistent: bool = _grpc_helpers.bool_field(3)
    bids: List["Order"] = _grpc_helpers.message_field(4)
    asks: List["Order"] = _grpc_helpers.message_field(5)
    time: datetime = _grpc_helpers.message_field(6)
    limit_up: "Quotation" = _grpc_helpers.message_field(7)
    limit_down: "Quotation" = _grpc_helpers.message_field(8)
    instrument_uid: str = _grpc_helpers.string_field(9)
    order_book_type: "OrderBookType" = _grpc_helpers.message_field(10)


@dataclass(eq=False, repr=True)
class Order(_grpc_helpers.Message):
    price: "Quotation" = _grpc_helpers.message_field(1)
    quantity: int = _grpc_helpers.int64_field(2)


@dataclass(eq=False, repr=True)
class Trade(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    direction: "TradeDirection" = _grpc_helpers.enum_field(2)
    price: "Quotation" = _grpc_helpers.message_field(3)
    quantity: int = _grpc_helpers.int64_field(4)
    time: datetime = _grpc_helpers.message_field(5)
    instrument_uid: str = _grpc_helpers.string_field(6)
    trade_source: TradeSourceType = _grpc_helpers.message_field(7)


@dataclass(eq=False, repr=True)
class TradingStatus(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    trading_status: "SecurityTradingStatus" = _grpc_helpers.enum_field(2)
    time: datetime = _grpc_helpers.enum_field(3)
    limit_order_available_flag: bool = _grpc_helpers.bool_field(4)
    market_order_available_flag: bool = _grpc_helpers.bool_field(5)
    instrument_uid: str = _grpc_helpers.string_field(6)


@dataclass(eq=False, repr=True)
class GetCandlesRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)
    interval: "CandleInterval" = _grpc_helpers.enum_field(4)
    instrument_id: Optional[str] = _grpc_helpers.string_field(5)
    candle_source_type: Optional[CandleSource] = _grpc_helpers.string_field(7)
    limit: Optional[int] = _grpc_helpers.int32_field(10)


@dataclass(eq=False, repr=True)
class GetCandlesResponse(_grpc_helpers.Message):
    candles: List["HistoricCandle"] = _grpc_helpers.message_field(1)


@dataclass(eq=True, repr=True, frozen=True)
class HistoricCandle(_grpc_helpers.Message):
    open: Quotation = _grpc_helpers.message_field(1)
    high: Quotation = _grpc_helpers.message_field(2)
    low: Quotation = _grpc_helpers.message_field(3)
    close: Quotation = _grpc_helpers.message_field(4)
    volume: int = _grpc_helpers.int64_field(5)
    time: datetime = _grpc_helpers.message_field(6)
    is_complete: bool = _grpc_helpers.bool_field(7)
    candle_source: CandleSource = _grpc_helpers.message_field(9)


@dataclass(eq=False, repr=True)
class GetLastPricesRequest(_grpc_helpers.Message):
    figi: List[str] = _grpc_helpers.string_field(1)
    instrument_id: List[str] = _grpc_helpers.string_field(2)
    last_price_type: LastPriceType = _grpc_helpers.message_field(3)
    instrument_status: Optional["InstrumentStatus"] = _grpc_helpers.enum_field(9)


@dataclass(eq=False, repr=True)
class GetLastPricesResponse(_grpc_helpers.Message):
    last_prices: List["LastPrice"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class LastPrice(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    price: "Quotation" = _grpc_helpers.message_field(2)
    time: datetime = _grpc_helpers.message_field(3)
    instrument_uid: str = _grpc_helpers.string_field(11)
    last_price_type: LastPriceType = _grpc_helpers.message_field(12)


@dataclass(eq=False, repr=True)
class OpenInterest(_grpc_helpers.Message):
    instrument_uid: str = _grpc_helpers.string_field(1)
    time: datetime = _grpc_helpers.message_field(2)
    open_interest: int = _grpc_helpers.int64_field(3)


@dataclass(eq=False, repr=True)
class GetOrderBookRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    instrument_id: Optional[str] = _grpc_helpers.string_field(3)


@dataclass(eq=False, repr=True)
class GetOrderBookResponse(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    bids: List["Order"] = _grpc_helpers.message_field(3)
    asks: List["Order"] = _grpc_helpers.message_field(4)
    last_price: "Quotation" = _grpc_helpers.message_field(5)
    close_price: "Quotation" = _grpc_helpers.message_field(6)
    limit_up: "Quotation" = _grpc_helpers.message_field(7)
    limit_down: "Quotation" = _grpc_helpers.message_field(8)
    last_price_ts: datetime = _grpc_helpers.message_field(21)
    close_price_ts: datetime = _grpc_helpers.message_field(22)
    orderbook_ts: datetime = _grpc_helpers.message_field(23)
    instrument_uid: str = _grpc_helpers.string_field(9)


@dataclass(eq=False, repr=True)
class GetTradingStatusRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1)
    instrument_id: Optional[str] = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class GetTradingStatusesRequest(_grpc_helpers.Message):
    instrument_id: List[str] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetTradingStatusesResponse(_grpc_helpers.Message):
    trading_statuses: List["GetTradingStatusResponse"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetTradingStatusResponse(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    trading_status: "SecurityTradingStatus" = _grpc_helpers.enum_field(2)
    limit_order_available_flag: bool = _grpc_helpers.bool_field(3)
    market_order_available_flag: bool = _grpc_helpers.bool_field(4)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(5)
    instrument_uid: str = _grpc_helpers.string_field(6)

    bestprice_order_available_flag: bool = _grpc_helpers.bool_field(8)
    only_best_price: bool = _grpc_helpers.bool_field(9)


@dataclass(eq=False, repr=True)
class GetLastTradesRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)
    instrument_id: Optional[str] = _grpc_helpers.string_field(4)
    trade_source: TradeSourceType = _grpc_helpers.enum_field(5)


@dataclass(eq=False, repr=True)
class GetLastTradesResponse(_grpc_helpers.Message):
    trades: List["Trade"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetMySubscriptions(_grpc_helpers.Message):
    pass


@dataclass(eq=False, repr=True)
class GetClosePricesRequest(_grpc_helpers.Message):
    instruments: List["InstrumentClosePriceRequest"] = _grpc_helpers.message_field(1)
    instrument_status: Optional["InstrumentStatus"] = _grpc_helpers.enum_field(9)


@dataclass(eq=False, repr=True)
class InstrumentClosePriceRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class GetClosePricesResponse(_grpc_helpers.Message):
    close_prices: List["InstrumentClosePriceResponse"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class InstrumentClosePriceResponse(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)
    price: "Quotation" = _grpc_helpers.message_field(11)
    evening_session_price: "Quotation" = _grpc_helpers.message_field(12)
    time: datetime = _grpc_helpers.message_field(21)
    evening_session_price_time: datetime = _grpc_helpers.message_field(23)


@dataclass(eq=False, repr=True)
class GetMarketValuesRequest(_grpc_helpers.Message):
    instrument_id: List[str] = _grpc_helpers.message_field(1)
    values: List["MarketValueType"] = _grpc_helpers.message_field(2)


class MarketValueType(_grpc_helpers.Enum):
    INSTRUMENT_VALUE_UNSPECIFIED = 0
    INSTRUMENT_VALUE_LAST_PRICE = 1
    INSTRUMENT_VALUE_LAST_PRICE_DEALER = 2
    INSTRUMENT_VALUE_CLOSE_PRICE = 3
    INSTRUMENT_VALUE_EVENING_SESSION_PRICE = 4
    INSTRUMENT_VALUE_OPEN_INTEREST = 5


@dataclass(eq=False, repr=True)
class GetMarketValuesResponse(_grpc_helpers.Message):
    instruments: List["MarketValueInstrument"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class MarketValueInstrument(_grpc_helpers.Message):
    instrument_uid: str = _grpc_helpers.string_field(1)
    values: List["MarketValue"] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class MarketValue(_grpc_helpers.Message):
    type: "MarketValueType" = _grpc_helpers.enum_field(1)
    value: "Quotation" = _grpc_helpers.message_field(2)
    time: datetime = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class Smoothing(_grpc_helpers.Message):
    fast_length: int = _grpc_helpers.int32_field(1)
    slow_length: int = _grpc_helpers.int32_field(2)
    signal_smoothing: int = _grpc_helpers.int32_field(3)


@dataclass(eq=False, repr=True)
class Deviation(_grpc_helpers.Message):
    deviation_multiplier: "Quotation" = _grpc_helpers.message_field(1)


class IndicatorInterval(_grpc_helpers.Enum):
    INDICATOR_INTERVAL_UNSPECIFIED = 0
    INDICATOR_INTERVAL_ONE_MINUTE = 1
    INDICATOR_INTERVAL_FIVE_MINUTES = 2
    INDICATOR_INTERVAL_FIFTEEN_MINUTES = 3
    INDICATOR_INTERVAL_ONE_HOUR = 4
    INDICATOR_INTERVAL_ONE_DAY = 5
    INDICATOR_INTERVAL_2_MIN = 6
    INDICATOR_INTERVAL_3_MIN = 7
    INDICATOR_INTERVAL_10_MIN = 8
    INDICATOR_INTERVAL_30_MIN = 9
    INDICATOR_INTERVAL_2_HOUR = 10
    INDICATOR_INTERVAL_4_HOUR = 11
    INDICATOR_INTERVAL_WEEK = 12
    INDICATOR_INTERVAL_MONTH = 13


class TypeOfPrice(_grpc_helpers.Enum):
    TYPE_OF_PRICE_UNSPECIFIED = 0
    TYPE_OF_PRICE_CLOSE = 1
    TYPE_OF_PRICE_OPEN = 2
    TYPE_OF_PRICE_HIGH = 3
    TYPE_OF_PRICE_LOW = 4
    TYPE_OF_PRICE_AVG = 5


class IndicatorType(_grpc_helpers.Enum):
    INDICATOR_TYPE_UNSPECIFIED = 0
    INDICATOR_TYPE_BB = 1
    INDICATOR_TYPE_EMA = 2
    INDICATOR_TYPE_RSI = 3
    INDICATOR_TYPE_MACD = 4
    INDICATOR_TYPE_SMA = 5


@dataclass(eq=False, repr=True)
class GetTechAnalysisRequest(_grpc_helpers.Message):
    indicator_type: "IndicatorType" = _grpc_helpers.enum_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)
    from_: datetime = _grpc_helpers.message_field(3)
    to: datetime = _grpc_helpers.message_field(4)
    interval: "IndicatorInterval" = _grpc_helpers.enum_field(5)
    type_of_price: "TypeOfPrice" = _grpc_helpers.enum_field(6)
    length: int = _grpc_helpers.int32_field(7)
    deviation: "Deviation" = _grpc_helpers.message_field(8)
    smoothing: "Smoothing" = _grpc_helpers.message_field(9)


@dataclass(eq=False, repr=True)
class TechAnalysisItem(_grpc_helpers.Message):
    timestamp: datetime = _grpc_helpers.message_field(1)
    middle_band: Optional["Quotation"] = _grpc_helpers.message_field(2, optional=True)
    upper_band: Optional["Quotation"] = _grpc_helpers.message_field(3, optional=True)
    lower_band: Optional["Quotation"] = _grpc_helpers.message_field(4, optional=True)
    signal: Optional["Quotation"] = _grpc_helpers.message_field(5, optional=True)
    macd: Optional["Quotation"] = _grpc_helpers.message_field(6, optional=True)


@dataclass(eq=False, repr=True)
class GetTechAnalysisResponse(_grpc_helpers.Message):
    technical_indicators: List["TechAnalysisItem"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class OperationsRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    from_: Optional[datetime] = _grpc_helpers.message_field(2)
    to: Optional[datetime] = _grpc_helpers.message_field(3)
    state: Optional["OperationState"] = _grpc_helpers.enum_field(4)
    figi: Optional[str] = _grpc_helpers.string_field(5)


@dataclass(eq=False, repr=True)
class OperationsResponse(_grpc_helpers.Message):
    operations: List["Operation"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class OperationTrade(_grpc_helpers.Message):
    trade_id: str = _grpc_helpers.string_field(1)
    date_time: datetime = _grpc_helpers.message_field(2)
    quantity: int = _grpc_helpers.int64_field(3)
    price: "MoneyValue" = _grpc_helpers.message_field(4)


@dataclass(eq=False, repr=True)
class ChildOperationItem(_grpc_helpers.Message):
    instrument_uid: str = _grpc_helpers.string_field(1)
    payment: "MoneyValue" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class Operation(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    id: str = _grpc_helpers.string_field(1)
    parent_operation_id: str = _grpc_helpers.string_field(2)
    currency: str = _grpc_helpers.string_field(3)
    payment: "MoneyValue" = _grpc_helpers.message_field(4)
    price: "MoneyValue" = _grpc_helpers.message_field(5)
    state: "OperationState" = _grpc_helpers.enum_field(6)
    quantity: int = _grpc_helpers.int64_field(7)
    quantity_rest: int = _grpc_helpers.int64_field(8)
    figi: str = _grpc_helpers.string_field(9)
    instrument_type: str = _grpc_helpers.string_field(10)
    date: datetime = _grpc_helpers.message_field(11)
    type: str = _grpc_helpers.string_field(12)
    operation_type: "OperationType" = _grpc_helpers.enum_field(13)
    trades: List["OperationTrade"] = _grpc_helpers.message_field(14)
    asset_uid: str = _grpc_helpers.string_field(16)
    position_uid: str = _grpc_helpers.string_field(17)
    instrument_uid: str = _grpc_helpers.string_field(18)
    child_operations: List["ChildOperationItem"] = _grpc_helpers.message_field(19)


class CurrencyRequest(_grpc_helpers.Enum):
    RUB = 0
    USD = 1
    EUR = 2


@dataclass(eq=False, repr=True)
class PortfolioRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    currency: Optional[CurrencyRequest] = _grpc_helpers.enum_field(2)


@dataclass(eq=False, repr=True)
class VirtualPortfolioPosition(_grpc_helpers.Message):
    position_uid: str = _grpc_helpers.string_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)
    figi: str = _grpc_helpers.string_field(3)
    instrument_type: str = _grpc_helpers.string_field(4)
    quantity: "Quotation" = _grpc_helpers.message_field(5)
    average_position_price: "MoneyValue" = _grpc_helpers.message_field(6)
    expected_yield: "Quotation" = _grpc_helpers.message_field(7)
    expected_yield_fifo: "Quotation" = _grpc_helpers.message_field(8)
    expire_date: datetime = _grpc_helpers.message_field(9)
    current_price: "MoneyValue" = _grpc_helpers.message_field(10)
    average_position_price_fifo: "MoneyValue" = _grpc_helpers.message_field(11)
    daily_yield: "MoneyValue" = _grpc_helpers.message_field(31)
    ticker: str = _grpc_helpers.string_field(32)


@dataclass(eq=False, repr=True)
class PortfolioResponse(_grpc_helpers.Message):
    total_amount_shares: "MoneyValue" = _grpc_helpers.message_field(1)
    total_amount_bonds: "MoneyValue" = _grpc_helpers.message_field(2)
    total_amount_etf: "MoneyValue" = _grpc_helpers.message_field(3)
    total_amount_currencies: "MoneyValue" = _grpc_helpers.message_field(4)
    total_amount_futures: "MoneyValue" = _grpc_helpers.message_field(5)
    expected_yield: "Quotation" = _grpc_helpers.message_field(6)
    positions: List["PortfolioPosition"] = _grpc_helpers.message_field(7)
    account_id: str = _grpc_helpers.string_field(8)

    total_amount_options: MoneyValue = _grpc_helpers.message_field(9)
    total_amount_sp: MoneyValue = _grpc_helpers.message_field(10)
    total_amount_portfolio: MoneyValue = _grpc_helpers.message_field(11)
    virtual_positions: List["VirtualPortfolioPosition"] = _grpc_helpers.message_field(
        12
    )
    daily_yield: MoneyValue = _grpc_helpers.message_field(16)
    daily_yield_relative: Quotation = _grpc_helpers.message_field(17)


@dataclass(eq=False, repr=True)
class PositionsRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class PositionsResponse(_grpc_helpers.Message):
    money: List["MoneyValue"] = _grpc_helpers.message_field(1)
    blocked: List["MoneyValue"] = _grpc_helpers.message_field(2)
    securities: List["PositionsSecurities"] = _grpc_helpers.message_field(3)
    limits_loading_in_progress: bool = _grpc_helpers.bool_field(4)
    futures: List["PositionsFutures"] = _grpc_helpers.bool_field(5)
    options: List["PositionsOptions"] = _grpc_helpers.bool_field(6)
    account_id: str = _grpc_helpers.string_field(15)


@dataclass(eq=False, repr=True)
class WithdrawLimitsRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class WithdrawLimitsResponse(_grpc_helpers.Message):
    money: List["MoneyValue"] = _grpc_helpers.message_field(1)
    blocked: List["MoneyValue"] = _grpc_helpers.message_field(2)
    blocked_guarantee: List["MoneyValue"] = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class PortfolioPosition(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_type: str = _grpc_helpers.string_field(2)
    quantity: "Quotation" = _grpc_helpers.message_field(3)
    average_position_price: "MoneyValue" = _grpc_helpers.message_field(4)
    expected_yield: "Quotation" = _grpc_helpers.message_field(5)
    current_nkd: "MoneyValue" = _grpc_helpers.message_field(6)
    average_position_price_pt: "Quotation" = _grpc_helpers.message_field(7)
    current_price: "MoneyValue" = _grpc_helpers.message_field(8)
    average_position_price_fifo: "MoneyValue" = _grpc_helpers.message_field(9)
    quantity_lots: "Quotation" = _grpc_helpers.message_field(10)
    blocked: bool = _grpc_helpers.bool_field(21)
    blocked_lots: "Quotation" = _grpc_helpers.message_field(22)
    position_uid: str = _grpc_helpers.string_field(24)
    instrument_uid: str = _grpc_helpers.string_field(25)
    var_margin: "MoneyValue" = _grpc_helpers.message_field(26)
    expected_yield_fifo: "Quotation" = _grpc_helpers.message_field(27)
    daily_yield: "MoneyValue" = _grpc_helpers.message_field(31)
    ticker: str = _grpc_helpers.string_field(32)


@dataclass(eq=False, repr=True)
class PositionsSecurities(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    blocked: int = _grpc_helpers.int64_field(2)
    balance: int = _grpc_helpers.int64_field(3)
    position_uid: str = _grpc_helpers.string_field(4)
    instrument_uid: str = _grpc_helpers.string_field(5)
    exchange_blocked: bool = _grpc_helpers.bool_field(11)
    instrument_type: str = _grpc_helpers.string_field(16)
    ticker: str = _grpc_helpers.string_field(6)


@dataclass(eq=False, repr=True)
class TradesStreamRequest(_grpc_helpers.Message):
    accounts: List[str] = _grpc_helpers.string_field(1)
    ping_delay_ms: Optional[int] = _grpc_helpers.int32_field(15)


@dataclass(eq=False, repr=True)
class TradesStreamResponse(_grpc_helpers.Message):
    order_trades: "OrderTrades" = _grpc_helpers.message_field(1, group="payload")
    ping: "Ping" = _grpc_helpers.message_field(2, group="payload")
    subscription: "SubscriptionResponse" = _grpc_helpers.message_field(
        3, group="payload"
    )


@dataclass(eq=False, repr=True)
class OrderTrades(_grpc_helpers.Message):
    order_id: str = _grpc_helpers.string_field(1)
    created_at: datetime = _grpc_helpers.message_field(2)
    direction: "OrderDirection" = _grpc_helpers.enum_field(3)
    figi: str = _grpc_helpers.string_field(4)
    trades: List["OrderTrade"] = _grpc_helpers.message_field(5)
    account_id: str = _grpc_helpers.string_field(6)
    instrument_uid: str = _grpc_helpers.string_field(7)


@dataclass(eq=False, repr=True)
class OrderTrade(_grpc_helpers.Message):
    date_time: datetime = _grpc_helpers.message_field(1)
    price: "Quotation" = _grpc_helpers.message_field(2)
    quantity: int = _grpc_helpers.int64_field(3)
    trade_id: str = _grpc_helpers.string_field(4)


@dataclass(eq=False, repr=True)
class PostOrderRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1)
    quantity: int = _grpc_helpers.int64_field(2)
    price: Optional["Quotation"] = _grpc_helpers.message_field(3)
    direction: "OrderDirection" = _grpc_helpers.enum_field(4)
    account_id: str = _grpc_helpers.string_field(5)
    order_type: "OrderType" = _grpc_helpers.enum_field(6)
    order_id: str = _grpc_helpers.string_field(7)
    instrument_id: str = _grpc_helpers.string_field(8)
    time_in_force: "TimeInForceType" = _grpc_helpers.message_field(9)
    price_type: "PriceType" = _grpc_helpers.message_field(10)
    confirm_margin_trade: bool = _grpc_helpers.bool_field(11)


@dataclass(eq=False, repr=True)
class PostOrderResponse(  # pylint:disable=too-many-instance-attributes
    _grpc_helpers.Message
):
    order_id: str = _grpc_helpers.string_field(1)
    execution_report_status: "OrderExecutionReportStatus" = _grpc_helpers.enum_field(2)
    lots_requested: int = _grpc_helpers.int64_field(3)
    lots_executed: int = _grpc_helpers.int64_field(4)
    initial_order_price: "MoneyValue" = _grpc_helpers.message_field(5)
    executed_order_price: "MoneyValue" = _grpc_helpers.message_field(6)
    total_order_amount: "MoneyValue" = _grpc_helpers.message_field(7)
    initial_commission: "MoneyValue" = _grpc_helpers.message_field(8)
    executed_commission: "MoneyValue" = _grpc_helpers.message_field(9)
    aci_value: "MoneyValue" = _grpc_helpers.message_field(10)
    figi: str = _grpc_helpers.string_field(11)
    direction: "OrderDirection" = _grpc_helpers.enum_field(12)
    initial_security_price: "MoneyValue" = _grpc_helpers.message_field(13)
    order_type: "OrderType" = _grpc_helpers.enum_field(14)
    message: str = _grpc_helpers.string_field(15)
    initial_order_price_pt: "Quotation" = _grpc_helpers.message_field(16)
    instrument_uid: str = _grpc_helpers.string_field(17)
    order_request_id: str = _grpc_helpers.string_field(20)
    response_metadata: "ResponseMetadata" = _grpc_helpers.message_field(254)


@dataclass(eq=False, repr=True)
class PostOrderAsyncRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)
    quantity: int = _grpc_helpers.int64_field(2)
    price: "Quotation" = _grpc_helpers.message_field(3)
    direction: "OrderDirection" = _grpc_helpers.message_field(4)
    account_id: str = _grpc_helpers.string_field(5)
    order_type: "OrderType" = _grpc_helpers.message_field(6)
    order_id: str = _grpc_helpers.string_field(7)
    time_in_force: TimeInForceType = _grpc_helpers.string_field(8)
    price_type: PriceType = _grpc_helpers.string_field(9)
    confirm_margin_trade: bool = _grpc_helpers.bool_field(10)


@dataclass(eq=False, repr=True)
class PostOrderAsyncResponse(_grpc_helpers.Message):
    order_request_id: str = _grpc_helpers.string_field(1)
    execution_report_status: "OrderExecutionReportStatus" = _grpc_helpers.message_field(
        2
    )
    trade_intent_id: str = _grpc_helpers.string_field(3)


@dataclass(eq=False, repr=True)
class CancelOrderRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    order_id: str = _grpc_helpers.string_field(2)
    order_id_type: Optional["OrderIdType"] = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class CancelOrderResponse(_grpc_helpers.Message):
    time: datetime = _grpc_helpers.message_field(1)
    response_metadata: "ResponseMetadata" = _grpc_helpers.message_field(254)


@dataclass(eq=False, repr=True)
class GetOrderStateRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    order_id: str = _grpc_helpers.string_field(2)
    price_type: "PriceType" = _grpc_helpers.message_field(3)
    order_id_type: Optional["OrderIdType"] = _grpc_helpers.message_field(4)


@dataclass(eq=False, repr=True)
class GetOrdersRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class GetOrdersResponse(_grpc_helpers.Message):
    orders: List["OrderState"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class OrderState(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    order_id: str = _grpc_helpers.string_field(1)
    execution_report_status: "OrderExecutionReportStatus" = _grpc_helpers.enum_field(2)
    lots_requested: int = _grpc_helpers.int64_field(3)
    lots_executed: int = _grpc_helpers.int64_field(4)
    initial_order_price: "MoneyValue" = _grpc_helpers.message_field(5)
    executed_order_price: "MoneyValue" = _grpc_helpers.message_field(6)
    total_order_amount: "MoneyValue" = _grpc_helpers.message_field(7)
    average_position_price: "MoneyValue" = _grpc_helpers.message_field(8)
    initial_commission: "MoneyValue" = _grpc_helpers.message_field(9)
    executed_commission: "MoneyValue" = _grpc_helpers.message_field(10)
    figi: str = _grpc_helpers.string_field(11)
    direction: "OrderDirection" = _grpc_helpers.enum_field(12)
    initial_security_price: "MoneyValue" = _grpc_helpers.message_field(13)
    stages: List["OrderStage"] = _grpc_helpers.message_field(14)
    service_commission: "MoneyValue" = _grpc_helpers.message_field(15)
    currency: str = _grpc_helpers.string_field(16)
    order_type: "OrderType" = _grpc_helpers.enum_field(17)
    order_date: datetime = _grpc_helpers.message_field(18)
    instrument_uid: str = _grpc_helpers.string_field(19)
    order_request_id: str = _grpc_helpers.string_field(20)


@dataclass(eq=False, repr=True)
class OrderStage(_grpc_helpers.Message):
    price: "MoneyValue" = _grpc_helpers.message_field(1)
    quantity: int = _grpc_helpers.int64_field(2)
    trade_id: str = _grpc_helpers.string_field(3)
    execution_time: datetime = _grpc_helpers.message_field(5)


class ReplaceOrderRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    order_id: str = _grpc_helpers.string_field(6)
    idempotency_key: str = _grpc_helpers.string_field(7)
    quantity: int = _grpc_helpers.int64_field(11)
    price: Optional["Quotation"] = _grpc_helpers.message_field(12)
    price_type: Optional["PriceType"] = _grpc_helpers.enum_field(13)
    confirm_margin_trade: bool = _grpc_helpers.bool_field(14)


@dataclass(eq=False, repr=True)
class GetAccountsRequest(_grpc_helpers.Message):
    status: Optional["AccountStatus"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetAccountsResponse(_grpc_helpers.Message):
    accounts: List["Account"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class Account(_grpc_helpers.Message):
    id: str = _grpc_helpers.string_field(1)
    type: "AccountType" = _grpc_helpers.enum_field(2)
    name: str = _grpc_helpers.string_field(3)
    status: "AccountStatus" = _grpc_helpers.enum_field(4)
    opened_date: datetime = _grpc_helpers.message_field(5)
    closed_date: datetime = _grpc_helpers.message_field(6)
    access_level: "AccessLevel" = _grpc_helpers.message_field(7)

    @classmethod
    def loads(cls, obj) -> "Account":
        return cls(
            id=obj.id,
            type=AccountType(obj.type),
            name=obj.name,
            status=AccountStatus(obj.type),
            opened_date=_grpc_helpers.ts_to_datetime(obj.opened_date),
            closed_date=_grpc_helpers.ts_to_datetime(obj.closed_date),
        )


@dataclass(eq=False, repr=True)
class GetMarginAttributesRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class GetMarginAttributesResponse(_grpc_helpers.Message):
    liquid_portfolio: "MoneyValue" = _grpc_helpers.message_field(1)
    starting_margin: "MoneyValue" = _grpc_helpers.message_field(2)
    minimal_margin: "MoneyValue" = _grpc_helpers.message_field(3)
    funds_sufficiency_level: "Quotation" = _grpc_helpers.message_field(4)
    amount_of_missing_funds: "MoneyValue" = _grpc_helpers.message_field(5)
    corrected_margin: "MoneyValue" = _grpc_helpers.message_field(6)


@dataclass(eq=False, repr=True)
class GetUserTariffRequest(_grpc_helpers.Message):
    pass


@dataclass(eq=False, repr=True)
class GetUserTariffResponse(_grpc_helpers.Message):
    unary_limits: List["UnaryLimit"] = _grpc_helpers.message_field(1)
    stream_limits: List["StreamLimit"] = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class UnaryLimit(_grpc_helpers.Message):
    limit_per_minute: int = _grpc_helpers.int32_field(1)
    methods: List[str] = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class StreamLimit(_grpc_helpers.Message):
    limit: int = _grpc_helpers.int32_field(1)
    streams: List[str] = _grpc_helpers.string_field(2)
    open: int = _grpc_helpers.int32_field(3)


@dataclass(eq=False, repr=True)
class GetInfoRequest(_grpc_helpers.Message):
    pass


@dataclass(eq=False, repr=True)
class GetInfoResponse(_grpc_helpers.Message):
    prem_status: bool = _grpc_helpers.bool_field(1)
    qual_status: bool = _grpc_helpers.bool_field(2)
    qualified_for_work_with: List[str] = _grpc_helpers.string_field(3)
    tariff: str = _grpc_helpers.string_field(4)
    user_id: str = _grpc_helpers.string_field(9)
    risk_level_code: str = _grpc_helpers.string_field(12)


@dataclass(eq=False, repr=True)
class OpenSandboxAccountRequest(_grpc_helpers.Message):
    name: Optional[str] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class OpenSandboxAccountResponse(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class CloseSandboxAccountRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class CloseSandboxAccountResponse(_grpc_helpers.Message):
    pass


@dataclass(eq=False, repr=True)
class SandboxPayInRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    amount: "MoneyValue" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class SandboxPayInResponse(_grpc_helpers.Message):
    balance: "MoneyValue" = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class PostStopOrderRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1)
    quantity: int = _grpc_helpers.int64_field(2)
    price: Optional["Quotation"] = _grpc_helpers.message_field(3)
    stop_price: Optional["Quotation"] = _grpc_helpers.message_field(4)
    direction: "StopOrderDirection" = _grpc_helpers.enum_field(5)
    account_id: str = _grpc_helpers.string_field(6)
    expiration_type: "StopOrderExpirationType" = _grpc_helpers.enum_field(7)
    stop_order_type: "StopOrderType" = _grpc_helpers.enum_field(8)
    expire_date: Optional[datetime] = _grpc_helpers.message_field(9)
    instrument_id: str = _grpc_helpers.string_field(10)
    exchange_order_type: "ExchangeOrderType" = _grpc_helpers.message_field(11)
    take_profit_type: "TakeProfitType" = _grpc_helpers.message_field(12)
    trailing_data: "PostStopOrderRequestTrailingData" = _grpc_helpers.message_field(13)
    price_type: "PriceType" = _grpc_helpers.message_field(14)
    order_id: str = _grpc_helpers.string_field(15)
    confirm_margin_trade: bool = _grpc_helpers.bool_field(16)


@dataclass(eq=False, repr=True)
class PostStopOrderRequestTrailingData(_grpc_helpers.Message):
    indent: "Quotation" = _grpc_helpers.message_field(1)
    indent_type: "TrailingValueType" = _grpc_helpers.message_field(2)
    spread: "Quotation" = _grpc_helpers.message_field(3)
    spread_type: "TrailingValueType" = _grpc_helpers.message_field(4)


@dataclass(eq=False, repr=True)
class PostStopOrderResponse(_grpc_helpers.Message):
    stop_order_id: str = _grpc_helpers.string_field(1)
    order_request_id: str = _grpc_helpers.string_field(2)
    response_metadata: "ResponseMetadata" = _grpc_helpers.message_field(254)


@dataclass(eq=False, repr=True)
class GetStopOrdersRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    status: "StopOrderStatusOption" = _grpc_helpers.message_field(2)
    from_: datetime = _grpc_helpers.message_field(3)
    to: datetime = _grpc_helpers.message_field(4)


@dataclass(eq=False, repr=True)
class GetStopOrdersResponse(_grpc_helpers.Message):
    stop_orders: List["StopOrder"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class CancelStopOrderRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    stop_order_id: str = _grpc_helpers.string_field(2)


@dataclass(eq=False, repr=True)
class CancelStopOrderResponse(_grpc_helpers.Message):
    time: datetime = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class StopOrder(_grpc_helpers.Message):  # pylint:disable=too-many-instance-attributes
    stop_order_id: str = _grpc_helpers.string_field(1)
    lots_requested: int = _grpc_helpers.int64_field(2)
    figi: str = _grpc_helpers.string_field(3)
    direction: "StopOrderDirection" = _grpc_helpers.enum_field(4)
    currency: str = _grpc_helpers.string_field(5)
    order_type: "StopOrderType" = _grpc_helpers.enum_field(6)
    create_date: datetime = _grpc_helpers.message_field(7)
    activation_date_time: datetime = _grpc_helpers.message_field(8)
    expiration_time: datetime = _grpc_helpers.message_field(9)
    price: "MoneyValue" = _grpc_helpers.message_field(10)
    stop_price: "MoneyValue" = _grpc_helpers.message_field(11)
    instrument_uid: str = _grpc_helpers.string_field(12)
    take_profit_type: "TakeProfitType" = _grpc_helpers.message_field(13)
    trailing_data: "StopOrderTrailingData" = _grpc_helpers.message_field(14)
    status: "StopOrderStatusOption" = _grpc_helpers.message_field(15)
    exchange_order_type: "ExchangeOrderType" = _grpc_helpers.message_field(16)
    exchange_order_id: Optional[str] = _grpc_helpers.string_field(17)


@dataclass(eq=False, repr=True)
class StopOrderTrailingData(_grpc_helpers.Message):
    indent: "Quotation" = _grpc_helpers.message_field(1)
    indent_type: "TrailingValueType" = _grpc_helpers.message_field(2)
    spread: "Quotation" = _grpc_helpers.message_field(3)
    spread_type: "TrailingValueType" = _grpc_helpers.message_field(4)
    status: "TrailingStopStatus" = _grpc_helpers.message_field(5)
    price: "Quotation" = _grpc_helpers.message_field(7)
    extr: "Quotation" = _grpc_helpers.message_field(8)


@dataclass(eq=False, repr=True)
class BrokerReportRequest(_grpc_helpers.Message):
    generate_broker_report_request: "GenerateBrokerReportRequest" = (
        _grpc_helpers.message_field(1, group="payload")
    )
    get_broker_report_request: "GetBrokerReportRequest" = _grpc_helpers.message_field(
        2, group="payload"
    )


@dataclass(eq=False, repr=True)
class BrokerReportResponse(_grpc_helpers.Message):
    generate_broker_report_response: "GenerateBrokerReportResponse" = (
        _grpc_helpers.message_field(1, group="payload")
    )
    get_broker_report_response: "GetBrokerReportResponse" = _grpc_helpers.message_field(
        2, group="payload"
    )


@dataclass(eq=False, repr=True)
class GenerateBrokerReportRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class GenerateBrokerReportResponse(_grpc_helpers.Message):
    task_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class GetBrokerReportRequest(_grpc_helpers.Message):
    task_id: str = _grpc_helpers.string_field(1)
    page: Optional[int] = _grpc_helpers.int32_field(2)


@dataclass(eq=False, repr=True)
class GetBrokerReportResponse(_grpc_helpers.Message):
    broker_report: List["BrokerReport"] = _grpc_helpers.message_field(1)
    itemsCount: int = _grpc_helpers.int32_field(2)
    pagesCount: int = _grpc_helpers.int32_field(3)
    page: int = _grpc_helpers.int32_field(4)


@dataclass(eq=False, repr=True)
class BrokerReport(  # pylint:disable=too-many-instance-attributes
    _grpc_helpers.Message
):
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
    price: "MoneyValue" = _grpc_helpers.message_field(11)
    quantity: int = _grpc_helpers.int64_field(12)
    order_amount: "MoneyValue" = _grpc_helpers.message_field(13)
    aci_value: float = _grpc_helpers.double_field(14)
    total_order_amount: "MoneyValue" = _grpc_helpers.message_field(15)
    broker_commission: "MoneyValue" = _grpc_helpers.message_field(16)
    exchange_commission: "MoneyValue" = _grpc_helpers.message_field(17)
    exchange_clearing_commission: "MoneyValue" = _grpc_helpers.message_field(18)
    repo_rate: float = _grpc_helpers.double_field(19)
    party: str = _grpc_helpers.string_field(20)
    clear_value_date: datetime = _grpc_helpers.message_field(21)
    sec_value_date: datetime = _grpc_helpers.message_field(22)
    broker_status: str = _grpc_helpers.string_field(23)
    separate_agreement_type: str = _grpc_helpers.string_field(24)
    separate_agreement_number: str = _grpc_helpers.string_field(25)
    separate_agreement_date: str = _grpc_helpers.string_field(26)
    delivery_type: str = _grpc_helpers.string_field(27)


@dataclass(eq=False, repr=True)
class PositionsFutures(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    blocked: int = _grpc_helpers.int64_field(2)
    balance: int = _grpc_helpers.int64_field(3)
    position_uid: str = _grpc_helpers.string_field(4)
    instrument_uid: str = _grpc_helpers.string_field(5)
    ticker: str = _grpc_helpers.string_field(6)


@dataclass(eq=False, repr=True)
class PositionsOptions(_grpc_helpers.Message):
    position_uid: str = _grpc_helpers.string_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)
    blocked: int = _grpc_helpers.int64_field(11)
    balance: int = _grpc_helpers.int64_field(21)
    ticker: str = _grpc_helpers.string_field(3)


@dataclass(eq=False, repr=True)
class GetDividendsForeignIssuerRequest(_grpc_helpers.Message):
    generate_div_foreign_issuer_report: "GenerateDividendsForeignIssuerReportRequest" = _grpc_helpers.message_field(  # noqa:E501 # pylint:disable=line-too-long
        1, group="payload"
    )
    get_div_foreign_issuer_report: "GetDividendsForeignIssuerReportRequest" = (
        _grpc_helpers.message_field(2, group="payload")
    )


@dataclass(eq=False, repr=True)
class GetDividendsForeignIssuerResponse(_grpc_helpers.Message):
    generate_div_foreign_issuer_report_response: "GenerateDividendsForeignIssuerReportResponse" = _grpc_helpers.message_field(  # noqa:E501 # pylint:disable=line-too-long
        1, group="payload"
    )
    div_foreign_issuer_report: "GetDividendsForeignIssuerReportResponse" = (
        _grpc_helpers.message_field(2, group="payload")
    )


@dataclass(eq=False, repr=True)
class GenerateDividendsForeignIssuerReportRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class GetDividendsForeignIssuerReportRequest(_grpc_helpers.Message):
    task_id: str = _grpc_helpers.string_field(1)
    page: Optional[int] = _grpc_helpers.int32_field(2)


@dataclass(eq=False, repr=True)
class GenerateDividendsForeignIssuerReportResponse(_grpc_helpers.Message):
    task_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class GetDividendsForeignIssuerReportResponse(_grpc_helpers.Message):
    dividends_foreign_issuer_report: List[
        "DividendsForeignIssuerReport"
    ] = _grpc_helpers.message_field(1)
    itemsCount: int = _grpc_helpers.int32_field(2)
    pagesCount: int = _grpc_helpers.int32_field(3)
    page: int = _grpc_helpers.int32_field(4)


@dataclass(eq=False, repr=True)
class DividendsForeignIssuerReport(  # pylint:disable=too-many-instance-attributes
    _grpc_helpers.Message
):
    record_date: datetime = _grpc_helpers.message_field(1)
    payment_date: datetime = _grpc_helpers.message_field(2)
    security_name: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    issuer_country: str = _grpc_helpers.string_field(5)
    quantity: int = _grpc_helpers.int64_field(6)
    dividend: "Quotation" = _grpc_helpers.message_field(7)
    external_commission: "Quotation" = _grpc_helpers.message_field(8)
    dividend_gross: "Quotation" = _grpc_helpers.message_field(9)
    tax: "Quotation" = _grpc_helpers.message_field(10)
    dividend_amount: "Quotation" = _grpc_helpers.message_field(11)
    currency: str = _grpc_helpers.string_field(12)


@dataclass(eq=False, repr=True)
class PortfolioStreamRequest(_grpc_helpers.Message):
    accounts: List[str] = _grpc_helpers.message_field(1)
    ping_settings: "PingDelaySettings" = _grpc_helpers.message_field(15)


@dataclass(eq=False, repr=True)
class PortfolioStreamResponse(_grpc_helpers.Message):
    subscriptions: "PortfolioSubscriptionResult" = _grpc_helpers.message_field(
        1, group="payload"
    )
    portfolio: "PortfolioResponse" = _grpc_helpers.message_field(2, group="payload")
    ping: "Ping" = _grpc_helpers.message_field(3, group="payload")


@dataclass(eq=False, repr=True)
class PortfolioSubscriptionResult(_grpc_helpers.Message):
    accounts: List["AccountSubscriptionStatus"] = _grpc_helpers.message_field(1)
    tracking_id: str = _grpc_helpers.string_field(7)
    stream_id: str = _grpc_helpers.string_field(8)


@dataclass(eq=False, repr=True)
class AccountSubscriptionStatus(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    subscription_status: "PortfolioSubscriptionStatus" = _grpc_helpers.message_field(6)


@dataclass(eq=False, repr=True)
class GetOperationsByCursorRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    instrument_id: Optional[str] = _grpc_helpers.string_field(2)
    from_: Optional[datetime] = _grpc_helpers.message_field(6)
    to: Optional[datetime] = _grpc_helpers.message_field(7)
    cursor: Optional[str] = _grpc_helpers.string_field(11)
    limit: Optional[int] = _grpc_helpers.int32_field(12)
    operation_types: List["OperationType"] = _grpc_helpers.message_field(13)
    state: Optional["OperationState"] = _grpc_helpers.message_field(14)
    without_commissions: Optional[bool] = _grpc_helpers.bool_field(15)
    without_trades: Optional[bool] = _grpc_helpers.bool_field(16)
    without_overnights: Optional[bool] = _grpc_helpers.bool_field(17)


@dataclass(eq=False, repr=True)
class GetOperationsByCursorResponse(_grpc_helpers.Message):
    has_next: bool = _grpc_helpers.bool_field(1)
    next_cursor: str = _grpc_helpers.string_field(2)
    items: List["OperationItem"] = _grpc_helpers.message_field(6)


@dataclass(eq=False, repr=True)
class OperationItem(_grpc_helpers.Message):
    cursor: str = _grpc_helpers.string_field(1)
    broker_account_id: str = _grpc_helpers.string_field(6)
    id: str = _grpc_helpers.string_field(16)
    parent_operation_id: str = _grpc_helpers.string_field(17)
    name: str = _grpc_helpers.string_field(18)
    date: datetime = _grpc_helpers.message_field(21)
    type: "OperationType" = _grpc_helpers.enum_field(22)
    description: str = _grpc_helpers.string_field(23)
    state: "OperationState" = _grpc_helpers.message_field(24)
    instrument_uid: str = _grpc_helpers.string_field(31)
    figi: str = _grpc_helpers.string_field(32)
    instrument_type: str = _grpc_helpers.string_field(33)
    instrument_kind: "InstrumentType" = _grpc_helpers.enum_field(34)
    position_uid: str = _grpc_helpers.string_field(35)
    payment: "MoneyValue" = _grpc_helpers.message_field(41)
    price: "MoneyValue" = _grpc_helpers.message_field(42)
    commission: "MoneyValue" = _grpc_helpers.message_field(43)
    yield_: "MoneyValue" = _grpc_helpers.message_field(44)
    yield_relative: "Quotation" = _grpc_helpers.message_field(45)
    accrued_int: "MoneyValue" = _grpc_helpers.message_field(46)
    quantity: int = _grpc_helpers.int64_field(51)
    quantity_rest: int = _grpc_helpers.int64_field(52)
    quantity_done: int = _grpc_helpers.int64_field(53)
    cancel_date_time: datetime = _grpc_helpers.message_field(56)
    cancel_reason: str = _grpc_helpers.string_field(57)
    trades_info: "OperationItemTrades" = _grpc_helpers.message_field(61)
    asset_uid: str = _grpc_helpers.string_field(64)
    child_operations: List["ChildOperationItem"] = _grpc_helpers.message_field(65)


@dataclass(eq=False, repr=True)
class OperationItemTrades(_grpc_helpers.Message):
    trades: List["OperationItemTrade"] = _grpc_helpers.message_field(6)


@dataclass(eq=False, repr=True)
class OperationItemTrade(_grpc_helpers.Message):
    num: str = _grpc_helpers.string_field(1)
    date: datetime = _grpc_helpers.message_field(6)
    quantity: int = _grpc_helpers.int64_field(11)
    price: "MoneyValue" = _grpc_helpers.message_field(16)
    yield_: "MoneyValue" = _grpc_helpers.message_field(21)
    yield_relative: "Quotation" = _grpc_helpers.message_field(22)


@dataclass(eq=False, repr=True)
class PositionsStreamRequest(_grpc_helpers.Message):
    accounts: List[str] = _grpc_helpers.string_field(1)
    ping_settings: "PingDelaySettings" = _grpc_helpers.message_field(15)
    with_initial_positions: bool = _grpc_helpers.bool_field(3)


@dataclass(eq=False, repr=True)
class PositionsStreamResponse(_grpc_helpers.Message):
    subscriptions: "PositionsSubscriptionResult" = _grpc_helpers.message_field(
        1, group="payload"
    )
    position: "PositionData" = _grpc_helpers.message_field(2, group="payload")
    ping: "Ping" = _grpc_helpers.message_field(3, group="payload")
    initial_positions: "PositionsResponse" = _grpc_helpers.message_field(
        5, group="payload"
    )


@dataclass(eq=False, repr=True)
class PositionsSubscriptionResult(_grpc_helpers.Message):
    accounts: List["PositionsSubscriptionStatus"] = _grpc_helpers.message_field(1)
    tracking_id: str = _grpc_helpers.string_field(7)
    stream_id: str = _grpc_helpers.string_field(8)


@dataclass(eq=False, repr=True)
class PositionsSubscriptionStatus(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    subscription_status: "PositionsAccountSubscriptionStatus" = (
        _grpc_helpers.message_field(6)
    )


@dataclass(eq=False, repr=True)
class PositionData(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    money: List["PositionsMoney"] = _grpc_helpers.message_field(2)
    securities: List["PositionsSecurities"] = _grpc_helpers.message_field(3)
    futures: List["PositionsFutures"] = _grpc_helpers.message_field(4)
    options: List["PositionsOptions"] = _grpc_helpers.message_field(5)
    date: datetime = _grpc_helpers.message_field(6)


@dataclass(eq=False, repr=True)
class PositionsMoney(_grpc_helpers.Message):
    available_value: "MoneyValue" = _grpc_helpers.message_field(1)
    blocked_value: "MoneyValue" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class Page(_grpc_helpers.Message):
    limit: int = _grpc_helpers.int32_field(1)
    page_number: int = _grpc_helpers.int32_field(2)


@dataclass(eq=False, repr=True)
class PageResponse(_grpc_helpers.Message):
    limit: int = _grpc_helpers.int32_field(1)
    page_number: int = _grpc_helpers.int32_field(2)
    total_count: int = _grpc_helpers.int32_field(3)


@dataclass(eq=False, repr=True)
class ResponseMetadata(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(42)
    server_time: datetime = _grpc_helpers.message_field(43)


@dataclass(eq=False, repr=True)
class BrandData(_grpc_helpers.Message):
    logo_name: str = _grpc_helpers.string_field(1)
    logo_base_color: str = _grpc_helpers.string_field(2)
    text_color: str = _grpc_helpers.string_field(3)


@dataclass(eq=False, repr=True)
class GetAssetFundamentalsRequest(_grpc_helpers.Message):
    assets: List[str] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetAssetFundamentalsResponse(_grpc_helpers.Message):
    fundamentals: List["StatisticResponse"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class StatisticResponse(_grpc_helpers.Message):
    asset_uid: str = _grpc_helpers.string_field(1)
    currency: str = _grpc_helpers.string_field(2)
    market_capitalization: float = _grpc_helpers.double_field(3)
    high_price_last_52_weeks: float = _grpc_helpers.double_field(4)
    low_price_last_52_weeks: float = _grpc_helpers.double_field(5)
    average_daily_volume_last_10_days: float = _grpc_helpers.double_field(6)
    average_daily_volume_last_4_weeks: float = _grpc_helpers.double_field(7)
    beta: float = _grpc_helpers.double_field(8)
    free_float: float = _grpc_helpers.double_field(9)
    forward_annual_dividend_yield: float = _grpc_helpers.double_field(10)
    shares_outstanding: float = _grpc_helpers.double_field(11)
    revenue_ttm: float = _grpc_helpers.double_field(12)
    ebitda_ttm: float = _grpc_helpers.double_field(13)
    net_income_ttm: float = _grpc_helpers.double_field(14)
    eps_ttm: float = _grpc_helpers.double_field(15)
    diluted_eps_ttm: float = _grpc_helpers.double_field(16)
    free_cash_flow_ttm: float = _grpc_helpers.double_field(17)
    five_year_annual_revenue_growth_rate: float = _grpc_helpers.double_field(18)
    three_year_annual_revenue_growth_rate: float = _grpc_helpers.double_field(19)
    pe_ratio_ttm: float = _grpc_helpers.double_field(20)
    price_to_sales_ttm: float = _grpc_helpers.double_field(21)
    price_to_book_ttm: float = _grpc_helpers.double_field(22)
    price_to_free_cash_flow_ttm: float = _grpc_helpers.double_field(23)
    total_enterprise_value_mrq: float = _grpc_helpers.double_field(24)
    ev_to_ebitda_mrq: float = _grpc_helpers.double_field(25)
    net_margin_mrq: float = _grpc_helpers.double_field(26)
    net_interest_margin_mrq: float = _grpc_helpers.double_field(27)
    roe: float = _grpc_helpers.double_field(28)
    roa: float = _grpc_helpers.double_field(29)
    roic: float = _grpc_helpers.double_field(30)
    total_debt_mrq: float = _grpc_helpers.double_field(31)
    total_debt_to_equity_mrq: float = _grpc_helpers.double_field(32)
    total_debt_to_ebitda_mrq: float = _grpc_helpers.double_field(33)
    free_cash_flow_to_price: float = _grpc_helpers.double_field(34)
    net_debt_to_ebitda: float = _grpc_helpers.double_field(35)
    current_ratio_mrq: float = _grpc_helpers.double_field(36)
    fixed_charge_coverage_ratio_fy: float = _grpc_helpers.double_field(37)
    dividend_yield_daily_ttm: float = _grpc_helpers.double_field(38)
    dividend_rate_ttm: float = _grpc_helpers.double_field(39)
    dividends_per_share: float = _grpc_helpers.double_field(40)
    five_years_average_dividend_yield: float = _grpc_helpers.double_field(41)
    five_year_annual_dividend_growth_rate: float = _grpc_helpers.double_field(42)
    dividend_payout_ratio_fy: float = _grpc_helpers.double_field(43)
    buy_back_ttm: float = _grpc_helpers.double_field(44)
    one_year_annual_revenue_growth_rate: float = _grpc_helpers.double_field(45)
    domicile_indicator_code: str = _grpc_helpers.string_field(46)
    adr_to_common_share_ratio: float = _grpc_helpers.double_field(47)
    number_of_employees: float = _grpc_helpers.double_field(48)
    ex_dividend_date: datetime = _grpc_helpers.message_field(49)
    fiscal_period_start_date: datetime = _grpc_helpers.message_field(50)
    fiscal_period_end_date: datetime = _grpc_helpers.message_field(51)
    revenue_change_five_years: float = _grpc_helpers.double_field(53)
    eps_change_five_years: float = _grpc_helpers.double_field(54)
    ebitda_change_five_years: float = _grpc_helpers.double_field(55)
    total_debt_change_five_years: float = _grpc_helpers.double_field(56)
    ev_to_sales: float = _grpc_helpers.double_field(57)


@dataclass(eq=False, repr=True)
class GetAssetReportsRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class GetAssetReportsEvent(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)
    report_date: datetime = _grpc_helpers.message_field(2)
    period_year: datetime = _grpc_helpers.message_field(3)
    period_num: datetime = _grpc_helpers.message_field(4)
    period_type: "AssetReportPeriodType" = _grpc_helpers.enum_field(5)
    created_at: datetime = _grpc_helpers.message_field(6)


@dataclass(eq=False, repr=True)
class GetAssetReportsResponse(_grpc_helpers.Message):
    events: List["GetAssetReportsEvent"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class GetConsensusForecastsRequest(_grpc_helpers.Message):
    paging: Optional["Page"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class ConsensusForecastsItem(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    asset_uid: str = _grpc_helpers.string_field(2)
    created_at: datetime = _grpc_helpers.message_field(3)
    best_target_price: "Quotation" = _grpc_helpers.message_field(4)
    best_target_low: "Quotation" = _grpc_helpers.message_field(5)
    best_target_high: "Quotation" = _grpc_helpers.message_field(6)
    total_buy_recommend: int = _grpc_helpers.int32_field(7)
    total_hold_recommend: int = _grpc_helpers.int32_field(8)
    total_sell_recommend: int = _grpc_helpers.int32_field(9)
    currency: str = _grpc_helpers.string_field(10)
    consensus: "Recommendation" = _grpc_helpers.message_field(11)
    prognosis_date: datetime = _grpc_helpers.message_field(12)


@dataclass(eq=False, repr=True)
class GetConsensusForecastsResponse(_grpc_helpers.Message):
    items: List["ConsensusForecastsItem"] = _grpc_helpers.message_field(1)
    page: "PageResponse" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class GetForecastRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class TargetItem(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    company: str = _grpc_helpers.string_field(3)
    recommendation: "Recommendation" = _grpc_helpers.message_field(4)
    recommendation_date: datetime = _grpc_helpers.message_field(5)
    currency: str = _grpc_helpers.string_field(6)
    current_price: "Quotation" = _grpc_helpers.message_field(7)
    target_price: "Quotation" = _grpc_helpers.message_field(8)
    price_change: "Quotation" = _grpc_helpers.message_field(9)
    price_change_rel: "Quotation" = _grpc_helpers.message_field(10)
    show_name: str = _grpc_helpers.string_field(11)


@dataclass(eq=False, repr=True)
class ConsensusItem(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    recommendation: "Recommendation" = _grpc_helpers.message_field(3)
    currency: str = _grpc_helpers.string_field(4)
    current_price: "Quotation" = _grpc_helpers.message_field(5)
    consensus: "Quotation" = _grpc_helpers.message_field(6)
    min_target: "Quotation" = _grpc_helpers.message_field(7)
    max_target: "Quotation" = _grpc_helpers.message_field(8)
    price_change: "Quotation" = _grpc_helpers.message_field(9)
    price_change_rel: "Quotation" = _grpc_helpers.message_field(10)


@dataclass(eq=False, repr=True)
class GetForecastResponse(_grpc_helpers.Message):
    targets: List["TargetItem"] = _grpc_helpers.message_field(1)
    consensus: "ConsensusItem" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class RiskRatesRequest(_grpc_helpers.Message):
    instrument_id: List[str] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class RiskRatesResponse(_grpc_helpers.Message):
    instrument_risk_rates: List["RiskRateResult"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class RiskRateResult(_grpc_helpers.Message):
    instrument_uid: str = _grpc_helpers.string_field(1)
    short_risk_rate: Optional["RiskRate"] = _grpc_helpers.message_field(2)
    long_risk_rate: Optional["RiskRate"] = _grpc_helpers.message_field(3)
    short_risk_rates: List["RiskRate"] = _grpc_helpers.message_field(5)
    long_risk_rates: List["RiskRate"] = _grpc_helpers.message_field(6)
    error: Optional[str] = _grpc_helpers.string_field(9)


@dataclass(eq=False, repr=True)
class RiskRate(_grpc_helpers.Message):
    risk_level_code: str = _grpc_helpers.string_field(2)
    value: Quotation = _grpc_helpers.message_field(5)


@dataclass(eq=False, repr=True)
class TimeInterval(_grpc_helpers.Message):
    start_ts: datetime = _grpc_helpers.message_field(1)
    end_ts: datetime = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class TradingInterval(_grpc_helpers.Message):
    type: str = _grpc_helpers.string_field(1)
    interval: "TimeInterval" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class GetMaxLotsRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)
    price: Optional["Quotation"] = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class GetMaxLotsResponse(_grpc_helpers.Message):
    currency: str = _grpc_helpers.string_field(1)
    buy_limits: "BuyLimitsView" = _grpc_helpers.message_field(2)
    buy_margin_limits: "BuyLimitsView" = _grpc_helpers.message_field(3)
    sell_limits: "SellLimitsView" = _grpc_helpers.message_field(4)
    sell_margin_limits: "SellLimitsView" = _grpc_helpers.message_field(5)


@dataclass(eq=False, repr=True)
class BuyLimitsView(_grpc_helpers.Message):
    buy_money_amount: "Quotation" = _grpc_helpers.message_field(1)
    buy_max_lots: int = _grpc_helpers.int64_field(2)
    buy_max_market_lots: int = _grpc_helpers.int64_field(3)


@dataclass(eq=False, repr=True)
class SellLimitsView(_grpc_helpers.Message):
    sell_max_lots: int = _grpc_helpers.int64_field(1)


@dataclass(eq=False, repr=True)
class GetOrderPriceRequest(_grpc_helpers.Message):
    account_id: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)
    price: "Quotation" = _grpc_helpers.message_field(3)
    direction: "OrderDirection" = _grpc_helpers.message_field(12)
    quantity: int = _grpc_helpers.int64_field(13)


@dataclass(eq=False, repr=True)
class GetOrderPriceResponse(_grpc_helpers.Message):
    total_order_amount: "MoneyValue" = _grpc_helpers.message_field(1)
    initial_order_amount: "MoneyValue" = _grpc_helpers.message_field(5)
    lots_requested: int = _grpc_helpers.int64_field(3)
    executed_commission: "MoneyValue" = _grpc_helpers.message_field(7)
    executed_commission_rub: "MoneyValue" = _grpc_helpers.message_field(8)
    service_commission: "MoneyValue" = _grpc_helpers.message_field(9)
    deal_commission: "MoneyValue" = _grpc_helpers.message_field(10)
    extra_bond: "ExtraBond" = _grpc_helpers.message_field(12, group="instrument_extra")
    extra_future: "ExtraFuture" = _grpc_helpers.message_field(
        13, group="instrument_extra"
    )


@dataclass(eq=False, repr=True)
class OrderStateStreamRequest(_grpc_helpers.Message):
    accounts: List[str] = _grpc_helpers.message_field(1)
    ping_delay_millis: Optional[int] = _grpc_helpers.int32_field(15)


@dataclass(eq=False, repr=True)
class ErrorDetail(_grpc_helpers.Message):
    code: str = _grpc_helpers.string_field(1)
    message: str = _grpc_helpers.string_field(3)


@dataclass(eq=False, repr=True)
class SubscriptionResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    status: ResultSubscriptionStatus = _grpc_helpers.message_field(2)
    stream_id: str = _grpc_helpers.message_field(4)
    accounts: List[str] = _grpc_helpers.message_field(5)
    error: Optional[ErrorDetail] = _grpc_helpers.message_field(7)


@dataclass(eq=False, repr=True)
class OrderStateStreamOrderState(_grpc_helpers.Message):
    order_id: str = _grpc_helpers.string_field(1)
    order_request_id: Optional[str] = _grpc_helpers.string_field(2)
    client_code: str = _grpc_helpers.string_field(3)
    created_at: datetime = _grpc_helpers.message_field(4)
    execution_report_status: OrderExecutionReportStatus = _grpc_helpers.message_field(5)
    status_info: Optional[StatusCauseInfo] = _grpc_helpers.message_field(6)
    ticker: str = _grpc_helpers.string_field(7)
    class_code: str = _grpc_helpers.string_field(8)
    lot_size: int = _grpc_helpers.int32_field(9)
    direction: OrderDirection = _grpc_helpers.message_field(10)
    time_in_force: TimeInForceType = _grpc_helpers.message_field(11)
    order_type: OrderType = _grpc_helpers.message_field(12)
    account_id: str = _grpc_helpers.string_field(13)
    initial_order_price: MoneyValue = _grpc_helpers.message_field(22)
    order_price: MoneyValue = _grpc_helpers.message_field(23)
    amount: Optional[MoneyValue] = _grpc_helpers.message_field(24)
    executed_order_price: MoneyValue = _grpc_helpers.message_field(25)
    currency: str = _grpc_helpers.string_field(26)
    lots_requested: int = _grpc_helpers.int64_field(27)
    lots_executed: int = _grpc_helpers.int64_field(28)
    lots_left: int = _grpc_helpers.int64_field(29)
    lots_cancelled: int = _grpc_helpers.int64_field(30)
    marker: Optional[MarkerType] = _grpc_helpers.message_field(31)
    trades: List[OrderTrade] = _grpc_helpers.message_field(33)
    completion_time: datetime = _grpc_helpers.message_field(35)
    exchange: str = _grpc_helpers.string_field(36)
    instrument_uid: str = _grpc_helpers.string_field(41)


@dataclass(eq=False, repr=True)
class OrderStateStreamResponse(_grpc_helpers.Message):
    order_state: "OrderStateStreamOrderState" = _grpc_helpers.message_field(
        1, group="payload"
    )
    ping: "Ping" = _grpc_helpers.message_field(2, group="payload")
    subscription: "SubscriptionResponse" = _grpc_helpers.message_field(
        3, group="payload"
    )


@dataclass(eq=False, repr=True)
class ExtraBond(_grpc_helpers.Message):
    aci_value: "MoneyValue" = _grpc_helpers.message_field(2)
    nominal_conversion_rate: "Quotation" = _grpc_helpers.message_field(3)


@dataclass(eq=False, repr=True)
class ExtraFuture(_grpc_helpers.Message):
    initial_margin: "MoneyValue" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class GetStrategiesRequest(_grpc_helpers.Message):
    strategy_id: Optional[str] = _grpc_helpers.string_field(1)


@dataclass(eq=False, repr=True)
class GetStrategiesResponse(_grpc_helpers.Message):
    strategies: List["Strategy"] = _grpc_helpers.message_field(1)


@dataclass(eq=False, repr=True)
class Strategy(_grpc_helpers.Message):
    strategy_id: str = _grpc_helpers.string_field(1)
    strategy_name: str = _grpc_helpers.string_field(2)
    strategy_description: Optional[str] = _grpc_helpers.string_field(3)
    strategy_url: Optional[str] = _grpc_helpers.string_field(4)
    strategy_type: "StrategyType" = _grpc_helpers.message_field(5)
    active_signals: int = _grpc_helpers.int32_field(6)
    total_signals: int = _grpc_helpers.int32_field(7)
    time_in_position: int = _grpc_helpers.int64_field(8)
    average_signal_yield: "Quotation" = _grpc_helpers.string_field(9)
    average_signal_yield_year: "Quotation" = _grpc_helpers.string_field(10)
    yield_: "Quotation" = _grpc_helpers.string_field(11)
    yield_year: "Quotation" = _grpc_helpers.string_field(12)


@dataclass(eq=False, repr=True)
class GetSignalsRequest(_grpc_helpers.Message):
    signal_id: Optional[str] = _grpc_helpers.string_field(1)
    strategy_id: Optional[str] = _grpc_helpers.string_field(2)
    strategy_type: Optional["StrategyType"] = _grpc_helpers.message_field(3)
    instrument_uid: Optional[str] = _grpc_helpers.string_field(4)
    from_: Optional[datetime] = _grpc_helpers.message_field(5)
    to: Optional[datetime] = _grpc_helpers.message_field(6)
    direction: Optional["SignalDirection"] = _grpc_helpers.message_field(7)
    active: Optional[SignalState] = _grpc_helpers.message_field(8)
    paging: Optional["Page"] = _grpc_helpers.message_field(9)


@dataclass(eq=False, repr=True)
class GetSignalsResponse(_grpc_helpers.Message):
    signals: List["Signal"] = _grpc_helpers.message_field(1)
    paging: "PageResponse" = _grpc_helpers.message_field(2)


@dataclass(eq=False, repr=True)
class Signal(_grpc_helpers.Message):
    signal_id: str = _grpc_helpers.string_field(1)
    strategy_id: str = _grpc_helpers.string_field(2)
    strategy_name: str = _grpc_helpers.string_field(3)
    instrument_uid: str = _grpc_helpers.string_field(4)
    create_dt: datetime = _grpc_helpers.message_field(5)
    direction: "SignalDirection" = _grpc_helpers.message_field(6)
    initial_price: "Quotation" = _grpc_helpers.message_field(7)
    info: Optional[str] = _grpc_helpers.string_field(8)
    name: str = _grpc_helpers.string_field(9)
    target_price: "Quotation" = _grpc_helpers.message_field(10)
    end_dt: datetime = _grpc_helpers.message_field(11)
    probability: int = _grpc_helpers.int32_field(12)
    stoploss: "Quotation" = _grpc_helpers.message_field(13)
    close_price: "Quotation" = _grpc_helpers.message_field(14)
    close_dt: Optional[datetime] = _grpc_helpers.message_field(15)
