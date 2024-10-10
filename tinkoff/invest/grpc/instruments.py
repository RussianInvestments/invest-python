from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import List, Optional

from iprotopy import dataclass_to_protobuf, protobuf_to_dataclass

from base_service import BaseService
from tinkoff.invest.grpc import instruments_pb2, instruments_pb2_grpc
from tinkoff.invest.grpc.common import (
    BrandData,
    InstrumentType,
    MoneyValue,
    Page,
    PageResponse,
    Quotation,
    SecurityTradingStatus,
)


class InstrumentsService(BaseService):
    """/*Методы сервиса предназначены для получения:</br>1. Информации об инструментах.</br>2.
                            Расписания торговых сессий.</br>3. Календаря выплат купонов по облигациям.</br>4.
                            Размера гарантийного обеспечения по фьючерсам.</br>5. Дивидендов по ценной бумаге.*/"""
    _protobuf = instruments_pb2
    _protobuf_grpc = instruments_pb2_grpc
    _protobuf_stub = _protobuf_grpc.InstrumentsServiceStub

    def TradingSchedules(self, request: 'TradingSchedulesRequest'
        ) ->'TradingSchedulesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            TradingSchedulesRequest())
        response, call = self._stub.TradingSchedules.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, TradingSchedulesResponse)

    def BondBy(self, request: 'InstrumentRequest') ->'BondResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.BondBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, BondResponse)

    def Bonds(self, request: 'InstrumentsRequest') ->'BondsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Bonds.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, BondsResponse)

    def GetBondCoupons(self, request: 'GetBondCouponsRequest'
        ) ->'GetBondCouponsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBondCouponsRequest())
        response, call = self._stub.GetBondCoupons.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetBondCouponsResponse)

    def GetBondEvents(self, request: 'GetBondEventsRequest'
        ) ->'GetBondEventsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBondEventsRequest())
        response, call = self._stub.GetBondEvents.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetBondEventsResponse)

    def CurrencyBy(self, request: 'InstrumentRequest') ->'CurrencyResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.CurrencyBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, CurrencyResponse)

    def Currencies(self, request: 'InstrumentsRequest') ->'CurrenciesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Currencies.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, CurrenciesResponse)

    def EtfBy(self, request: 'InstrumentRequest') ->'EtfResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.EtfBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, EtfResponse)

    def Etfs(self, request: 'InstrumentsRequest') ->'EtfsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Etfs.with_call(request=protobuf_request,
            metadata=self._metadata)
        return protobuf_to_dataclass(response, EtfsResponse)

    def FutureBy(self, request: 'InstrumentRequest') ->'FutureResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.FutureBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, FutureResponse)

    def Futures(self, request: 'InstrumentsRequest') ->'FuturesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Futures.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, FuturesResponse)

    def OptionBy(self, request: 'InstrumentRequest') ->'OptionResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.OptionBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, OptionResponse)

    def Options(self, request: 'InstrumentsRequest') ->'OptionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Options.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, OptionsResponse)

    def OptionsBy(self, request: 'FilterOptionsRequest') ->'OptionsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            FilterOptionsRequest())
        response, call = self._stub.OptionsBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, OptionsResponse)

    def ShareBy(self, request: 'InstrumentRequest') ->'ShareResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.ShareBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, ShareResponse)

    def Shares(self, request: 'InstrumentsRequest') ->'SharesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentsRequest())
        response, call = self._stub.Shares.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, SharesResponse)

    def Indicatives(self, request: 'IndicativesRequest'
        ) ->'IndicativesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            IndicativesRequest())
        response, call = self._stub.Indicatives.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, IndicativesResponse)

    def GetAccruedInterests(self, request: 'GetAccruedInterestsRequest'
        ) ->'GetAccruedInterestsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAccruedInterestsRequest())
        response, call = self._stub.GetAccruedInterests.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAccruedInterestsResponse)

    def GetFuturesMargin(self, request: 'GetFuturesMarginRequest'
        ) ->'GetFuturesMarginResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFuturesMarginRequest())
        response, call = self._stub.GetFuturesMargin.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetFuturesMarginResponse)

    def GetInstrumentBy(self, request: 'InstrumentRequest'
        ) ->'InstrumentResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            InstrumentRequest())
        response, call = self._stub.GetInstrumentBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, InstrumentResponse)

    def GetDividends(self, request: 'GetDividendsRequest'
        ) ->'GetDividendsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetDividendsRequest())
        response, call = self._stub.GetDividends.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetDividendsResponse)

    def GetAssetBy(self, request: 'AssetRequest') ->'AssetResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            AssetRequest())
        response, call = self._stub.GetAssetBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, AssetResponse)

    def GetAssets(self, request: 'AssetsRequest') ->'AssetsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            AssetsRequest())
        response, call = self._stub.GetAssets.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, AssetsResponse)

    def GetFavorites(self, request: 'GetFavoritesRequest'
        ) ->'GetFavoritesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetFavoritesRequest())
        response, call = self._stub.GetFavorites.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetFavoritesResponse)

    def EditFavorites(self, request: 'EditFavoritesRequest'
        ) ->'EditFavoritesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            EditFavoritesRequest())
        response, call = self._stub.EditFavorites.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, EditFavoritesResponse)

    def GetCountries(self, request: 'GetCountriesRequest'
        ) ->'GetCountriesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetCountriesRequest())
        response, call = self._stub.GetCountries.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetCountriesResponse)

    def FindInstrument(self, request: 'FindInstrumentRequest'
        ) ->'FindInstrumentResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            FindInstrumentRequest())
        response, call = self._stub.FindInstrument.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, FindInstrumentResponse)

    def GetBrands(self, request: 'GetBrandsRequest') ->'GetBrandsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBrandsRequest())
        response, call = self._stub.GetBrands.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetBrandsResponse)

    def GetBrandBy(self, request: 'GetBrandRequest') ->'Brand':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetBrandRequest())
        response, call = self._stub.GetBrandBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, Brand)

    def GetAssetFundamentals(self, request: 'GetAssetFundamentalsRequest'
        ) ->'GetAssetFundamentalsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAssetFundamentalsRequest())
        response, call = self._stub.GetAssetFundamentals.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAssetFundamentalsResponse)

    def GetAssetReports(self, request: 'GetAssetReportsRequest'
        ) ->'GetAssetReportsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetAssetReportsRequest())
        response, call = self._stub.GetAssetReports.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetAssetReportsResponse)

    def GetConsensusForecasts(self, request: 'GetConsensusForecastsRequest'
        ) ->'GetConsensusForecastsResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetConsensusForecastsRequest())
        response, call = self._stub.GetConsensusForecasts.with_call(request
            =protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetConsensusForecastsResponse)

    def GetForecastBy(self, request: 'GetForecastRequest'
        ) ->'GetForecastResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetForecastRequest())
        response, call = self._stub.GetForecastBy.with_call(request=
            protobuf_request, metadata=self._metadata)
        return protobuf_to_dataclass(response, GetForecastResponse)


