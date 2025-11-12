from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest import _grpc_helpers
from tinkoff.invest._errors import handle_aio_request_error, handle_request_error
from tinkoff.invest.grpc import instruments_pb2, instruments_pb2_grpc
from tinkoff.invest.grpc.common import (
    BrandData,
    InstrumentStatus,
    InstrumentType,
    MoneyValue,
    Page,
    PageResponse,
    Quotation,
    RealExchange,
    SecurityTradingStatus,
)
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


class CouponType(IntEnum):
    COUPON_TYPE_UNSPECIFIED = 0
    COUPON_TYPE_CONSTANT = 1
    COUPON_TYPE_FLOATING = 2
    COUPON_TYPE_DISCOUNT = 3
    COUPON_TYPE_MORTGAGE = 4
    COUPON_TYPE_FIX = 5
    COUPON_TYPE_VARIABLE = 6
    COUPON_TYPE_OTHER = 7


class OptionDirection(IntEnum):
    OPTION_DIRECTION_UNSPECIFIED = 0
    OPTION_DIRECTION_PUT = 1
    OPTION_DIRECTION_CALL = 2


class OptionPaymentType(IntEnum):
    OPTION_PAYMENT_TYPE_UNSPECIFIED = 0
    OPTION_PAYMENT_TYPE_PREMIUM = 1
    OPTION_PAYMENT_TYPE_MARGINAL = 2


class OptionStyle(IntEnum):
    OPTION_STYLE_UNSPECIFIED = 0
    OPTION_STYLE_AMERICAN = 1
    OPTION_STYLE_EUROPEAN = 2


class OptionSettlementType(IntEnum):
    OPTION_EXECUTION_TYPE_UNSPECIFIED = 0
    OPTION_EXECUTION_TYPE_PHYSICAL_DELIVERY = 1
    OPTION_EXECUTION_TYPE_CASH_SETTLEMENT = 2


class InstrumentIdType(IntEnum):
    INSTRUMENT_ID_UNSPECIFIED = 0
    INSTRUMENT_ID_TYPE_FIGI = 1
    INSTRUMENT_ID_TYPE_TICKER = 2
    INSTRUMENT_ID_TYPE_UID = 3
    INSTRUMENT_ID_TYPE_POSITION_UID = 4


class ShareType(IntEnum):
    SHARE_TYPE_UNSPECIFIED = 0
    SHARE_TYPE_COMMON = 1
    SHARE_TYPE_PREFERRED = 2
    SHARE_TYPE_ADR = 3
    SHARE_TYPE_GDR = 4
    SHARE_TYPE_MLP = 5
    SHARE_TYPE_NY_REG_SHRS = 6
    SHARE_TYPE_CLOSED_END_FUND = 7
    SHARE_TYPE_REIT = 8


class AssetType(IntEnum):
    ASSET_TYPE_UNSPECIFIED = 0
    ASSET_TYPE_CURRENCY = 1
    ASSET_TYPE_COMMODITY = 2
    ASSET_TYPE_INDEX = 3
    ASSET_TYPE_SECURITY = 4


class StructuredProductType(IntEnum):
    SP_TYPE_UNSPECIFIED = 0
    SP_TYPE_DELIVERABLE = 1
    SP_TYPE_NON_DELIVERABLE = 2


class EditFavoritesActionType(IntEnum):
    EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED = 0
    EDIT_FAVORITES_ACTION_TYPE_ADD = 1
    EDIT_FAVORITES_ACTION_TYPE_DEL = 2


class Recommendation(IntEnum):
    RECOMMENDATION_UNSPECIFIED = 0
    RECOMMENDATION_BUY = 1
    RECOMMENDATION_HOLD = 2
    RECOMMENDATION_SELL = 3


class RiskLevel(IntEnum):
    RISK_LEVEL_UNSPECIFIED = 0
    RISK_LEVEL_LOW = 1
    RISK_LEVEL_MODERATE = 2
    RISK_LEVEL_HIGH = 3


class BondType(IntEnum):
    BOND_TYPE_UNSPECIFIED = 0
    BOND_TYPE_REPLACED = 1


class InstrumentExchangeType(IntEnum):
    INSTRUMENT_EXCHANGE_UNSPECIFIED = 0
    INSTRUMENT_EXCHANGE_DEALER = 1


@dataclass
class TradingSchedulesRequest(_grpc_helpers.Message):
    exchange: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    from_: Optional[datetime] = _grpc_helpers.message_field(2, optional=True)
    to: Optional[datetime] = _grpc_helpers.message_field(3, optional=True)


@dataclass
class TradingSchedulesResponse(_grpc_helpers.Message):
    exchanges: List['TradingSchedule'] = _grpc_helpers.message_field(1)


@dataclass
class TradingSchedule(_grpc_helpers.Message):
    exchange: str = _grpc_helpers.string_field(1)
    days: List['TradingDay'] = _grpc_helpers.message_field(2)


@dataclass
class TradingDay(_grpc_helpers.Message):
    date: datetime = _grpc_helpers.message_field(1)
    is_trading_day: bool = _grpc_helpers.bool_field(2)
    start_time: datetime = _grpc_helpers.message_field(3)
    end_time: datetime = _grpc_helpers.message_field(4)
    opening_auction_start_time: datetime = _grpc_helpers.message_field(7)
    closing_auction_end_time: datetime = _grpc_helpers.message_field(8)
    evening_opening_auction_start_time: datetime = _grpc_helpers.message_field(
        9)
    evening_start_time: datetime = _grpc_helpers.message_field(10)
    evening_end_time: datetime = _grpc_helpers.message_field(11)
    clearing_start_time: datetime = _grpc_helpers.message_field(12)
    clearing_end_time: datetime = _grpc_helpers.message_field(13)
    premarket_start_time: datetime = _grpc_helpers.message_field(14)
    premarket_end_time: datetime = _grpc_helpers.message_field(15)
    closing_auction_start_time: datetime = _grpc_helpers.message_field(16)
    opening_auction_end_time: datetime = _grpc_helpers.message_field(17)
    intervals: List['TradingInterval'] = _grpc_helpers.message_field(18)


@dataclass
class InstrumentRequest(_grpc_helpers.Message):
    id_type: 'InstrumentIdType' = _grpc_helpers.message_field(1)
    class_code: Optional[str] = _grpc_helpers.string_field(2, optional=True)
    id: str = _grpc_helpers.string_field(3)


@dataclass
class InstrumentsRequest(_grpc_helpers.Message):
    instrument_status: Optional['InstrumentStatus'
        ] = _grpc_helpers.message_field(1, optional=True)
    instrument_exchange: Optional['InstrumentExchangeType'
        ] = _grpc_helpers.message_field(2, optional=True)


@dataclass
class FilterOptionsRequest(_grpc_helpers.Message):
    basic_asset_uid: Optional[str] = _grpc_helpers.string_field(1, optional
        =True)
    basic_asset_position_uid: Optional[str] = _grpc_helpers.string_field(2,
        optional=True)


@dataclass
class BondResponse(_grpc_helpers.Message):
    instrument: 'Bond' = _grpc_helpers.message_field(1)


@dataclass
class BondsResponse(_grpc_helpers.Message):
    instruments: List['Bond'] = _grpc_helpers.message_field(1)