@dataclass
class TradingSchedulesRequest:
    exchange: Optional[str] = None
    from_: Optional[datetime] = None
    to: Optional[datetime] = None


@dataclass
class TradingSchedulesResponse:
    exchanges: List['TradingSchedule']


@dataclass
class TradingSchedule:
    exchange: str
    days: List['TradingDay']


@dataclass
class TradingDay:
    date: datetime
    is_trading_day: bool
    start_time: datetime
    end_time: datetime
    opening_auction_start_time: datetime
    closing_auction_end_time: datetime
    evening_opening_auction_start_time: datetime
    evening_start_time: datetime
    evening_end_time: datetime
    clearing_start_time: datetime
    clearing_end_time: datetime
    premarket_start_time: datetime
    premarket_end_time: datetime
    closing_auction_start_time: datetime
    opening_auction_end_time: datetime
    intervals: List['TradingInterval']


@dataclass
class InstrumentRequest:
    id_type: 'InstrumentIdType'
    id: str
    class_code: Optional[str] = None


@dataclass
class InstrumentsRequest:
    instrument_status: Optional['InstrumentStatus'] = None
    instrument_exchange: Optional['InstrumentExchangeType'] = None


@dataclass
class FilterOptionsRequest:
    basic_asset_uid: Optional[str] = None
    basic_asset_position_uid: Optional[str] = None


@dataclass
class BondResponse:
    instrument: 'Bond'


@dataclass
class BondsResponse:
    instruments: List['Bond']


@dataclass
class GetBondCouponsRequest:
    figi: str
    instrument_id: str
    from_: Optional[datetime] = None
    to: Optional[datetime] = None


@dataclass
class GetBondCouponsResponse:
    events: List['Coupon']


@dataclass
class GetBondEventsRequest:
    instrument_id: str
    type: 'EventType'
    from_: Optional[datetime] = None
    to: Optional[datetime] = None


    class EventType(IntEnum):
        EVENT_TYPE_UNSPECIFIED = 0
        EVENT_TYPE_CPN = 1
        EVENT_TYPE_CALL = 2
        EVENT_TYPE_MTY = 3
        EVENT_TYPE_CONV = 4


@dataclass
class GetBondEventsResponse:
    events: List['BondEvent']


    @dataclass
    class BondEvent:
        instrument_id: str
        event_number: int
        event_date: datetime
        event_type: 'GetBondEventsRequest.EventType'
        event_total_vol: 'Quotation'
        fix_date: datetime
        rate_date: datetime
        default_date: datetime
        real_pay_date: datetime
        pay_date: datetime
        pay_one_bond: 'MoneyValue'
        money_flow_val: 'MoneyValue'
        execution: str
        operation_type: str
        value: 'Quotation'
        note: str
        convert_to_fin_tool_id: str
        coupon_start_date: datetime
        coupon_end_date: datetime
        coupon_period: int
        coupon_interest_rate: 'Quotation'


@dataclass
class Coupon:
    figi: str
    coupon_date: datetime
    coupon_number: int
    fix_date: datetime
    pay_one_bond: 'MoneyValue'
    coupon_type: 'CouponType'
    coupon_start_date: datetime
    coupon_end_date: datetime
    coupon_period: int


class CouponType(IntEnum):
    COUPON_TYPE_UNSPECIFIED = 0
    COUPON_TYPE_CONSTANT = 1
    COUPON_TYPE_FLOATING = 2
    COUPON_TYPE_DISCOUNT = 3
    COUPON_TYPE_MORTGAGE = 4
    COUPON_TYPE_FIX = 5
    COUPON_TYPE_VARIABLE = 6
    COUPON_TYPE_OTHER = 7


@dataclass
class CurrencyResponse:
    instrument: 'Currency'


@dataclass
class CurrenciesResponse:
    instruments: List['Currency']


@dataclass
class EtfResponse:
    instrument: 'Etf'


@dataclass
class EtfsResponse:
    instruments: List['Etf']


@dataclass
class FutureResponse:
    instrument: 'Future'


@dataclass
class FuturesResponse:
    instruments: List['Future']


@dataclass
class OptionResponse:
    instrument: 'Option'


@dataclass
class OptionsResponse:
    instruments: List['Option']


@dataclass
class Option:
    uid: str
    position_uid: str
    ticker: str
    class_code: str
    basic_asset_position_uid: str
    trading_status: 'SecurityTradingStatus'
    real_exchange: 'RealExchange'
    direction: 'OptionDirection'
    payment_type: 'OptionPaymentType'
    style: 'OptionStyle'
    settlement_type: 'OptionSettlementType'
    name: str
    currency: str
    settlement_currency: str
    asset_type: str
    basic_asset: str
    exchange: str
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    brand: 'BrandData'
    lot: int
    basic_asset_size: 'Quotation'
    klong: 'Quotation'
    kshort: 'Quotation'
    dlong: 'Quotation'
    dshort: 'Quotation'
    dlong_min: 'Quotation'
    dshort_min: 'Quotation'
    min_price_increment: 'Quotation'
    strike_price: 'MoneyValue'
    expiration_date: datetime
    first_trade_date: datetime
    last_trade_date: datetime
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    short_enabled_flag: bool
    for_iis_flag: bool
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    api_trade_available_flag: bool


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