@dataclass
class GetBondCouponsRequest(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    from_: Optional[datetime] = _grpc_helpers.message_field(2, optional=True)
    to: Optional[datetime] = _grpc_helpers.message_field(3, optional=True)
    instrument_id: str = _grpc_helpers.string_field(4)


@dataclass
class GetBondCouponsResponse(_grpc_helpers.Message):
    events: List['Coupon'] = _grpc_helpers.message_field(1)


@dataclass
class GetBondEventsRequest(_grpc_helpers.Message):
    from_: Optional[datetime] = _grpc_helpers.message_field(2, optional=True)
    to: Optional[datetime] = _grpc_helpers.message_field(3, optional=True)
    instrument_id: str = _grpc_helpers.string_field(4)
    type: 'EventType' = _grpc_helpers.message_field(5)


    class EventType(IntEnum):
        EVENT_TYPE_UNSPECIFIED = 0
        EVENT_TYPE_CPN = 1
        EVENT_TYPE_CALL = 2
        EVENT_TYPE_MTY = 3
        EVENT_TYPE_CONV = 4


@dataclass
class GetBondEventsResponse(_grpc_helpers.Message):
    events: List['BondEvent'] = _grpc_helpers.message_field(1)


    @dataclass
    class BondEvent(_grpc_helpers.Message):
        instrument_id: str = _grpc_helpers.string_field(2)
        event_number: int = _grpc_helpers.int32_field(3)
        event_date: datetime = _grpc_helpers.message_field(4)
        event_type: 'GetBondEventsRequest.EventType' = (_grpc_helpers.
            message_field(5))
        event_total_vol: 'Quotation' = _grpc_helpers.message_field(6)
        fix_date: datetime = _grpc_helpers.message_field(7)
        rate_date: datetime = _grpc_helpers.message_field(8)
        default_date: datetime = _grpc_helpers.message_field(9)
        real_pay_date: datetime = _grpc_helpers.message_field(10)
        pay_date: datetime = _grpc_helpers.message_field(11)
        pay_one_bond: 'MoneyValue' = _grpc_helpers.message_field(12)
        money_flow_val: 'MoneyValue' = _grpc_helpers.message_field(13)
        execution: str = _grpc_helpers.string_field(14)
        operation_type: str = _grpc_helpers.string_field(15)
        value: 'Quotation' = _grpc_helpers.message_field(16)
        note: str = _grpc_helpers.string_field(17)
        convert_to_fin_tool_id: str = _grpc_helpers.string_field(18)
        coupon_start_date: datetime = _grpc_helpers.message_field(19)
        coupon_end_date: datetime = _grpc_helpers.message_field(20)
        coupon_period: int = _grpc_helpers.int32_field(21)
        coupon_interest_rate: 'Quotation' = _grpc_helpers.message_field(22)


@dataclass
class Coupon(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    coupon_date: datetime = _grpc_helpers.message_field(2)
    coupon_number: int = _grpc_helpers.int64_field(3)
    fix_date: datetime = _grpc_helpers.message_field(4)
    pay_one_bond: 'MoneyValue' = _grpc_helpers.message_field(5)
    coupon_type: 'CouponType' = _grpc_helpers.message_field(6)
    coupon_start_date: datetime = _grpc_helpers.message_field(7)
    coupon_end_date: datetime = _grpc_helpers.message_field(8)
    coupon_period: int = _grpc_helpers.int32_field(9)


@dataclass
class CurrencyResponse(_grpc_helpers.Message):
    instrument: 'Currency' = _grpc_helpers.message_field(1)


@dataclass
class CurrenciesResponse(_grpc_helpers.Message):
    instruments: List['Currency'] = _grpc_helpers.message_field(1)


@dataclass
class EtfResponse(_grpc_helpers.Message):
    instrument: 'Etf' = _grpc_helpers.message_field(1)


@dataclass
class EtfsResponse(_grpc_helpers.Message):
    instruments: List['Etf'] = _grpc_helpers.message_field(1)


@dataclass
class FutureResponse(_grpc_helpers.Message):
    instrument: 'Future' = _grpc_helpers.message_field(1)


@dataclass
class FuturesResponse(_grpc_helpers.Message):
    instruments: List['Future'] = _grpc_helpers.message_field(1)


@dataclass
class OptionResponse(_grpc_helpers.Message):
    instrument: 'Option' = _grpc_helpers.message_field(1)


@dataclass
class OptionsResponse(_grpc_helpers.Message):
    instruments: List['Option'] = _grpc_helpers.message_field(1)


@dataclass
class Option(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    position_uid: str = _grpc_helpers.string_field(2)
    ticker: str = _grpc_helpers.string_field(3)
    class_code: str = _grpc_helpers.string_field(4)
    basic_asset_position_uid: str = _grpc_helpers.string_field(5)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(21)
    real_exchange: 'RealExchange' = _grpc_helpers.message_field(31)
    direction: 'OptionDirection' = _grpc_helpers.message_field(41)
    payment_type: 'OptionPaymentType' = _grpc_helpers.message_field(42)
    style: 'OptionStyle' = _grpc_helpers.message_field(43)
    settlement_type: 'OptionSettlementType' = _grpc_helpers.message_field(44)
    name: str = _grpc_helpers.string_field(101)
    currency: str = _grpc_helpers.string_field(111)
    settlement_currency: str = _grpc_helpers.string_field(112)
    asset_type: str = _grpc_helpers.string_field(131)
    basic_asset: str = _grpc_helpers.string_field(132)
    exchange: str = _grpc_helpers.string_field(141)
    country_of_risk: str = _grpc_helpers.string_field(151)
    country_of_risk_name: str = _grpc_helpers.string_field(152)
    sector: str = _grpc_helpers.string_field(161)
    brand: 'BrandData' = _grpc_helpers.message_field(162)
    lot: int = _grpc_helpers.int32_field(201)
    basic_asset_size: 'Quotation' = _grpc_helpers.message_field(211)
    klong: 'Quotation' = _grpc_helpers.message_field(221)
    kshort: 'Quotation' = _grpc_helpers.message_field(222)
    dlong: 'Quotation' = _grpc_helpers.message_field(223)
    dshort: 'Quotation' = _grpc_helpers.message_field(224)
    dlong_min: 'Quotation' = _grpc_helpers.message_field(225)
    dshort_min: 'Quotation' = _grpc_helpers.message_field(226)
    min_price_increment: 'Quotation' = _grpc_helpers.message_field(231)
    strike_price: 'MoneyValue' = _grpc_helpers.message_field(241)
    dlong_client: 'Quotation' = _grpc_helpers.message_field(290)
    dshort_client: 'Quotation' = _grpc_helpers.message_field(291)
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


@dataclass
class ShareResponse(_grpc_helpers.Message):
    instrument: 'Share' = _grpc_helpers.message_field(1)


@dataclass
class SharesResponse(_grpc_helpers.Message):
    instruments: List['Share'] = _grpc_helpers.message_field(1)


@dataclass
class Bond(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: 'Quotation' = _grpc_helpers.message_field(7)
    kshort: 'Quotation' = _grpc_helpers.message_field(8)
    dlong: 'Quotation' = _grpc_helpers.message_field(9)
    dshort: 'Quotation' = _grpc_helpers.message_field(10)
    dlong_min: 'Quotation' = _grpc_helpers.message_field(11)
    dshort_min: 'Quotation' = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(15)
    exchange: str = _grpc_helpers.string_field(16)
    coupon_quantity_per_year: int = _grpc_helpers.int32_field(17)
    maturity_date: datetime = _grpc_helpers.message_field(18)
    nominal: 'MoneyValue' = _grpc_helpers.message_field(19)
    initial_nominal: 'MoneyValue' = _grpc_helpers.message_field(20)
    state_reg_date: datetime = _grpc_helpers.message_field(21)
    placement_date: datetime = _grpc_helpers.message_field(22)
    placement_price: 'MoneyValue' = _grpc_helpers.message_field(23)
    aci_value: 'MoneyValue' = _grpc_helpers.message_field(24)
    country_of_risk: str = _grpc_helpers.string_field(25)
    country_of_risk_name: str = _grpc_helpers.string_field(26)
    sector: str = _grpc_helpers.string_field(27)
    issue_kind: str = _grpc_helpers.string_field(28)
    issue_size: int = _grpc_helpers.int64_field(29)
    issue_size_plan: int = _grpc_helpers.int64_field(30)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(31)
    otc_flag: bool = _grpc_helpers.bool_field(32)
    buy_available_flag: bool = _grpc_helpers.bool_field(33)
    sell_available_flag: bool = _grpc_helpers.bool_field(34)
    floating_coupon_flag: bool = _grpc_helpers.bool_field(35)
    perpetual_flag: bool = _grpc_helpers.bool_field(36)
    amortization_flag: bool = _grpc_helpers.bool_field(37)
    min_price_increment: 'Quotation' = _grpc_helpers.message_field(38)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(39)
    uid: str = _grpc_helpers.string_field(40)
    real_exchange: 'RealExchange' = _grpc_helpers.message_field(41)
    position_uid: str = _grpc_helpers.string_field(42)
    asset_uid: str = _grpc_helpers.string_field(43)
    required_tests: List[str] = _grpc_helpers.string_field(44)
    for_iis_flag: bool = _grpc_helpers.bool_field(51)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(52)
    weekend_flag: bool = _grpc_helpers.bool_field(53)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(54)
    subordinated_flag: bool = _grpc_helpers.bool_field(55)
    liquidity_flag: bool = _grpc_helpers.bool_field(56)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(61)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(62)
    risk_level: 'RiskLevel' = _grpc_helpers.message_field(63)
    brand: 'BrandData' = _grpc_helpers.message_field(64)
    bond_type: 'BondType' = _grpc_helpers.message_field(65)
    call_date: datetime = _grpc_helpers.message_field(69)
    dlong_client: 'Quotation' = _grpc_helpers.message_field(90)
    dshort_client: 'Quotation' = _grpc_helpers.message_field(91)


@dataclass
class Currency(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: 'Quotation' = _grpc_helpers.message_field(7)
    kshort: 'Quotation' = _grpc_helpers.message_field(8)
    dlong: 'Quotation' = _grpc_helpers.message_field(9)
    dshort: 'Quotation' = _grpc_helpers.message_field(10)
    dlong_min: 'Quotation' = _grpc_helpers.message_field(11)
    dshort_min: 'Quotation' = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(15)
    exchange: str = _grpc_helpers.string_field(16)
    nominal: 'MoneyValue' = _grpc_helpers.message_field(17)
    country_of_risk: str = _grpc_helpers.string_field(18)
    country_of_risk_name: str = _grpc_helpers.string_field(19)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(20)
    otc_flag: bool = _grpc_helpers.bool_field(21)
    buy_available_flag: bool = _grpc_helpers.bool_field(22)
    sell_available_flag: bool = _grpc_helpers.bool_field(23)
    iso_currency_name: str = _grpc_helpers.string_field(24)
    min_price_increment: 'Quotation' = _grpc_helpers.message_field(25)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(26)
    uid: str = _grpc_helpers.string_field(27)
    real_exchange: 'RealExchange' = _grpc_helpers.message_field(28)
    position_uid: str = _grpc_helpers.string_field(29)
    required_tests: List[str] = _grpc_helpers.string_field(30)
    for_iis_flag: bool = _grpc_helpers.bool_field(41)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(52)
    weekend_flag: bool = _grpc_helpers.bool_field(53)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(54)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    brand: 'BrandData' = _grpc_helpers.message_field(60)
    dlong_client: 'Quotation' = _grpc_helpers.message_field(90)
    dshort_client: 'Quotation' = _grpc_helpers.message_field(91)


@dataclass
class Etf(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: 'Quotation' = _grpc_helpers.message_field(7)
    kshort: 'Quotation' = _grpc_helpers.message_field(8)
    dlong: 'Quotation' = _grpc_helpers.message_field(9)
    dshort: 'Quotation' = _grpc_helpers.message_field(10)
    dlong_min: 'Quotation' = _grpc_helpers.message_field(11)
    dshort_min: 'Quotation' = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(15)
    exchange: str = _grpc_helpers.string_field(16)
    fixed_commission: 'Quotation' = _grpc_helpers.message_field(17)
    focus_type: str = _grpc_helpers.string_field(18)
    released_date: datetime = _grpc_helpers.message_field(19)
    num_shares: 'Quotation' = _grpc_helpers.message_field(20)
    country_of_risk: str = _grpc_helpers.string_field(21)
    country_of_risk_name: str = _grpc_helpers.string_field(22)
    sector: str = _grpc_helpers.string_field(23)
    rebalancing_freq: str = _grpc_helpers.string_field(24)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(25)
    otc_flag: bool = _grpc_helpers.bool_field(26)
    buy_available_flag: bool = _grpc_helpers.bool_field(27)
    sell_available_flag: bool = _grpc_helpers.bool_field(28)
    min_price_increment: 'Quotation' = _grpc_helpers.message_field(29)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(30)
    uid: str = _grpc_helpers.string_field(31)
    real_exchange: 'RealExchange' = _grpc_helpers.message_field(32)
    position_uid: str = _grpc_helpers.string_field(33)
    asset_uid: str = _grpc_helpers.string_field(34)
    instrument_exchange: 'InstrumentExchangeType' = (_grpc_helpers.
        message_field(35))
    required_tests: List[str] = _grpc_helpers.string_field(36)
    for_iis_flag: bool = _grpc_helpers.bool_field(41)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(42)
    weekend_flag: bool = _grpc_helpers.bool_field(43)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(44)
    liquidity_flag: bool = _grpc_helpers.bool_field(45)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    brand: 'BrandData' = _grpc_helpers.message_field(60)
    dlong_client: 'Quotation' = _grpc_helpers.message_field(90)
    dshort_client: 'Quotation' = _grpc_helpers.message_field(91)


@dataclass
class Future(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    lot: int = _grpc_helpers.int32_field(4)
    currency: str = _grpc_helpers.string_field(5)
    klong: 'Quotation' = _grpc_helpers.message_field(6)
    kshort: 'Quotation' = _grpc_helpers.message_field(7)
    dlong: 'Quotation' = _grpc_helpers.message_field(8)
    dshort: 'Quotation' = _grpc_helpers.message_field(9)
    dlong_min: 'Quotation' = _grpc_helpers.message_field(10)
    dshort_min: 'Quotation' = _grpc_helpers.message_field(11)
    short_enabled_flag: bool = _grpc_helpers.bool_field(12)
    name: str = _grpc_helpers.string_field(13)
    exchange: str = _grpc_helpers.string_field(14)
    first_trade_date: datetime = _grpc_helpers.message_field(15)
    last_trade_date: datetime = _grpc_helpers.message_field(16)
    futures_type: str = _grpc_helpers.string_field(17)
    asset_type: str = _grpc_helpers.string_field(18)
    basic_asset: str = _grpc_helpers.string_field(19)
    basic_asset_size: 'Quotation' = _grpc_helpers.message_field(20)
    country_of_risk: str = _grpc_helpers.string_field(21)
    country_of_risk_name: str = _grpc_helpers.string_field(22)
    sector: str = _grpc_helpers.string_field(23)
    expiration_date: datetime = _grpc_helpers.message_field(24)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(25)
    otc_flag: bool = _grpc_helpers.bool_field(26)
    buy_available_flag: bool = _grpc_helpers.bool_field(27)
    sell_available_flag: bool = _grpc_helpers.bool_field(28)
    min_price_increment: 'Quotation' = _grpc_helpers.message_field(29)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(30)
    uid: str = _grpc_helpers.string_field(31)
    real_exchange: 'RealExchange' = _grpc_helpers.message_field(32)
    position_uid: str = _grpc_helpers.string_field(33)
    basic_asset_position_uid: str = _grpc_helpers.string_field(34)
    required_tests: List[str] = _grpc_helpers.string_field(35)
    for_iis_flag: bool = _grpc_helpers.bool_field(41)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(42)
    weekend_flag: bool = _grpc_helpers.bool_field(43)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(44)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    initial_margin_on_buy: 'MoneyValue' = _grpc_helpers.message_field(61)
    initial_margin_on_sell: 'MoneyValue' = _grpc_helpers.message_field(62)
    min_price_increment_amount: 'Quotation' = _grpc_helpers.message_field(63)
    brand: 'BrandData' = _grpc_helpers.message_field(64)
    dlong_client: 'Quotation' = _grpc_helpers.message_field(90)
    dshort_client: 'Quotation' = _grpc_helpers.message_field(91)


@dataclass
class Share(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: 'Quotation' = _grpc_helpers.message_field(7)
    kshort: 'Quotation' = _grpc_helpers.message_field(8)
    dlong: 'Quotation' = _grpc_helpers.message_field(9)
    dshort: 'Quotation' = _grpc_helpers.message_field(10)
    dlong_min: 'Quotation' = _grpc_helpers.message_field(11)
    dshort_min: 'Quotation' = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(15)
    exchange: str = _grpc_helpers.string_field(16)
    ipo_date: datetime = _grpc_helpers.message_field(17)
    issue_size: int = _grpc_helpers.int64_field(18)
    country_of_risk: str = _grpc_helpers.string_field(19)
    country_of_risk_name: str = _grpc_helpers.string_field(20)
    sector: str = _grpc_helpers.string_field(21)
    issue_size_plan: int = _grpc_helpers.int64_field(22)
    nominal: 'MoneyValue' = _grpc_helpers.message_field(23)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(25)
    otc_flag: bool = _grpc_helpers.bool_field(26)
    buy_available_flag: bool = _grpc_helpers.bool_field(27)
    sell_available_flag: bool = _grpc_helpers.bool_field(28)
    div_yield_flag: bool = _grpc_helpers.bool_field(29)
    share_type: 'ShareType' = _grpc_helpers.message_field(30)
    min_price_increment: 'Quotation' = _grpc_helpers.message_field(31)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(32)
    uid: str = _grpc_helpers.string_field(33)
    real_exchange: 'RealExchange' = _grpc_helpers.message_field(34)
    position_uid: str = _grpc_helpers.string_field(35)
    asset_uid: str = _grpc_helpers.string_field(36)
    instrument_exchange: 'InstrumentExchangeType' = (_grpc_helpers.
        message_field(37))
    required_tests: List[str] = _grpc_helpers.string_field(38)
    for_iis_flag: bool = _grpc_helpers.bool_field(46)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(47)
    weekend_flag: bool = _grpc_helpers.bool_field(48)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(49)
    liquidity_flag: bool = _grpc_helpers.bool_field(50)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    brand: 'BrandData' = _grpc_helpers.message_field(60)
    dlong_client: 'Quotation' = _grpc_helpers.message_field(90)
    dshort_client: 'Quotation' = _grpc_helpers.message_field(91)


@dataclass
class GetAccruedInterestsRequest(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)
    instrument_id: str = _grpc_helpers.string_field(4)


@dataclass
class GetAccruedInterestsResponse(_grpc_helpers.Message):
    accrued_interests: List['AccruedInterest'] = _grpc_helpers.message_field(1)


@dataclass
class AccruedInterest(_grpc_helpers.Message):
    date: datetime = _grpc_helpers.message_field(1)
    value: 'Quotation' = _grpc_helpers.message_field(2)
    value_percent: 'Quotation' = _grpc_helpers.message_field(3)
    nominal: 'Quotation' = _grpc_helpers.message_field(4)


@dataclass
class GetFuturesMarginRequest(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(4)


@dataclass
class GetFuturesMarginResponse(_grpc_helpers.Message):
    initial_margin_on_buy: 'MoneyValue' = _grpc_helpers.message_field(1)
    initial_margin_on_sell: 'MoneyValue' = _grpc_helpers.message_field(2)
    min_price_increment: 'Quotation' = _grpc_helpers.message_field(3)
    min_price_increment_amount: 'Quotation' = _grpc_helpers.message_field(4)


@dataclass
class InstrumentResponse(_grpc_helpers.Message):
    instrument: 'Instrument' = _grpc_helpers.message_field(1)


@dataclass
class Instrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    isin: str = _grpc_helpers.string_field(4)
    lot: int = _grpc_helpers.int32_field(5)
    currency: str = _grpc_helpers.string_field(6)
    klong: 'Quotation' = _grpc_helpers.message_field(7)
    kshort: 'Quotation' = _grpc_helpers.message_field(8)
    dlong: 'Quotation' = _grpc_helpers.message_field(9)
    dshort: 'Quotation' = _grpc_helpers.message_field(10)
    dlong_min: 'Quotation' = _grpc_helpers.message_field(11)
    dshort_min: 'Quotation' = _grpc_helpers.message_field(12)
    short_enabled_flag: bool = _grpc_helpers.bool_field(13)
    name: str = _grpc_helpers.string_field(14)
    exchange: str = _grpc_helpers.string_field(15)
    country_of_risk: str = _grpc_helpers.string_field(16)
    country_of_risk_name: str = _grpc_helpers.string_field(17)
    instrument_type: str = _grpc_helpers.string_field(18)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(19)
    otc_flag: bool = _grpc_helpers.bool_field(20)
    buy_available_flag: bool = _grpc_helpers.bool_field(21)
    sell_available_flag: bool = _grpc_helpers.bool_field(22)
    min_price_increment: 'Quotation' = _grpc_helpers.message_field(23)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(24)
    uid: str = _grpc_helpers.string_field(25)
    real_exchange: 'RealExchange' = _grpc_helpers.message_field(26)
    position_uid: str = _grpc_helpers.string_field(27)
    asset_uid: str = _grpc_helpers.string_field(28)
    required_tests: List[str] = _grpc_helpers.string_field(29)
    for_iis_flag: bool = _grpc_helpers.bool_field(36)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(37)
    weekend_flag: bool = _grpc_helpers.bool_field(38)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(39)
    instrument_kind: 'InstrumentType' = _grpc_helpers.message_field(40)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(56)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(57)
    brand: 'BrandData' = _grpc_helpers.message_field(60)
    dlong_client: 'Quotation' = _grpc_helpers.message_field(490)
    dshort_client: 'Quotation' = _grpc_helpers.message_field(491)


@dataclass
class GetDividendsRequest(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    from_: Optional[datetime] = _grpc_helpers.message_field(2, optional=True)
    to: Optional[datetime] = _grpc_helpers.message_field(3, optional=True)
    instrument_id: str = _grpc_helpers.string_field(4)


@dataclass
class GetDividendsResponse(_grpc_helpers.Message):
    dividends: List['Dividend'] = _grpc_helpers.message_field(1)


@dataclass
class Dividend(_grpc_helpers.Message):
    dividend_net: 'MoneyValue' = _grpc_helpers.message_field(1)
    payment_date: datetime = _grpc_helpers.message_field(2)
    declared_date: datetime = _grpc_helpers.message_field(3)
    last_buy_date: datetime = _grpc_helpers.message_field(4)
    dividend_type: str = _grpc_helpers.string_field(5)
    record_date: datetime = _grpc_helpers.message_field(6)
    regularity: str = _grpc_helpers.string_field(7)
    close_price: 'MoneyValue' = _grpc_helpers.message_field(8)
    yield_value: 'Quotation' = _grpc_helpers.message_field(9)
    created_at: datetime = _grpc_helpers.message_field(10)


@dataclass
class AssetRequest(_grpc_helpers.Message):
    id: str = _grpc_helpers.string_field(1)


@dataclass
class AssetResponse(_grpc_helpers.Message):
    asset: 'AssetFull' = _grpc_helpers.message_field(1)


@dataclass
class AssetsRequest(_grpc_helpers.Message):
    instrument_type: Optional['InstrumentType'] = _grpc_helpers.message_field(
        1, optional=True)
    instrument_status: Optional['InstrumentStatus'
        ] = _grpc_helpers.message_field(2, optional=True)


@dataclass
class AssetsResponse(_grpc_helpers.Message):
    assets: List['Asset'] = _grpc_helpers.message_field(1)


@dataclass
class AssetFull(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    type: 'AssetType' = _grpc_helpers.message_field(2)
    name: str = _grpc_helpers.string_field(3)
    name_brief: str = _grpc_helpers.string_field(4)
    description: str = _grpc_helpers.string_field(5)
    deleted_at: datetime = _grpc_helpers.message_field(6)
    required_tests: List[str] = _grpc_helpers.string_field(7)
    currency: Optional['AssetCurrency'] = _grpc_helpers.message_field(8,
        optional=True)
    security: Optional['AssetSecurity'] = _grpc_helpers.message_field(9,
        optional=True)
    gos_reg_code: str = _grpc_helpers.string_field(10)
    cfi: str = _grpc_helpers.string_field(11)
    code_nsd: str = _grpc_helpers.string_field(12)
    status: str = _grpc_helpers.string_field(13)
    brand: 'Brand' = _grpc_helpers.message_field(14)
    updated_at: datetime = _grpc_helpers.message_field(15)
    br_code: str = _grpc_helpers.string_field(16)
    br_code_name: str = _grpc_helpers.string_field(17)
    instruments: List['AssetInstrument'] = _grpc_helpers.message_field(18)


@dataclass
class Asset(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    type: 'AssetType' = _grpc_helpers.message_field(2)
    name: str = _grpc_helpers.string_field(3)
    instruments: List['AssetInstrument'] = _grpc_helpers.message_field(4)


@dataclass
class AssetCurrency(_grpc_helpers.Message):
    base_currency: str = _grpc_helpers.string_field(1)


@dataclass
class AssetSecurity(_grpc_helpers.Message):
    isin: str = _grpc_helpers.string_field(1)
    type: str = _grpc_helpers.string_field(2)
    instrument_kind: 'InstrumentType' = _grpc_helpers.message_field(10)
    share: Optional['AssetShare'] = _grpc_helpers.message_field(3, optional
        =True)
    bond: Optional['AssetBond'] = _grpc_helpers.message_field(4, optional=True)
    sp: Optional['AssetStructuredProduct'] = _grpc_helpers.message_field(5,
        optional=True)
    etf: Optional['AssetEtf'] = _grpc_helpers.message_field(6, optional=True)
    clearing_certificate: Optional['AssetClearingCertificate'
        ] = _grpc_helpers.message_field(7, optional=True)


@dataclass
class AssetShare(_grpc_helpers.Message):
    type: 'ShareType' = _grpc_helpers.message_field(1)
    issue_size: 'Quotation' = _grpc_helpers.message_field(2)
    nominal: 'Quotation' = _grpc_helpers.message_field(3)
    nominal_currency: str = _grpc_helpers.string_field(4)
    primary_index: str = _grpc_helpers.string_field(5)
    dividend_rate: 'Quotation' = _grpc_helpers.message_field(6)
    preferred_share_type: str = _grpc_helpers.string_field(7)
    ipo_date: datetime = _grpc_helpers.message_field(8)
    registry_date: datetime = _grpc_helpers.message_field(9)
    div_yield_flag: bool = _grpc_helpers.bool_field(10)
    issue_kind: str = _grpc_helpers.string_field(11)
    placement_date: datetime = _grpc_helpers.message_field(12)
    repres_isin: str = _grpc_helpers.string_field(13)
    issue_size_plan: 'Quotation' = _grpc_helpers.message_field(14)
    total_float: 'Quotation' = _grpc_helpers.message_field(15)


@dataclass
class AssetBond(_grpc_helpers.Message):
    current_nominal: 'Quotation' = _grpc_helpers.message_field(1)
    borrow_name: str = _grpc_helpers.string_field(2)
    issue_size: 'Quotation' = _grpc_helpers.message_field(3)
    nominal: 'Quotation' = _grpc_helpers.message_field(4)
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
    placement_price: 'Quotation' = _grpc_helpers.message_field(20)
    issue_size_plan: 'Quotation' = _grpc_helpers.message_field(21)


@dataclass
class AssetStructuredProduct(_grpc_helpers.Message):
    borrow_name: str = _grpc_helpers.string_field(1)
    nominal: 'Quotation' = _grpc_helpers.message_field(2)
    nominal_currency: str = _grpc_helpers.string_field(3)
    type: 'StructuredProductType' = _grpc_helpers.message_field(4)
    logic_portfolio: str = _grpc_helpers.string_field(5)
    asset_type: 'AssetType' = _grpc_helpers.message_field(6)
    basic_asset: str = _grpc_helpers.string_field(7)
    safety_barrier: 'Quotation' = _grpc_helpers.message_field(8)
    maturity_date: datetime = _grpc_helpers.message_field(9)
    issue_size_plan: 'Quotation' = _grpc_helpers.message_field(10)
    issue_size: 'Quotation' = _grpc_helpers.message_field(11)
    placement_date: datetime = _grpc_helpers.message_field(12)
    issue_kind: str = _grpc_helpers.string_field(13)


@dataclass
class AssetEtf(_grpc_helpers.Message):
    total_expense: 'Quotation' = _grpc_helpers.message_field(1)
    hurdle_rate: 'Quotation' = _grpc_helpers.message_field(2)
    performance_fee: 'Quotation' = _grpc_helpers.message_field(3)
    fixed_commission: 'Quotation' = _grpc_helpers.message_field(4)
    payment_type: str = _grpc_helpers.string_field(5)
    watermark_flag: bool = _grpc_helpers.bool_field(6)
    buy_premium: 'Quotation' = _grpc_helpers.message_field(7)
    sell_discount: 'Quotation' = _grpc_helpers.message_field(8)
    rebalancing_flag: bool = _grpc_helpers.bool_field(9)
    rebalancing_freq: str = _grpc_helpers.string_field(10)
    management_type: str = _grpc_helpers.string_field(11)
    primary_index: str = _grpc_helpers.string_field(12)
    focus_type: str = _grpc_helpers.string_field(13)
    leveraged_flag: bool = _grpc_helpers.bool_field(14)
    num_share: 'Quotation' = _grpc_helpers.message_field(15)
    ucits_flag: bool = _grpc_helpers.bool_field(16)
    released_date: datetime = _grpc_helpers.message_field(17)
    description: str = _grpc_helpers.string_field(18)
    primary_index_description: str = _grpc_helpers.string_field(19)
    primary_index_company: str = _grpc_helpers.string_field(20)
    index_recovery_period: 'Quotation' = _grpc_helpers.message_field(21)
    inav_code: str = _grpc_helpers.string_field(22)
    div_yield_flag: bool = _grpc_helpers.bool_field(23)
    expense_commission: 'Quotation' = _grpc_helpers.message_field(24)
    primary_index_tracking_error: 'Quotation' = _grpc_helpers.message_field(25)
    rebalancing_plan: str = _grpc_helpers.string_field(26)
    tax_rate: str = _grpc_helpers.string_field(27)
    rebalancing_dates: List[datetime] = _grpc_helpers.message_field(28)
    issue_kind: str = _grpc_helpers.string_field(29)
    nominal: 'Quotation' = _grpc_helpers.message_field(30)
    nominal_currency: str = _grpc_helpers.string_field(31)


@dataclass
class AssetClearingCertificate(_grpc_helpers.Message):
    nominal: 'Quotation' = _grpc_helpers.message_field(1)
    nominal_currency: str = _grpc_helpers.string_field(2)


@dataclass
class Brand(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    name: str = _grpc_helpers.string_field(2)
    description: str = _grpc_helpers.string_field(3)
    info: str = _grpc_helpers.string_field(4)
    company: str = _grpc_helpers.string_field(5)
    sector: str = _grpc_helpers.string_field(6)
    country_of_risk: str = _grpc_helpers.string_field(7)
    country_of_risk_name: str = _grpc_helpers.string_field(8)


@dataclass
class AssetInstrument(_grpc_helpers.Message):
    uid: str = _grpc_helpers.string_field(1)
    figi: str = _grpc_helpers.string_field(2)
    instrument_type: str = _grpc_helpers.string_field(3)
    ticker: str = _grpc_helpers.string_field(4)
    class_code: str = _grpc_helpers.string_field(5)
    links: List['InstrumentLink'] = _grpc_helpers.message_field(6)
    instrument_kind: 'InstrumentType' = _grpc_helpers.message_field(10)
    position_uid: str = _grpc_helpers.string_field(11)


@dataclass
class InstrumentLink(_grpc_helpers.Message):
    type: str = _grpc_helpers.string_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)


@dataclass
class GetFavoritesRequest(_grpc_helpers.Message):
    group_id: Optional[str] = _grpc_helpers.string_field(1, optional=True)


@dataclass
class GetFavoritesResponse(_grpc_helpers.Message):
    favorite_instruments: List['FavoriteInstrument'
        ] = _grpc_helpers.message_field(1)
    group_id: Optional[str] = _grpc_helpers.string_field(2, optional=True)


@dataclass
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
    instrument_kind: 'InstrumentType' = _grpc_helpers.message_field(18)


@dataclass
class EditFavoritesRequest(_grpc_helpers.Message):
    instruments: List['EditFavoritesRequestInstrument'
        ] = _grpc_helpers.message_field(1)
    action_type: 'EditFavoritesActionType' = _grpc_helpers.message_field(6)
    group_id: Optional[str] = _grpc_helpers.string_field(7, optional=True)


@dataclass
class EditFavoritesRequestInstrument(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    instrument_id: str = _grpc_helpers.string_field(2)


@dataclass
class EditFavoritesResponse(_grpc_helpers.Message):
    favorite_instruments: List['FavoriteInstrument'
        ] = _grpc_helpers.message_field(1)
    group_id: Optional[str] = _grpc_helpers.string_field(2, optional=True)


@dataclass
class CreateFavoriteGroupRequest(_grpc_helpers.Message):
    group_name: str = _grpc_helpers.string_field(1)
    group_color: str = _grpc_helpers.string_field(2)
    note: Optional[str] = _grpc_helpers.string_field(3, optional=True)


@dataclass
class CreateFavoriteGroupResponse(_grpc_helpers.Message):
    group_id: str = _grpc_helpers.string_field(1)
    group_name: str = _grpc_helpers.string_field(2)


@dataclass
class DeleteFavoriteGroupRequest(_grpc_helpers.Message):
    group_id: str = _grpc_helpers.string_field(1)


@dataclass
class DeleteFavoriteGroupResponse(_grpc_helpers.Message):
    pass


@dataclass
class GetFavoriteGroupsRequest(_grpc_helpers.Message):
    instrument_id: List[str] = _grpc_helpers.string_field(1)
    excluded_group_id: List[str] = _grpc_helpers.string_field(2)


@dataclass
class GetFavoriteGroupsResponse(_grpc_helpers.Message):
    groups: List['FavoriteGroup'] = _grpc_helpers.message_field(1)


    @dataclass
    class FavoriteGroup(_grpc_helpers.Message):
        group_id: str = _grpc_helpers.string_field(1)
        group_name: str = _grpc_helpers.string_field(2)
        color: str = _grpc_helpers.string_field(3)
        size: int = _grpc_helpers.int32_field(4)
        contains_instrument: Optional[bool] = _grpc_helpers.bool_field(5,
            optional=True)


@dataclass
class GetCountriesRequest(_grpc_helpers.Message):
    pass


@dataclass
class GetCountriesResponse(_grpc_helpers.Message):
    countries: List['CountryResponse'] = _grpc_helpers.message_field(1)


@dataclass
class IndicativesRequest(_grpc_helpers.Message):
    pass


@dataclass
class IndicativesResponse(_grpc_helpers.Message):
    instruments: List['IndicativeResponse'] = _grpc_helpers.message_field(1)


@dataclass
class IndicativeResponse(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    ticker: str = _grpc_helpers.string_field(2)
    class_code: str = _grpc_helpers.string_field(3)
    currency: str = _grpc_helpers.string_field(4)
    instrument_kind: 'InstrumentType' = _grpc_helpers.message_field(10)
    name: str = _grpc_helpers.string_field(12)
    exchange: str = _grpc_helpers.string_field(13)
    uid: str = _grpc_helpers.string_field(14)
    buy_available_flag: bool = _grpc_helpers.bool_field(404)
    sell_available_flag: bool = _grpc_helpers.bool_field(405)


@dataclass
class CountryResponse(_grpc_helpers.Message):
    alfa_two: str = _grpc_helpers.string_field(1)
    alfa_three: str = _grpc_helpers.string_field(2)
    name: str = _grpc_helpers.string_field(3)
    name_brief: str = _grpc_helpers.string_field(4)


@dataclass
class FindInstrumentRequest(_grpc_helpers.Message):
    query: str = _grpc_helpers.string_field(1)
    instrument_kind: Optional['InstrumentType'] = _grpc_helpers.message_field(
        2, optional=True)
    api_trade_available_flag: Optional[bool] = _grpc_helpers.bool_field(3,
        optional=True)


@dataclass
class FindInstrumentResponse(_grpc_helpers.Message):
    instruments: List['InstrumentShort'] = _grpc_helpers.message_field(1)


@dataclass
class InstrumentShort(_grpc_helpers.Message):
    isin: str = _grpc_helpers.string_field(1)
    figi: str = _grpc_helpers.string_field(2)
    ticker: str = _grpc_helpers.string_field(3)
    class_code: str = _grpc_helpers.string_field(4)
    instrument_type: str = _grpc_helpers.string_field(5)
    name: str = _grpc_helpers.string_field(6)
    uid: str = _grpc_helpers.string_field(7)
    position_uid: str = _grpc_helpers.string_field(8)
    instrument_kind: 'InstrumentType' = _grpc_helpers.message_field(10)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(11)
    for_iis_flag: bool = _grpc_helpers.bool_field(12)
    first_1min_candle_date: datetime = _grpc_helpers.message_field(26)
    first_1day_candle_date: datetime = _grpc_helpers.message_field(27)
    for_qual_investor_flag: bool = _grpc_helpers.bool_field(28)
    weekend_flag: bool = _grpc_helpers.bool_field(29)
    blocked_tca_flag: bool = _grpc_helpers.bool_field(30)
    lot: int = _grpc_helpers.int32_field(31)


@dataclass
class GetBrandsRequest(_grpc_helpers.Message):
    paging: 'Page' = _grpc_helpers.message_field(1)


@dataclass
class GetBrandRequest(_grpc_helpers.Message):
    id: str = _grpc_helpers.string_field(1)


@dataclass
class GetBrandsResponse(_grpc_helpers.Message):
    brands: List['Brand'] = _grpc_helpers.message_field(1)
    paging: 'PageResponse' = _grpc_helpers.message_field(2)


@dataclass
class GetAssetFundamentalsRequest(_grpc_helpers.Message):
    assets: List[str] = _grpc_helpers.string_field(1)


@dataclass
class GetAssetFundamentalsResponse(_grpc_helpers.Message):
    fundamentals: List['StatisticResponse'] = _grpc_helpers.message_field(1)


    @dataclass
    class StatisticResponse(_grpc_helpers.Message):
        asset_uid: str = _grpc_helpers.string_field(1)
        currency: str = _grpc_helpers.string_field(2)
        market_capitalization: float = _grpc_helpers.double_field(3)
        high_price_last_52_weeks: float = _grpc_helpers.double_field(4)
        low_price_last_52_weeks: float = _grpc_helpers.double_field(5)
        average_daily_volume_last_10_days: float = _grpc_helpers.double_field(6
            )
        average_daily_volume_last_4_weeks: float = _grpc_helpers.double_field(7
            )
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
        five_year_annual_revenue_growth_rate: float = (_grpc_helpers.
            double_field(18))
        three_year_annual_revenue_growth_rate: float = (_grpc_helpers.
            double_field(19))
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
        five_years_average_dividend_yield: float = _grpc_helpers.double_field(
            41)
        five_year_annual_dividend_growth_rate: float = (_grpc_helpers.
            double_field(42))
        dividend_payout_ratio_fy: float = _grpc_helpers.double_field(43)
        buy_back_ttm: float = _grpc_helpers.double_field(44)
        one_year_annual_revenue_growth_rate: float = (_grpc_helpers.
            double_field(45))
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


@dataclass
class GetAssetReportsRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)
    from_: Optional[datetime] = _grpc_helpers.message_field(2, optional=True)
    to: Optional[datetime] = _grpc_helpers.message_field(3, optional=True)


@dataclass
class GetAssetReportsResponse(_grpc_helpers.Message):
    events: List['GetAssetReportsEvent'] = _grpc_helpers.message_field(1)


    @dataclass
    class GetAssetReportsEvent(_grpc_helpers.Message):
        instrument_id: str = _grpc_helpers.string_field(1)
        report_date: datetime = _grpc_helpers.message_field(2)
        period_year: int = _grpc_helpers.int32_field(3)
        period_num: int = _grpc_helpers.int32_field(4)
        period_type: 'AssetReportPeriodType' = _grpc_helpers.message_field(5)
        created_at: datetime = _grpc_helpers.message_field(6)


    class AssetReportPeriodType(IntEnum):
        PERIOD_TYPE_UNSPECIFIED = 0
        PERIOD_TYPE_QUARTER = 1
        PERIOD_TYPE_SEMIANNUAL = 2
        PERIOD_TYPE_ANNUAL = 3


@dataclass
class GetConsensusForecastsRequest(_grpc_helpers.Message):
    paging: Optional['Page'] = _grpc_helpers.message_field(1, optional=True)


@dataclass
class GetConsensusForecastsResponse(_grpc_helpers.Message):
    items: List['ConsensusForecastsItem'] = _grpc_helpers.message_field(1)
    page: 'PageResponse' = _grpc_helpers.message_field(2)


    @dataclass
    class ConsensusForecastsItem(_grpc_helpers.Message):
        uid: str = _grpc_helpers.string_field(1)
        asset_uid: str = _grpc_helpers.string_field(2)
        created_at: datetime = _grpc_helpers.message_field(3)
        best_target_price: 'Quotation' = _grpc_helpers.message_field(4)
        best_target_low: 'Quotation' = _grpc_helpers.message_field(5)
        best_target_high: 'Quotation' = _grpc_helpers.message_field(6)
        total_buy_recommend: int = _grpc_helpers.int32_field(7)
        total_hold_recommend: int = _grpc_helpers.int32_field(8)
        total_sell_recommend: int = _grpc_helpers.int32_field(9)
        currency: str = _grpc_helpers.string_field(10)
        consensus: 'Recommendation' = _grpc_helpers.message_field(11)
        prognosis_date: datetime = _grpc_helpers.message_field(12)


@dataclass
class GetForecastRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)


@dataclass
class GetForecastResponse(_grpc_helpers.Message):
    targets: List['TargetItem'] = _grpc_helpers.message_field(1)
    consensus: 'ConsensusItem' = _grpc_helpers.message_field(2)


    @dataclass
    class TargetItem(_grpc_helpers.Message):
        uid: str = _grpc_helpers.string_field(1)
        ticker: str = _grpc_helpers.string_field(2)
        company: str = _grpc_helpers.string_field(3)
        recommendation: 'Recommendation' = _grpc_helpers.message_field(4)
        recommendation_date: datetime = _grpc_helpers.message_field(5)
        currency: str = _grpc_helpers.string_field(6)
        current_price: 'Quotation' = _grpc_helpers.message_field(7)
        target_price: 'Quotation' = _grpc_helpers.message_field(8)
        price_change: 'Quotation' = _grpc_helpers.message_field(9)
        price_change_rel: 'Quotation' = _grpc_helpers.message_field(10)
        show_name: str = _grpc_helpers.string_field(11)


    @dataclass
    class ConsensusItem(_grpc_helpers.Message):
        uid: str = _grpc_helpers.string_field(1)
        ticker: str = _grpc_helpers.string_field(2)
        recommendation: 'Recommendation' = _grpc_helpers.message_field(3)
        currency: str = _grpc_helpers.string_field(4)
        current_price: 'Quotation' = _grpc_helpers.message_field(5)
        consensus: 'Quotation' = _grpc_helpers.message_field(6)
        min_target: 'Quotation' = _grpc_helpers.message_field(7)
        max_target: 'Quotation' = _grpc_helpers.message_field(8)
        price_change: 'Quotation' = _grpc_helpers.message_field(9)
        price_change_rel: 'Quotation' = _grpc_helpers.message_field(10)


@dataclass
class RiskRatesRequest(_grpc_helpers.Message):
    instrument_id: List[str] = _grpc_helpers.string_field(1)


@dataclass
class RiskRatesResponse(_grpc_helpers.Message):
    instrument_risk_rates: List['RiskRateResult'
        ] = _grpc_helpers.message_field(1)


    @dataclass
    class RiskRateResult(_grpc_helpers.Message):
        instrument_uid: str = _grpc_helpers.string_field(1)
        short_risk_rate: Optional['RiskRate'] = _grpc_helpers.message_field(
            2, optional=True)
        long_risk_rate: Optional['RiskRate'] = _grpc_helpers.message_field(
            3, optional=True)
        short_risk_rates: List['RiskRate'] = _grpc_helpers.message_field(5)
        long_risk_rates: List['RiskRate'] = _grpc_helpers.message_field(6)
        error: Optional[str] = _grpc_helpers.string_field(9, optional=True)


    @dataclass
    class RiskRate(_grpc_helpers.Message):
        risk_level_code: str = _grpc_helpers.string_field(2)
        value: 'Quotation' = _grpc_helpers.message_field(5)


@dataclass
class TradingInterval(_grpc_helpers.Message):
    type: str = _grpc_helpers.string_field(1)
    interval: 'TimeInterval' = _grpc_helpers.message_field(2)


    @dataclass
    class TimeInterval(_grpc_helpers.Message):
        start_ts: datetime = _grpc_helpers.message_field(1)
        end_ts: datetime = _grpc_helpers.message_field(2)


@dataclass
class GetInsiderDealsRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)
    limit: int = _grpc_helpers.int32_field(2)
    next_cursor: Optional[str] = _grpc_helpers.string_field(3, optional=True)


@dataclass
class GetInsiderDealsResponse(_grpc_helpers.Message):
    insider_deals: List['InsiderDeal'] = _grpc_helpers.message_field(1)
    next_cursor: Optional[str] = _grpc_helpers.string_field(2, optional=True)


    @dataclass
    class InsiderDeal(_grpc_helpers.Message):
        trade_id: int = _grpc_helpers.int64_field(1)
        direction: 'TradeDirection' = _grpc_helpers.message_field(2)
        currency: str = _grpc_helpers.string_field(3)
        date: datetime = _grpc_helpers.message_field(4)
        quantity: int = _grpc_helpers.int64_field(5)
        price: 'Quotation' = _grpc_helpers.message_field(6)
        instrument_uid: str = _grpc_helpers.string_field(7)
        ticker: str = _grpc_helpers.string_field(8)
        investor_name: str = _grpc_helpers.string_field(9)
        investor_position: str = _grpc_helpers.string_field(10)
        percentage: float = _grpc_helpers.float_field(11)
        is_option_execution: bool = _grpc_helpers.bool_field(12)
        disclosure_date: datetime = _grpc_helpers.message_field(13)


    class TradeDirection(IntEnum):
        TRADE_DIRECTION_UNSPECIFIED = 0
        TRADE_DIRECTION_BUY = 1
        TRADE_DIRECTION_SELL = 2


class InstrumentsService(BaseService):
    """/*Методы сервиса предназначены для получения:<br/>1. Информации об инструментах.<br/>2.
                            Расписания торговых сессий.<br/>3. Календаря выплат купонов по облигациям.<br/>4.
                            Размера гарантийного обеспечения по фьючерсам.<br/>5. Дивидендов по ценной бумаге.*/"""
    _protobuf = instruments_pb2
    _protobuf_grpc = instruments_pb2_grpc
    _protobuf_stub = _protobuf_grpc.InstrumentsServiceStub

    @handle_request_error('TradingSchedules')
    def trading_schedules(self, request: 'TradingSchedulesRequest'=
        TradingSchedulesRequest()) ->'TradingSchedulesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            TradingSchedulesRequest())
        response, call = self._stub.TradingSchedules.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'TradingSchedules')
        return protobuf_to_dataclass(response, TradingSchedulesResponse)

    @handle_request_error('BondBy')
    def bond_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'BondResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.BondBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'BondBy')
        return protobuf_to_dataclass(response, BondResponse)

    @handle_request_error('Bonds')
    def bonds(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'BondsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Bonds.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Bonds')
        return protobuf_to_dataclass(response, BondsResponse)

    @handle_request_error('GetBondCoupons')
    def get_bond_coupons(self, request: 'GetBondCouponsRequest'=
        GetBondCouponsRequest()) ->'GetBondCouponsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBondCouponsRequest())
        response, call = self._stub.GetBondCoupons.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBondCoupons')
        return protobuf_to_dataclass(response, GetBondCouponsResponse)

    @handle_request_error('GetBondEvents')
    def get_bond_events(self, request: 'GetBondEventsRequest'=
        GetBondEventsRequest()) ->'GetBondEventsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBondEventsRequest())
        response, call = self._stub.GetBondEvents.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBondEvents')
        return protobuf_to_dataclass(response, GetBondEventsResponse)

    @handle_request_error('CurrencyBy')
    def currency_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'CurrencyResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.CurrencyBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CurrencyBy')
        return protobuf_to_dataclass(response, CurrencyResponse)

    @handle_request_error('Currencies')
    def currencies(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'CurrenciesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Currencies.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Currencies')
        return protobuf_to_dataclass(response, CurrenciesResponse)

    @handle_request_error('EtfBy')
    def etf_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'EtfResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.EtfBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'EtfBy')
        return protobuf_to_dataclass(response, EtfResponse)

    @handle_request_error('Etfs')
    def etfs(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'EtfsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Etfs.with_call(request=protobuf_request,
            metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Etfs')
        return protobuf_to_dataclass(response, EtfsResponse)

    @handle_request_error('FutureBy')
    def future_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'FutureResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.FutureBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'FutureBy')
        return protobuf_to_dataclass(response, FutureResponse)

    @handle_request_error('Futures')
    def futures(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'FuturesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Futures.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Futures')
        return protobuf_to_dataclass(response, FuturesResponse)

    @handle_request_error('OptionBy')
    def option_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'OptionResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.OptionBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'OptionBy')
        return protobuf_to_dataclass(response, OptionResponse)

    @handle_request_error('Options')
    def options(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'OptionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Options.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Options')
        return protobuf_to_dataclass(response, OptionsResponse)

    @handle_request_error('OptionsBy')
    def options_by(self, request: 'FilterOptionsRequest'=FilterOptionsRequest()
        ) ->'OptionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            FilterOptionsRequest())
        response, call = self._stub.OptionsBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'OptionsBy')
        return protobuf_to_dataclass(response, OptionsResponse)

    @handle_request_error('ShareBy')
    def share_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'ShareResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.ShareBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'ShareBy')
        return protobuf_to_dataclass(response, ShareResponse)

    @handle_request_error('Shares')
    def shares(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'SharesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Shares.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Shares')
        return protobuf_to_dataclass(response, SharesResponse)

    @handle_request_error('Indicatives')
    def indicatives(self, request: 'IndicativesRequest'=IndicativesRequest()
        ) ->'IndicativesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            IndicativesRequest())
        response, call = self._stub.Indicatives.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'Indicatives')
        return protobuf_to_dataclass(response, IndicativesResponse)

    @handle_request_error('GetAccruedInterests')
    def get_accrued_interests(self, request: 'GetAccruedInterestsRequest'=
        GetAccruedInterestsRequest()) ->'GetAccruedInterestsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccruedInterestsRequest())
        response, call = self._stub.GetAccruedInterests.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAccruedInterests')
        return protobuf_to_dataclass(response, GetAccruedInterestsResponse)

    @handle_request_error('GetFuturesMargin')
    def get_futures_margin(self, request: 'GetFuturesMarginRequest'=
        GetFuturesMarginRequest()) ->'GetFuturesMarginResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFuturesMarginRequest())
        response, call = self._stub.GetFuturesMargin.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetFuturesMargin')
        return protobuf_to_dataclass(response, GetFuturesMarginResponse)

    @handle_request_error('GetInstrumentBy')
    def get_instrument_by(self, request: 'InstrumentRequest'=
        InstrumentRequest()) ->'InstrumentResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.GetInstrumentBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetInstrumentBy')
        return protobuf_to_dataclass(response, InstrumentResponse)

    @handle_request_error('GetDividends')
    def get_dividends(self, request: 'GetDividendsRequest'=
        GetDividendsRequest()) ->'GetDividendsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetDividendsRequest())
        response, call = self._stub.GetDividends.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetDividends')
        return protobuf_to_dataclass(response, GetDividendsResponse)

    @handle_request_error('GetAssetBy')
    def get_asset_by(self, request: 'AssetRequest'=AssetRequest()
        ) ->'AssetResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            AssetRequest())
        response, call = self._stub.GetAssetBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAssetBy')
        return protobuf_to_dataclass(response, AssetResponse)

    @handle_request_error('GetAssets')
    def get_assets(self, request: 'AssetsRequest'=AssetsRequest()
        ) ->'AssetsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            AssetsRequest())
        response, call = self._stub.GetAssets.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAssets')
        return protobuf_to_dataclass(response, AssetsResponse)

    @handle_request_error('GetFavorites')
    def get_favorites(self, request: 'GetFavoritesRequest'=
        GetFavoritesRequest()) ->'GetFavoritesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFavoritesRequest())
        response, call = self._stub.GetFavorites.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetFavorites')
        return protobuf_to_dataclass(response, GetFavoritesResponse)

    @handle_request_error('EditFavorites')
    def edit_favorites(self, request: 'EditFavoritesRequest'=
        EditFavoritesRequest()) ->'EditFavoritesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            EditFavoritesRequest())
        response, call = self._stub.EditFavorites.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'EditFavorites')
        return protobuf_to_dataclass(response, EditFavoritesResponse)

    @handle_request_error('CreateFavoriteGroup')
    def create_favorite_group(self, request: 'CreateFavoriteGroupRequest'=
        CreateFavoriteGroupRequest()) ->'CreateFavoriteGroupResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CreateFavoriteGroupRequest())
        response, call = self._stub.CreateFavoriteGroup.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'CreateFavoriteGroup')
        return protobuf_to_dataclass(response, CreateFavoriteGroupResponse)

    @handle_request_error('DeleteFavoriteGroup')
    def delete_favorite_group(self, request: 'DeleteFavoriteGroupRequest'=
        DeleteFavoriteGroupRequest()) ->'DeleteFavoriteGroupResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            DeleteFavoriteGroupRequest())
        response, call = self._stub.DeleteFavoriteGroup.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'DeleteFavoriteGroup')
        return protobuf_to_dataclass(response, DeleteFavoriteGroupResponse)

    @handle_request_error('GetFavoriteGroups')
    def get_favorite_groups(self, request: 'GetFavoriteGroupsRequest'=
        GetFavoriteGroupsRequest()) ->'GetFavoriteGroupsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFavoriteGroupsRequest())
        response, call = self._stub.GetFavoriteGroups.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetFavoriteGroups')
        return protobuf_to_dataclass(response, GetFavoriteGroupsResponse)

    @handle_request_error('GetCountries')
    def get_countries(self, request: 'GetCountriesRequest'=
        GetCountriesRequest()) ->'GetCountriesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetCountriesRequest())
        response, call = self._stub.GetCountries.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetCountries')
        return protobuf_to_dataclass(response, GetCountriesResponse)

    @handle_request_error('FindInstrument')
    def find_instrument(self, request: 'FindInstrumentRequest'=
        FindInstrumentRequest()) ->'FindInstrumentResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            FindInstrumentRequest())
        response, call = self._stub.FindInstrument.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'FindInstrument')
        return protobuf_to_dataclass(response, FindInstrumentResponse)

    @handle_request_error('GetBrands')
    def get_brands(self, request: 'GetBrandsRequest'=GetBrandsRequest()
        ) ->'GetBrandsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBrandsRequest())
        response, call = self._stub.GetBrands.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBrands')
        return protobuf_to_dataclass(response, GetBrandsResponse)

    @handle_request_error('GetBrandBy')
    def get_brand_by(self, request: 'GetBrandRequest'=GetBrandRequest()
        ) ->'Brand':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBrandRequest())
        response, call = self._stub.GetBrandBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetBrandBy')
        return protobuf_to_dataclass(response, Brand)

    @handle_request_error('GetAssetFundamentals')
    def get_asset_fundamentals(self, request: 'GetAssetFundamentalsRequest'
        =GetAssetFundamentalsRequest()) ->'GetAssetFundamentalsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAssetFundamentalsRequest())
        response, call = self._stub.GetAssetFundamentals.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAssetFundamentals')
        return protobuf_to_dataclass(response, GetAssetFundamentalsResponse)

    @handle_request_error('GetAssetReports')
    def get_asset_reports(self, request: 'GetAssetReportsRequest'=
        GetAssetReportsRequest()) ->'GetAssetReportsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAssetReportsRequest())
        response, call = self._stub.GetAssetReports.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetAssetReports')
        return protobuf_to_dataclass(response, GetAssetReportsResponse)

    @handle_request_error('GetConsensusForecasts')
    def get_consensus_forecasts(self, request:
        'GetConsensusForecastsRequest'=GetConsensusForecastsRequest()
        ) ->'GetConsensusForecastsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetConsensusForecastsRequest())
        response, call = self._stub.GetConsensusForecasts.with_call(request
            =protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetConsensusForecasts')
        return protobuf_to_dataclass(response, GetConsensusForecastsResponse)

    @handle_request_error('GetForecastBy')
    def get_forecast_by(self, request: 'GetForecastRequest'=
        GetForecastRequest()) ->'GetForecastResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetForecastRequest())
        response, call = self._stub.GetForecastBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetForecastBy')
        return protobuf_to_dataclass(response, GetForecastResponse)

    @handle_request_error('GetRiskRates')
    def get_risk_rates(self, request: 'RiskRatesRequest'=RiskRatesRequest()
        ) ->'RiskRatesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            RiskRatesRequest())
        response, call = self._stub.GetRiskRates.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetRiskRates')
        return protobuf_to_dataclass(response, RiskRatesResponse)

    @handle_request_error('GetInsiderDeals')
    def get_insider_deals(self, request: 'GetInsiderDealsRequest'=
        GetInsiderDealsRequest()) ->'GetInsiderDealsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetInsiderDealsRequest())
        response, call = self._stub.GetInsiderDeals.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetInsiderDeals')
        return protobuf_to_dataclass(response, GetInsiderDealsResponse)


class AsyncInstrumentsService(BaseService):
    """//TradingSchedules — расписания торговых площадок"""
    _protobuf = instruments_pb2
    _protobuf_grpc = instruments_pb2_grpc
    _protobuf_stub = _protobuf_grpc.InstrumentsServiceStub

    @handle_aio_request_error('TradingSchedules')
    async def trading_schedules(self, request: 'TradingSchedulesRequest'=
        TradingSchedulesRequest()) ->'TradingSchedulesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            TradingSchedulesRequest())
        response_coro = self._stub.TradingSchedules(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'TradingSchedules')
        return protobuf_to_dataclass(response, TradingSchedulesResponse)

    @handle_aio_request_error('BondBy')
    async def bond_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'BondResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response_coro = self._stub.BondBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'BondBy')
        return protobuf_to_dataclass(response, BondResponse)

    @handle_aio_request_error('Bonds')
    async def bonds(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'BondsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response_coro = self._stub.Bonds(request=protobuf_request, metadata
            =self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'Bonds')
        return protobuf_to_dataclass(response, BondsResponse)

    @handle_aio_request_error('GetBondCoupons')
    async def get_bond_coupons(self, request: 'GetBondCouponsRequest'=
        GetBondCouponsRequest()) ->'GetBondCouponsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBondCouponsRequest())
        response_coro = self._stub.GetBondCoupons(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetBondCoupons')
        return protobuf_to_dataclass(response, GetBondCouponsResponse)

    @handle_aio_request_error('GetBondEvents')
    async def get_bond_events(self, request: 'GetBondEventsRequest'=
        GetBondEventsRequest()) ->'GetBondEventsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBondEventsRequest())
        response_coro = self._stub.GetBondEvents(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetBondEvents')
        return protobuf_to_dataclass(response, GetBondEventsResponse)

    @handle_aio_request_error('CurrencyBy')
    async def currency_by(self, request: 'InstrumentRequest'=
        InstrumentRequest()) ->'CurrencyResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response_coro = self._stub.CurrencyBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'CurrencyBy')
        return protobuf_to_dataclass(response, CurrencyResponse)

    @handle_aio_request_error('Currencies')
    async def currencies(self, request: 'InstrumentsRequest'=
        InstrumentsRequest()) ->'CurrenciesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response_coro = self._stub.Currencies(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'Currencies')
        return protobuf_to_dataclass(response, CurrenciesResponse)

    @handle_aio_request_error('EtfBy')
    async def etf_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'EtfResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response_coro = self._stub.EtfBy(request=protobuf_request, metadata
            =self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'EtfBy')
        return protobuf_to_dataclass(response, EtfResponse)

    @handle_aio_request_error('Etfs')
    async def etfs(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'EtfsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response_coro = self._stub.Etfs(request=protobuf_request, metadata=
            self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'Etfs')
        return protobuf_to_dataclass(response, EtfsResponse)

    @handle_aio_request_error('FutureBy')
    async def future_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'FutureResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response_coro = self._stub.FutureBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'FutureBy')
        return protobuf_to_dataclass(response, FutureResponse)

    @handle_aio_request_error('Futures')
    async def futures(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'FuturesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response_coro = self._stub.Futures(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'Futures')
        return protobuf_to_dataclass(response, FuturesResponse)

    @handle_aio_request_error('OptionBy')
    async def option_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'OptionResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response_coro = self._stub.OptionBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'OptionBy')
        return protobuf_to_dataclass(response, OptionResponse)

    @handle_aio_request_error('Options')
    async def options(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'OptionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response_coro = self._stub.Options(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'Options')
        return protobuf_to_dataclass(response, OptionsResponse)

    @handle_aio_request_error('OptionsBy')
    async def options_by(self, request: 'FilterOptionsRequest'=
        FilterOptionsRequest()) ->'OptionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            FilterOptionsRequest())
        response_coro = self._stub.OptionsBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'OptionsBy'
            )
        return protobuf_to_dataclass(response, OptionsResponse)

    @handle_aio_request_error('ShareBy')
    async def share_by(self, request: 'InstrumentRequest'=InstrumentRequest()
        ) ->'ShareResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response_coro = self._stub.ShareBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'ShareBy')
        return protobuf_to_dataclass(response, ShareResponse)

    @handle_aio_request_error('Shares')
    async def shares(self, request: 'InstrumentsRequest'=InstrumentsRequest()
        ) ->'SharesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response_coro = self._stub.Shares(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'Shares')
        return protobuf_to_dataclass(response, SharesResponse)

    @handle_aio_request_error('Indicatives')
    async def indicatives(self, request: 'IndicativesRequest'=
        IndicativesRequest()) ->'IndicativesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            IndicativesRequest())
        response_coro = self._stub.Indicatives(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'Indicatives')
        return protobuf_to_dataclass(response, IndicativesResponse)

    @handle_aio_request_error('GetAccruedInterests')
    async def get_accrued_interests(self, request:
        'GetAccruedInterestsRequest'=GetAccruedInterestsRequest()
        ) ->'GetAccruedInterestsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccruedInterestsRequest())
        response_coro = self._stub.GetAccruedInterests(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetAccruedInterests')
        return protobuf_to_dataclass(response, GetAccruedInterestsResponse)

    @handle_aio_request_error('GetFuturesMargin')
    async def get_futures_margin(self, request: 'GetFuturesMarginRequest'=
        GetFuturesMarginRequest()) ->'GetFuturesMarginResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFuturesMarginRequest())
        response_coro = self._stub.GetFuturesMargin(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetFuturesMargin')
        return protobuf_to_dataclass(response, GetFuturesMarginResponse)

    @handle_aio_request_error('GetInstrumentBy')
    async def get_instrument_by(self, request: 'InstrumentRequest'=
        InstrumentRequest()) ->'InstrumentResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response_coro = self._stub.GetInstrumentBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetInstrumentBy')
        return protobuf_to_dataclass(response, InstrumentResponse)

    @handle_aio_request_error('GetDividends')
    async def get_dividends(self, request: 'GetDividendsRequest'=
        GetDividendsRequest()) ->'GetDividendsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetDividendsRequest())
        response_coro = self._stub.GetDividends(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetDividends')
        return protobuf_to_dataclass(response, GetDividendsResponse)

    @handle_aio_request_error('GetAssetBy')
    async def get_asset_by(self, request: 'AssetRequest'=AssetRequest()
        ) ->'AssetResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            AssetRequest())
        response_coro = self._stub.GetAssetBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetAssetBy')
        return protobuf_to_dataclass(response, AssetResponse)

    @handle_aio_request_error('GetAssets')
    async def get_assets(self, request: 'AssetsRequest'=AssetsRequest()
        ) ->'AssetsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            AssetsRequest())
        response_coro = self._stub.GetAssets(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'GetAssets'
            )
        return protobuf_to_dataclass(response, AssetsResponse)

    @handle_aio_request_error('GetFavorites')
    async def get_favorites(self, request: 'GetFavoritesRequest'=
        GetFavoritesRequest()) ->'GetFavoritesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFavoritesRequest())
        response_coro = self._stub.GetFavorites(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetFavorites')
        return protobuf_to_dataclass(response, GetFavoritesResponse)

    @handle_aio_request_error('EditFavorites')
    async def edit_favorites(self, request: 'EditFavoritesRequest'=
        EditFavoritesRequest()) ->'EditFavoritesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            EditFavoritesRequest())
        response_coro = self._stub.EditFavorites(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'EditFavorites')
        return protobuf_to_dataclass(response, EditFavoritesResponse)

    @handle_aio_request_error('CreateFavoriteGroup')
    async def create_favorite_group(self, request:
        'CreateFavoriteGroupRequest'=CreateFavoriteGroupRequest()
        ) ->'CreateFavoriteGroupResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            CreateFavoriteGroupRequest())
        response_coro = self._stub.CreateFavoriteGroup(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'CreateFavoriteGroup')
        return protobuf_to_dataclass(response, CreateFavoriteGroupResponse)

    @handle_aio_request_error('DeleteFavoriteGroup')
    async def delete_favorite_group(self, request:
        'DeleteFavoriteGroupRequest'=DeleteFavoriteGroupRequest()
        ) ->'DeleteFavoriteGroupResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            DeleteFavoriteGroupRequest())
        response_coro = self._stub.DeleteFavoriteGroup(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'DeleteFavoriteGroup')
        return protobuf_to_dataclass(response, DeleteFavoriteGroupResponse)

    @handle_aio_request_error('GetFavoriteGroups')
    async def get_favorite_groups(self, request: 'GetFavoriteGroupsRequest'
        =GetFavoriteGroupsRequest()) ->'GetFavoriteGroupsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFavoriteGroupsRequest())
        response_coro = self._stub.GetFavoriteGroups(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetFavoriteGroups')
        return protobuf_to_dataclass(response, GetFavoriteGroupsResponse)

    @handle_aio_request_error('GetCountries')
    async def get_countries(self, request: 'GetCountriesRequest'=
        GetCountriesRequest()) ->'GetCountriesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetCountriesRequest())
        response_coro = self._stub.GetCountries(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetCountries')
        return protobuf_to_dataclass(response, GetCountriesResponse)

    @handle_aio_request_error('FindInstrument')
    async def find_instrument(self, request: 'FindInstrumentRequest'=
        FindInstrumentRequest()) ->'FindInstrumentResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            FindInstrumentRequest())
        response_coro = self._stub.FindInstrument(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'FindInstrument')
        return protobuf_to_dataclass(response, FindInstrumentResponse)

    @handle_aio_request_error('GetBrands')
    async def get_brands(self, request: 'GetBrandsRequest'=GetBrandsRequest()
        ) ->'GetBrandsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBrandsRequest())
        response_coro = self._stub.GetBrands(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro), 'GetBrands'
            )
        return protobuf_to_dataclass(response, GetBrandsResponse)

    @handle_aio_request_error('GetBrandBy')
    async def get_brand_by(self, request: 'GetBrandRequest'=GetBrandRequest()
        ) ->'Brand':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBrandRequest())
        response_coro = self._stub.GetBrandBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetBrandBy')
        return protobuf_to_dataclass(response, Brand)

    @handle_aio_request_error('GetAssetFundamentals')
    async def get_asset_fundamentals(self, request:
        'GetAssetFundamentalsRequest'=GetAssetFundamentalsRequest()
        ) ->'GetAssetFundamentalsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAssetFundamentalsRequest())
        response_coro = self._stub.GetAssetFundamentals(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetAssetFundamentals')
        return protobuf_to_dataclass(response, GetAssetFundamentalsResponse)

    @handle_aio_request_error('GetAssetReports')
    async def get_asset_reports(self, request: 'GetAssetReportsRequest'=
        GetAssetReportsRequest()) ->'GetAssetReportsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAssetReportsRequest())
        response_coro = self._stub.GetAssetReports(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetAssetReports')
        return protobuf_to_dataclass(response, GetAssetReportsResponse)

    @handle_aio_request_error('GetConsensusForecasts')
    async def get_consensus_forecasts(self, request:
        'GetConsensusForecastsRequest'=GetConsensusForecastsRequest()
        ) ->'GetConsensusForecastsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetConsensusForecastsRequest())
        response_coro = self._stub.GetConsensusForecasts(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetConsensusForecasts')
        return protobuf_to_dataclass(response, GetConsensusForecastsResponse)

    @handle_aio_request_error('GetForecastBy')
    async def get_forecast_by(self, request: 'GetForecastRequest'=
        GetForecastRequest()) ->'GetForecastResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetForecastRequest())
        response_coro = self._stub.GetForecastBy(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetForecastBy')
        return protobuf_to_dataclass(response, GetForecastResponse)

    @handle_aio_request_error('GetRiskRates')
    async def get_risk_rates(self, request: 'RiskRatesRequest'=
        RiskRatesRequest()) ->'RiskRatesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            RiskRatesRequest())
        response_coro = self._stub.GetRiskRates(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetRiskRates')
        return protobuf_to_dataclass(response, RiskRatesResponse)

    @handle_aio_request_error('GetInsiderDeals')
    async def get_insider_deals(self, request: 'GetInsiderDealsRequest'=
        GetInsiderDealsRequest()) ->'GetInsiderDealsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetInsiderDealsRequest())
        response_coro = self._stub.GetInsiderDeals(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetInsiderDeals')
        return protobuf_to_dataclass(response, GetInsiderDealsResponse)