@dataclass
class ShareResponse:
    instrument: 'Share'


@dataclass
class SharesResponse:
    instruments: List['Share']


@dataclass
class Bond:
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: 'Quotation'
    kshort: 'Quotation'
    dlong: 'Quotation'
    dshort: 'Quotation'
    dlong_min: 'Quotation'
    dshort_min: 'Quotation'
    short_enabled_flag: bool
    name: str
    exchange: str
    coupon_quantity_per_year: int
    maturity_date: datetime
    nominal: 'MoneyValue'
    initial_nominal: 'MoneyValue'
    state_reg_date: datetime
    placement_date: datetime
    placement_price: 'MoneyValue'
    aci_value: 'MoneyValue'
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    issue_kind: str
    issue_size: int
    issue_size_plan: int
    trading_status: 'SecurityTradingStatus'
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    floating_coupon_flag: bool
    perpetual_flag: bool
    amortization_flag: bool
    min_price_increment: 'Quotation'
    api_trade_available_flag: bool
    uid: str
    real_exchange: 'RealExchange'
    position_uid: str
    asset_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    subordinated_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    risk_level: 'RiskLevel'
    brand: 'BrandData'
    bond_type: 'BondType'


@dataclass
class Currency:
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: 'Quotation'
    kshort: 'Quotation'
    dlong: 'Quotation'
    dshort: 'Quotation'
    dlong_min: 'Quotation'
    dshort_min: 'Quotation'
    short_enabled_flag: bool
    name: str
    exchange: str
    nominal: 'MoneyValue'
    country_of_risk: str
    country_of_risk_name: str
    trading_status: 'SecurityTradingStatus'
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    iso_currency_name: str
    min_price_increment: 'Quotation'
    api_trade_available_flag: bool
    uid: str
    real_exchange: 'RealExchange'
    position_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    brand: 'BrandData'


@dataclass
class Etf:
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: 'Quotation'
    kshort: 'Quotation'
    dlong: 'Quotation'
    dshort: 'Quotation'
    dlong_min: 'Quotation'
    dshort_min: 'Quotation'
    short_enabled_flag: bool
    name: str
    exchange: str
    fixed_commission: 'Quotation'
    focus_type: str
    released_date: datetime
    num_shares: 'Quotation'
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    rebalancing_freq: str
    trading_status: 'SecurityTradingStatus'
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: 'Quotation'
    api_trade_available_flag: bool
    uid: str
    real_exchange: 'RealExchange'
    position_uid: str
    asset_uid: str
    instrument_exchange: 'InstrumentExchangeType'
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    brand: 'BrandData'


@dataclass
class Future:
    figi: str
    ticker: str
    class_code: str
    lot: int
    currency: str
    klong: 'Quotation'
    kshort: 'Quotation'
    dlong: 'Quotation'
    dshort: 'Quotation'
    dlong_min: 'Quotation'
    dshort_min: 'Quotation'
    short_enabled_flag: bool
    name: str
    exchange: str
    first_trade_date: datetime
    last_trade_date: datetime
    futures_type: str
    asset_type: str
    basic_asset: str
    basic_asset_size: 'Quotation'
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    expiration_date: datetime
    trading_status: 'SecurityTradingStatus'
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: 'Quotation'
    api_trade_available_flag: bool
    uid: str
    real_exchange: 'RealExchange'
    position_uid: str
    basic_asset_position_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    initial_margin_on_buy: 'MoneyValue'
    initial_margin_on_sell: 'MoneyValue'
    min_price_increment_amount: 'Quotation'
    brand: 'BrandData'


@dataclass
class Share:
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: 'Quotation'
    kshort: 'Quotation'
    dlong: 'Quotation'
    dshort: 'Quotation'
    dlong_min: 'Quotation'
    dshort_min: 'Quotation'
    short_enabled_flag: bool
    name: str
    exchange: str
    ipo_date: datetime
    issue_size: int
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    issue_size_plan: int
    nominal: 'MoneyValue'
    trading_status: 'SecurityTradingStatus'
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    div_yield_flag: bool
    share_type: 'ShareType'
    min_price_increment: 'Quotation'
    api_trade_available_flag: bool
    uid: str
    real_exchange: 'RealExchange'
    position_uid: str
    asset_uid: str
    instrument_exchange: 'InstrumentExchangeType'
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    brand: 'BrandData'


@dataclass
class GetAccruedInterestsRequest:
    figi: str
    from_: datetime
    to: datetime
    instrument_id: str


@dataclass
class GetAccruedInterestsResponse:
    accrued_interests: List['AccruedInterest']


@dataclass
class AccruedInterest:
    date: datetime
    value: 'Quotation'
    value_percent: 'Quotation'
    nominal: 'Quotation'


@dataclass
class GetFuturesMarginRequest:
    figi: str
    instrument_id: str


@dataclass
class GetFuturesMarginResponse:
    initial_margin_on_buy: 'MoneyValue'
    initial_margin_on_sell: 'MoneyValue'
    min_price_increment: 'Quotation'
    min_price_increment_amount: 'Quotation'


class InstrumentIdType(IntEnum):
    INSTRUMENT_ID_UNSPECIFIED = 0
    INSTRUMENT_ID_TYPE_FIGI = 1
    INSTRUMENT_ID_TYPE_TICKER = 2
    INSTRUMENT_ID_TYPE_UID = 3
    INSTRUMENT_ID_TYPE_POSITION_UID = 4


class InstrumentStatus(IntEnum):
    INSTRUMENT_STATUS_UNSPECIFIED = 0
    INSTRUMENT_STATUS_BASE = 1
    INSTRUMENT_STATUS_ALL = 2


@dataclass
class InstrumentResponse:
    instrument: 'Instrument'


@dataclass
class Instrument:
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: 'Quotation'
    kshort: 'Quotation'
    dlong: 'Quotation'
    dshort: 'Quotation'
    dlong_min: 'Quotation'
    dshort_min: 'Quotation'
    short_enabled_flag: bool
    name: str
    exchange: str
    country_of_risk: str
    country_of_risk_name: str
    instrument_type: str
    trading_status: 'SecurityTradingStatus'
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: 'Quotation'
    api_trade_available_flag: bool
    uid: str
    real_exchange: 'RealExchange'
    position_uid: str
    asset_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    instrument_kind: 'InstrumentType'
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    brand: 'BrandData'


@dataclass
class GetDividendsRequest:
    figi: str
    instrument_id: str
    from_: Optional[datetime] = None
    to: Optional[datetime] = None


@dataclass
class GetDividendsResponse:
    dividends: List['Dividend']


@dataclass
class Dividend:
    dividend_net: 'MoneyValue'
    payment_date: datetime
    declared_date: datetime
    last_buy_date: datetime
    dividend_type: str
    record_date: datetime
    regularity: str
    close_price: 'MoneyValue'
    yield_value: 'Quotation'
    created_at: datetime


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


@dataclass
class AssetRequest:
    id: str


@dataclass
class AssetResponse:
    asset: 'AssetFull'


@dataclass
class AssetsRequest:
    instrument_type: Optional['InstrumentType'] = None


@dataclass
class AssetsResponse:
    assets: List['Asset']


@dataclass
class AssetFull:
    uid: str
    type: 'AssetType'
    name: str
    name_brief: str
    description: str
    deleted_at: datetime
    required_tests: List[str]
    gos_reg_code: str
    cfi: str
    code_nsd: str
    status: str
    brand: 'Brand'
    updated_at: datetime
    br_code: str
    br_code_name: str
    instruments: List['AssetInstrument']
    currency: Optional['AssetCurrency'] = None
    security: Optional['AssetSecurity'] = None


@dataclass
class Asset:
    uid: str
    type: 'AssetType'
    name: str
    instruments: List['AssetInstrument']


class AssetType(IntEnum):
    ASSET_TYPE_UNSPECIFIED = 0
    ASSET_TYPE_CURRENCY = 1
    ASSET_TYPE_COMMODITY = 2
    ASSET_TYPE_INDEX = 3
    ASSET_TYPE_SECURITY = 4


@dataclass
class AssetCurrency:
    base_currency: str


@dataclass
class AssetSecurity:
    isin: str
    type: str
    instrument_kind: 'InstrumentType'
    share: Optional['AssetShare'] = None
    bond: Optional['AssetBond'] = None
    sp: Optional['AssetStructuredProduct'] = None
    etf: Optional['AssetEtf'] = None
    clearing_certificate: Optional['AssetClearingCertificate'] = None


@dataclass
class AssetShare:
    type: 'ShareType'
    issue_size: 'Quotation'
    nominal: 'Quotation'
    nominal_currency: str
    primary_index: str
    dividend_rate: 'Quotation'
    preferred_share_type: str
    ipo_date: datetime
    registry_date: datetime
    div_yield_flag: bool
    issue_kind: str
    placement_date: datetime
    repres_isin: str
    issue_size_plan: 'Quotation'
    total_float: 'Quotation'


@dataclass
class AssetBond:
    current_nominal: 'Quotation'
    borrow_name: str
    issue_size: 'Quotation'
    nominal: 'Quotation'
    nominal_currency: str
    issue_kind: str
    interest_kind: str
    coupon_quantity_per_year: int
    indexed_nominal_flag: bool
    subordinated_flag: bool
    collateral_flag: bool
    tax_free_flag: bool
    amortization_flag: bool
    floating_coupon_flag: bool
    perpetual_flag: bool
    maturity_date: datetime
    return_condition: str
    state_reg_date: datetime
    placement_date: datetime
    placement_price: 'Quotation'
    issue_size_plan: 'Quotation'


@dataclass
class AssetStructuredProduct:
    borrow_name: str
    nominal: 'Quotation'
    nominal_currency: str
    type: 'StructuredProductType'
    logic_portfolio: str
    asset_type: 'AssetType'
    basic_asset: str
    safety_barrier: 'Quotation'
    maturity_date: datetime
    issue_size_plan: 'Quotation'
    issue_size: 'Quotation'
    placement_date: datetime
    issue_kind: str


class StructuredProductType(IntEnum):
    SP_TYPE_UNSPECIFIED = 0
    SP_TYPE_DELIVERABLE = 1
    SP_TYPE_NON_DELIVERABLE = 2


@dataclass
class AssetEtf:
    total_expense: 'Quotation'
    hurdle_rate: 'Quotation'
    performance_fee: 'Quotation'
    fixed_commission: 'Quotation'
    payment_type: str
    watermark_flag: bool
    buy_premium: 'Quotation'
    sell_discount: 'Quotation'
    rebalancing_flag: bool
    rebalancing_freq: str
    management_type: str
    primary_index: str
    focus_type: str
    leveraged_flag: bool
    num_share: 'Quotation'
    ucits_flag: bool
    released_date: datetime
    description: str
    primary_index_description: str
    primary_index_company: str
    index_recovery_period: 'Quotation'
    inav_code: str
    div_yield_flag: bool
    expense_commission: 'Quotation'
    primary_index_tracking_error: 'Quotation'
    rebalancing_plan: str
    tax_rate: str
    rebalancing_dates: List[datetime]
    issue_kind: str
    nominal: 'Quotation'
    nominal_currency: str


@dataclass
class AssetClearingCertificate:
    nominal: 'Quotation'
    nominal_currency: str


@dataclass
class Brand:
    uid: str
    name: str
    description: str
    info: str
    company: str
    sector: str
    country_of_risk: str
    country_of_risk_name: str


@dataclass
class AssetInstrument:
    uid: str
    figi: str
    instrument_type: str
    ticker: str
    class_code: str
    links: List['InstrumentLink']
    instrument_kind: 'InstrumentType'
    position_uid: str


@dataclass
class InstrumentLink:
    type: str
    instrument_uid: str


@dataclass
class GetFavoritesRequest:
    pass


@dataclass
class GetFavoritesResponse:
    favorite_instruments: List['FavoriteInstrument']


@dataclass
class FavoriteInstrument:
    figi: str
    ticker: str
    class_code: str
    isin: str
    instrument_type: str
    name: str
    uid: str
    otc_flag: bool
    api_trade_available_flag: bool
    instrument_kind: 'InstrumentType'


@dataclass
class EditFavoritesRequest:
    instruments: List['EditFavoritesRequestInstrument']
    action_type: 'EditFavoritesActionType'


@dataclass
class EditFavoritesRequestInstrument:
    instrument_id: str
    figi: Optional[str] = None


class EditFavoritesActionType(IntEnum):
    EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED = 0
    EDIT_FAVORITES_ACTION_TYPE_ADD = 1
    EDIT_FAVORITES_ACTION_TYPE_DEL = 2


@dataclass
class EditFavoritesResponse:
    favorite_instruments: List['FavoriteInstrument']


class RealExchange(IntEnum):
    REAL_EXCHANGE_UNSPECIFIED = 0
    REAL_EXCHANGE_MOEX = 1
    REAL_EXCHANGE_RTS = 2
    REAL_EXCHANGE_OTC = 3
    REAL_EXCHANGE_DEALER = 4


@dataclass
class GetCountriesRequest:
    pass


@dataclass
class GetCountriesResponse:
    countries: List['CountryResponse']


@dataclass
class IndicativesRequest:
    pass


@dataclass
class IndicativesResponse:
    instruments: List['IndicativeResponse']


@dataclass
class IndicativeResponse:
    figi: str
    ticker: str
    class_code: str
    currency: str
    instrument_kind: 'InstrumentType'
    name: str
    exchange: str
    uid: str
    buy_available_flag: bool
    sell_available_flag: bool


@dataclass
class CountryResponse:
    alfa_two: str
    alfa_three: str
    name: str
    name_brief: str


@dataclass
class FindInstrumentRequest:
    query: str
    instrument_kind: Optional['InstrumentType'] = None
    api_trade_available_flag: Optional[bool] = None


@dataclass
class FindInstrumentResponse:
    instruments: List['InstrumentShort']


@dataclass
class InstrumentShort:
    isin: str
    figi: str
    ticker: str
    class_code: str
    instrument_type: str
    name: str
    uid: str
    position_uid: str
    instrument_kind: 'InstrumentType'
    api_trade_available_flag: bool
    for_iis_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool


@dataclass
class GetBrandsRequest:
    paging: 'Page'


@dataclass
class GetBrandRequest:
    id: str


@dataclass
class GetBrandsResponse:
    brands: List['Brand']
    paging: 'PageResponse'


@dataclass
class GetAssetFundamentalsRequest:
    assets: List[str]


@dataclass
class GetAssetFundamentalsResponse:
    fundamentals: List['StatisticResponse']


    @dataclass
    class StatisticResponse:
        asset_uid: str
        currency: str
        market_capitalization: float
        high_price_last_52_weeks: float
        low_price_last_52_weeks: float
        average_daily_volume_last_10_days: float
        average_daily_volume_last_4_weeks: float
        beta: float
        free_float: float
        forward_annual_dividend_yield: float
        shares_outstanding: float
        revenue_ttm: float
        ebitda_ttm: float
        net_income_ttm: float
        eps_ttm: float
        diluted_eps_ttm: float
        free_cash_flow_ttm: float
        five_year_annual_revenue_growth_rate: float
        three_year_annual_revenue_growth_rate: float
        pe_ratio_ttm: float
        price_to_sales_ttm: float
        price_to_book_ttm: float
        price_to_free_cash_flow_ttm: float
        total_enterprise_value_mrq: float
        ev_to_ebitda_mrq: float
        net_margin_mrq: float
        net_interest_margin_mrq: float
        roe: float
        roa: float
        roic: float
        total_debt_mrq: float
        total_debt_to_equity_mrq: float
        total_debt_to_ebitda_mrq: float
        free_cash_flow_to_price: float
        net_debt_to_ebitda: float
        current_ratio_mrq: float
        fixed_charge_coverage_ratio_fy: float
        dividend_yield_daily_ttm: float
        dividend_rate_ttm: float
        dividends_per_share: float
        five_years_average_dividend_yield: float
        five_year_annual_dividend_growth_rate: float
        dividend_payout_ratio_fy: float
        buy_back_ttm: float
        one_year_annual_revenue_growth_rate: float
        domicile_indicator_code: str
        adr_to_common_share_ratio: float
        number_of_employees: float
        ex_dividend_date: datetime
        fiscal_period_start_date: datetime
        fiscal_period_end_date: datetime
        revenue_change_five_years: float
        eps_change_five_years: float
        ebitda_change_five_years: float
        total_debt_change_five_years: float
        ev_to_sales: float


@dataclass
class GetAssetReportsRequest:
    instrument_id: str
    from_: Optional[datetime] = None
    to: Optional[datetime] = None


@dataclass
class GetAssetReportsResponse:
    events: List['GetAssetReportsEvent']


    @dataclass
    class GetAssetReportsEvent:
        instrument_id: str
        report_date: datetime
        period_year: int
        period_num: int
        period_type: 'AssetReportPeriodType'
        created_at: datetime


    class AssetReportPeriodType(IntEnum):
        PERIOD_TYPE_UNSPECIFIED = 0
        PERIOD_TYPE_QUARTER = 1
        PERIOD_TYPE_SEMIANNUAL = 2
        PERIOD_TYPE_ANNUAL = 3


@dataclass
class GetConsensusForecastsRequest:
    paging: Optional['Page'] = None


@dataclass
class GetConsensusForecastsResponse:
    items: List['ConsensusForecastsItem']
    page: 'PageResponse'


    @dataclass
    class ConsensusForecastsItem:
        uid: str
        asset_uid: str
        created_at: datetime
        best_target_price: 'Quotation'
        best_target_low: 'Quotation'
        best_target_high: 'Quotation'
        total_buy_recommend: int
        total_hold_recommend: int
        total_sell_recommend: int
        currency: str
        consensus: 'Recommendation'
        prognosis_date: datetime


class Recommendation(IntEnum):
    RECOMMENDATION_UNSPECIFIED = 0
    RECOMMENDATION_BUY = 1
    RECOMMENDATION_HOLD = 2
    RECOMMENDATION_SELL = 3


@dataclass
class GetForecastRequest:
    instrument_id: str


@dataclass
class GetForecastResponse:
    targets: List['TargetItem']
    consensus: 'ConsensusItem'


    @dataclass
    class TargetItem:
        uid: str
        ticker: str
        company: str
        recommendation: 'Recommendation'
        recommendation_date: datetime
        currency: str
        current_price: 'Quotation'
        target_price: 'Quotation'
        price_change: 'Quotation'
        price_change_rel: 'Quotation'
        show_name: str


    @dataclass
    class ConsensusItem:
        uid: str
        ticker: str
        recommendation: 'Recommendation'
        currency: str
        current_price: 'Quotation'
        consensus: 'Quotation'
        min_target: 'Quotation'
        max_target: 'Quotation'
        price_change: 'Quotation'
        price_change_rel: 'Quotation'


@dataclass
class TradingInterval:
    type: str
    interval: 'TimeInterval'


    @dataclass
    class TimeInterval:
        start_ts: datetime
        end_ts: datetime


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
