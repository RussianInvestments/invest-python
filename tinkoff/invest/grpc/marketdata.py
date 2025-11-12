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
from tinkoff.invest.grpc import marketdata_pb2, marketdata_pb2_grpc
from tinkoff.invest.grpc.common import (
    InstrumentStatus,
    Ping,
    PingDelaySettings,
    PingRequest,
    Quotation,
    SecurityTradingStatus,
)
from tinkoff.invest.logging import (
    get_tracking_id_from_call,
    get_tracking_id_from_coro,
    log_request,
)


class SubscriptionAction(IntEnum):
    SUBSCRIPTION_ACTION_UNSPECIFIED = 0
    SUBSCRIPTION_ACTION_SUBSCRIBE = 1
    SUBSCRIPTION_ACTION_UNSUBSCRIBE = 2


class SubscriptionInterval(IntEnum):
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


class SubscriptionStatus(IntEnum):
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


class TradeSourceType(IntEnum):
    TRADE_SOURCE_UNSPECIFIED = 0
    TRADE_SOURCE_EXCHANGE = 1
    TRADE_SOURCE_DEALER = 2
    TRADE_SOURCE_ALL = 3


class TradeDirection(IntEnum):
    TRADE_DIRECTION_UNSPECIFIED = 0
    TRADE_DIRECTION_BUY = 1
    TRADE_DIRECTION_SELL = 2


class CandleInterval(IntEnum):
    CANDLE_INTERVAL_UNSPECIFIED = 0
    CANDLE_INTERVAL_1_MIN = 1
    CANDLE_INTERVAL_5_MIN = 2
    CANDLE_INTERVAL_15_MIN = 3
    CANDLE_INTERVAL_HOUR = 4
    CANDLE_INTERVAL_DAY = 5
    CANDLE_INTERVAL_2_MIN = 6
    CANDLE_INTERVAL_3_MIN = 7
    CANDLE_INTERVAL_10_MIN = 8
    CANDLE_INTERVAL_30_MIN = 9
    CANDLE_INTERVAL_2_HOUR = 10
    CANDLE_INTERVAL_4_HOUR = 11
    CANDLE_INTERVAL_WEEK = 12
    CANDLE_INTERVAL_MONTH = 13
    CANDLE_INTERVAL_5_SEC = 14
    CANDLE_INTERVAL_10_SEC = 15
    CANDLE_INTERVAL_30_SEC = 16


class CandleSource(IntEnum):
    CANDLE_SOURCE_UNSPECIFIED = 0
    CANDLE_SOURCE_EXCHANGE = 1
    CANDLE_SOURCE_DEALER_WEEKEND = 2


class MarketValueType(IntEnum):
    INSTRUMENT_VALUE_UNSPECIFIED = 0
    INSTRUMENT_VALUE_LAST_PRICE = 1
    INSTRUMENT_VALUE_LAST_PRICE_DEALER = 2
    INSTRUMENT_VALUE_CLOSE_PRICE = 3
    INSTRUMENT_VALUE_EVENING_SESSION_PRICE = 4
    INSTRUMENT_VALUE_OPEN_INTEREST = 5
    INSTRUMENT_VALUE_THEOR_PRICE = 6


class OrderBookType(IntEnum):
    ORDERBOOK_TYPE_UNSPECIFIED = 0
    ORDERBOOK_TYPE_EXCHANGE = 1
    ORDERBOOK_TYPE_DEALER = 2
    ORDERBOOK_TYPE_ALL = 3


class LastPriceType(IntEnum):
    LAST_PRICE_UNSPECIFIED = 0
    LAST_PRICE_EXCHANGE = 1
    LAST_PRICE_DEALER = 2


@dataclass
class MarketDataRequest(_grpc_helpers.Message):
    subscribe_candles_request: Optional['SubscribeCandlesRequest'
        ] = _grpc_helpers.message_field(1, optional=True)
    subscribe_order_book_request: Optional['SubscribeOrderBookRequest'
        ] = _grpc_helpers.message_field(2, optional=True)
    subscribe_trades_request: Optional['SubscribeTradesRequest'
        ] = _grpc_helpers.message_field(3, optional=True)
    subscribe_info_request: Optional['SubscribeInfoRequest'
        ] = _grpc_helpers.message_field(4, optional=True)
    subscribe_last_price_request: Optional['SubscribeLastPriceRequest'
        ] = _grpc_helpers.message_field(5, optional=True)
    get_my_subscriptions: Optional['GetMySubscriptions'
        ] = _grpc_helpers.message_field(6, optional=True)
    ping: Optional['PingRequest'] = _grpc_helpers.message_field(7, optional
        =True)
    ping_settings: Optional['PingDelaySettings'] = _grpc_helpers.message_field(
        15, optional=True)


@dataclass
class MarketDataServerSideStreamRequest(_grpc_helpers.Message):
    subscribe_candles_request: 'SubscribeCandlesRequest' = (_grpc_helpers.
        message_field(1))
    subscribe_order_book_request: 'SubscribeOrderBookRequest' = (_grpc_helpers
        .message_field(2))
    subscribe_trades_request: 'SubscribeTradesRequest' = (_grpc_helpers.
        message_field(3))
    subscribe_info_request: 'SubscribeInfoRequest' = (_grpc_helpers.
        message_field(4))
    subscribe_last_price_request: 'SubscribeLastPriceRequest' = (_grpc_helpers
        .message_field(5))
    ping_settings: 'PingDelaySettings' = _grpc_helpers.message_field(15)


@dataclass
class MarketDataResponse(_grpc_helpers.Message):
    subscribe_candles_response: Optional['SubscribeCandlesResponse'
        ] = _grpc_helpers.message_field(1, optional=True)
    subscribe_order_book_response: Optional['SubscribeOrderBookResponse'
        ] = _grpc_helpers.message_field(2, optional=True)
    subscribe_trades_response: Optional['SubscribeTradesResponse'
        ] = _grpc_helpers.message_field(3, optional=True)
    subscribe_info_response: Optional['SubscribeInfoResponse'
        ] = _grpc_helpers.message_field(4, optional=True)
    candle: Optional['Candle'] = _grpc_helpers.message_field(5, optional=True)
    trade: Optional['Trade'] = _grpc_helpers.message_field(6, optional=True)
    orderbook: Optional['OrderBook'] = _grpc_helpers.message_field(7,
        optional=True)
    trading_status: Optional['TradingStatus'] = _grpc_helpers.message_field(
        8, optional=True)
    ping: Optional['Ping'] = _grpc_helpers.message_field(9, optional=True)
    subscribe_last_price_response: Optional['SubscribeLastPriceResponse'
        ] = _grpc_helpers.message_field(10, optional=True)
    last_price: Optional['LastPrice'] = _grpc_helpers.message_field(11,
        optional=True)
    open_interest: Optional['OpenInterest'] = _grpc_helpers.message_field(
        12, optional=True)


@dataclass
class SubscribeCandlesRequest(_grpc_helpers.Message):
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(1)
    instruments: List['CandleInstrument'] = _grpc_helpers.message_field(2)
    waiting_close: bool = _grpc_helpers.bool_field(3)
    candle_source_type: Optional['GetCandlesRequest.CandleSource'
        ] = _grpc_helpers.message_field(9, optional=True)


@dataclass
class CandleInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    interval: 'SubscriptionInterval' = _grpc_helpers.message_field(2)
    instrument_id: str = _grpc_helpers.string_field(3)


@dataclass
class SubscribeCandlesResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    candles_subscriptions: List['CandleSubscription'
        ] = _grpc_helpers.message_field(2)


@dataclass
class CandleSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    interval: 'SubscriptionInterval' = _grpc_helpers.message_field(2)
    subscription_status: 'SubscriptionStatus' = _grpc_helpers.message_field(3)
    instrument_uid: str = _grpc_helpers.string_field(4)
    waiting_close: bool = _grpc_helpers.bool_field(5)
    stream_id: str = _grpc_helpers.string_field(6)
    subscription_id: str = _grpc_helpers.string_field(7)
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(8)
    candle_source_type: Optional['GetCandlesRequest.CandleSource'
        ] = _grpc_helpers.message_field(9, optional=True)


@dataclass
class SubscribeOrderBookRequest(_grpc_helpers.Message):
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(1)
    instruments: List['OrderBookInstrument'] = _grpc_helpers.message_field(2)


@dataclass
class OrderBookInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    instrument_id: str = _grpc_helpers.string_field(3)
    order_book_type: 'OrderBookType' = _grpc_helpers.message_field(4)


@dataclass
class SubscribeOrderBookResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    order_book_subscriptions: List['OrderBookSubscription'
        ] = _grpc_helpers.message_field(2)


@dataclass
class OrderBookSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    subscription_status: 'SubscriptionStatus' = _grpc_helpers.message_field(3)
    instrument_uid: str = _grpc_helpers.string_field(4)
    stream_id: str = _grpc_helpers.string_field(5)
    subscription_id: str = _grpc_helpers.string_field(6)
    order_book_type: 'OrderBookType' = _grpc_helpers.message_field(7)
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(8)


@dataclass
class SubscribeTradesRequest(_grpc_helpers.Message):
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(1)
    instruments: List['TradeInstrument'] = _grpc_helpers.message_field(2)
    trade_source: 'TradeSourceType' = _grpc_helpers.message_field(3)
    with_open_interest: bool = _grpc_helpers.bool_field(4)


@dataclass
class TradeInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)


@dataclass
class SubscribeTradesResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    trade_subscriptions: List['TradeSubscription'
        ] = _grpc_helpers.message_field(2)
    trade_source: 'TradeSourceType' = _grpc_helpers.message_field(3)


@dataclass
class TradeSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    subscription_status: 'SubscriptionStatus' = _grpc_helpers.message_field(2)
    instrument_uid: str = _grpc_helpers.string_field(3)
    stream_id: str = _grpc_helpers.string_field(4)
    subscription_id: str = _grpc_helpers.string_field(5)
    with_open_interest: bool = _grpc_helpers.bool_field(6)
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(7)


@dataclass
class SubscribeInfoRequest(_grpc_helpers.Message):
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(1)
    instruments: List['InfoInstrument'] = _grpc_helpers.message_field(2)


@dataclass
class InfoInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)


@dataclass
class SubscribeInfoResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    info_subscriptions: List['InfoSubscription'] = _grpc_helpers.message_field(
        2)


@dataclass
class InfoSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    subscription_status: 'SubscriptionStatus' = _grpc_helpers.message_field(2)
    instrument_uid: str = _grpc_helpers.string_field(3)
    stream_id: str = _grpc_helpers.string_field(4)
    subscription_id: str = _grpc_helpers.string_field(5)
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(6)


@dataclass
class SubscribeLastPriceRequest(_grpc_helpers.Message):
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(1)
    instruments: List['LastPriceInstrument'] = _grpc_helpers.message_field(2)


@dataclass
class LastPriceInstrument(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_id: str = _grpc_helpers.string_field(2)


@dataclass
class SubscribeLastPriceResponse(_grpc_helpers.Message):
    tracking_id: str = _grpc_helpers.string_field(1)
    last_price_subscriptions: List['LastPriceSubscription'
        ] = _grpc_helpers.message_field(2)


@dataclass
class LastPriceSubscription(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    subscription_status: 'SubscriptionStatus' = _grpc_helpers.message_field(2)
    instrument_uid: str = _grpc_helpers.string_field(3)
    stream_id: str = _grpc_helpers.string_field(4)
    subscription_id: str = _grpc_helpers.string_field(5)
    subscription_action: 'SubscriptionAction' = _grpc_helpers.message_field(6)


@dataclass
class Candle(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    interval: 'SubscriptionInterval' = _grpc_helpers.message_field(2)
    open: 'Quotation' = _grpc_helpers.message_field(3)
    high: 'Quotation' = _grpc_helpers.message_field(4)
    low: 'Quotation' = _grpc_helpers.message_field(5)
    close: 'Quotation' = _grpc_helpers.message_field(6)
    volume: int = _grpc_helpers.int64_field(7)
    time: datetime = _grpc_helpers.message_field(8)
    last_trade_ts: datetime = _grpc_helpers.message_field(9)
    instrument_uid: str = _grpc_helpers.string_field(10)
    candle_source_type: 'CandleSource' = _grpc_helpers.message_field(19)


@dataclass
class OrderBook(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    is_consistent: bool = _grpc_helpers.bool_field(3)
    bids: List['Order'] = _grpc_helpers.message_field(4)
    asks: List['Order'] = _grpc_helpers.message_field(5)
    time: datetime = _grpc_helpers.message_field(6)
    limit_up: 'Quotation' = _grpc_helpers.message_field(7)
    limit_down: 'Quotation' = _grpc_helpers.message_field(8)
    instrument_uid: str = _grpc_helpers.string_field(9)
    order_book_type: 'OrderBookType' = _grpc_helpers.message_field(10)


@dataclass
class Order(_grpc_helpers.Message):
    price: 'Quotation' = _grpc_helpers.message_field(1)
    quantity: int = _grpc_helpers.int64_field(2)


@dataclass
class Trade(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    direction: 'TradeDirection' = _grpc_helpers.message_field(2)
    price: 'Quotation' = _grpc_helpers.message_field(3)
    quantity: int = _grpc_helpers.int64_field(4)
    time: datetime = _grpc_helpers.message_field(5)
    instrument_uid: str = _grpc_helpers.string_field(6)
    trade_source: 'TradeSourceType' = _grpc_helpers.message_field(7)


@dataclass
class TradingStatus(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(2)
    time: datetime = _grpc_helpers.message_field(3)
    limit_order_available_flag: bool = _grpc_helpers.bool_field(4)
    market_order_available_flag: bool = _grpc_helpers.bool_field(5)
    instrument_uid: str = _grpc_helpers.string_field(6)


@dataclass
class GetCandlesRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)
    interval: 'CandleInterval' = _grpc_helpers.message_field(4)
    instrument_id: Optional[str] = _grpc_helpers.string_field(5, optional=True)
    candle_source_type: Optional['CandleSource'] = _grpc_helpers.message_field(
        7, optional=True)
    limit: Optional[int] = _grpc_helpers.int32_field(10, optional=True)


    class CandleSource(IntEnum):
        CANDLE_SOURCE_UNSPECIFIED = 0
        CANDLE_SOURCE_EXCHANGE = 1
        CANDLE_SOURCE_INCLUDE_WEEKEND = 3


@dataclass
class GetCandlesResponse(_grpc_helpers.Message):
    candles: List['HistoricCandle'] = _grpc_helpers.message_field(1)


@dataclass
class HistoricCandle(_grpc_helpers.Message):
    open: 'Quotation' = _grpc_helpers.message_field(1)
    high: 'Quotation' = _grpc_helpers.message_field(2)
    low: 'Quotation' = _grpc_helpers.message_field(3)
    close: 'Quotation' = _grpc_helpers.message_field(4)
    volume: int = _grpc_helpers.int64_field(5)
    time: datetime = _grpc_helpers.message_field(6)
    is_complete: bool = _grpc_helpers.bool_field(7)
    candle_source: 'CandleSource' = _grpc_helpers.message_field(9)


@dataclass
class GetLastPricesRequest(_grpc_helpers.Message):
    figi: List[str] = _grpc_helpers.string_field(1)
    instrument_id: List[str] = _grpc_helpers.string_field(2)
    last_price_type: 'LastPriceType' = _grpc_helpers.message_field(3)
    instrument_status: Optional['InstrumentStatus'
        ] = _grpc_helpers.message_field(9, optional=True)


@dataclass
class GetLastPricesResponse(_grpc_helpers.Message):
    last_prices: List['LastPrice'] = _grpc_helpers.message_field(1)


@dataclass
class LastPrice(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    price: 'Quotation' = _grpc_helpers.message_field(2)
    time: datetime = _grpc_helpers.message_field(3)
    instrument_uid: str = _grpc_helpers.string_field(11)
    last_price_type: 'LastPriceType' = _grpc_helpers.message_field(12)


@dataclass
class OpenInterest(_grpc_helpers.Message):
    instrument_uid: str = _grpc_helpers.string_field(1)
    time: datetime = _grpc_helpers.message_field(2)
    open_interest: int = _grpc_helpers.int64_field(3)


@dataclass
class GetOrderBookRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    depth: int = _grpc_helpers.int32_field(2)
    instrument_id: Optional[str] = _grpc_helpers.string_field(3, optional=True)


@dataclass
class GetOrderBookResponse(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    depth: int = _grpc_helpers.int32_field(2)
    bids: List['Order'] = _grpc_helpers.message_field(3)
    asks: List['Order'] = _grpc_helpers.message_field(4)
    last_price: 'Quotation' = _grpc_helpers.message_field(5)
    close_price: 'Quotation' = _grpc_helpers.message_field(6)
    limit_up: 'Quotation' = _grpc_helpers.message_field(7)
    limit_down: 'Quotation' = _grpc_helpers.message_field(8)
    last_price_ts: datetime = _grpc_helpers.message_field(21)
    close_price_ts: datetime = _grpc_helpers.message_field(22)
    orderbook_ts: datetime = _grpc_helpers.message_field(23)
    instrument_uid: str = _grpc_helpers.string_field(9)


@dataclass
class GetTradingStatusRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    instrument_id: Optional[str] = _grpc_helpers.string_field(2, optional=True)


@dataclass
class GetTradingStatusesRequest(_grpc_helpers.Message):
    instrument_id: List[str] = _grpc_helpers.string_field(1)


@dataclass
class GetTradingStatusesResponse(_grpc_helpers.Message):
    trading_statuses: List['GetTradingStatusResponse'
        ] = _grpc_helpers.message_field(1)


@dataclass
class GetTradingStatusResponse(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    trading_status: 'SecurityTradingStatus' = _grpc_helpers.message_field(2)
    limit_order_available_flag: bool = _grpc_helpers.bool_field(3)
    market_order_available_flag: bool = _grpc_helpers.bool_field(4)
    api_trade_available_flag: bool = _grpc_helpers.bool_field(5)
    instrument_uid: str = _grpc_helpers.string_field(6)
    bestprice_order_available_flag: bool = _grpc_helpers.bool_field(8)
    only_best_price: bool = _grpc_helpers.bool_field(9)


@dataclass
class GetLastTradesRequest(_grpc_helpers.Message):
    figi: Optional[str] = _grpc_helpers.string_field(1, optional=True)
    from_: datetime = _grpc_helpers.message_field(2)
    to: datetime = _grpc_helpers.message_field(3)
    instrument_id: Optional[str] = _grpc_helpers.string_field(4, optional=True)
    trade_source: 'TradeSourceType' = _grpc_helpers.message_field(5)


@dataclass
class GetLastTradesResponse(_grpc_helpers.Message):
    trades: List['Trade'] = _grpc_helpers.message_field(1)


@dataclass
class GetMySubscriptions(_grpc_helpers.Message):
    pass


@dataclass
class GetClosePricesRequest(_grpc_helpers.Message):
    instruments: List['InstrumentClosePriceRequest'
        ] = _grpc_helpers.message_field(1)
    instrument_status: Optional['InstrumentStatus'
        ] = _grpc_helpers.message_field(9, optional=True)


@dataclass
class InstrumentClosePriceRequest(_grpc_helpers.Message):
    instrument_id: str = _grpc_helpers.string_field(1)


@dataclass
class GetClosePricesResponse(_grpc_helpers.Message):
    close_prices: List['InstrumentClosePriceResponse'
        ] = _grpc_helpers.message_field(1)


@dataclass
class InstrumentClosePriceResponse(_grpc_helpers.Message):
    figi: str = _grpc_helpers.string_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)
    price: 'Quotation' = _grpc_helpers.message_field(11)
    evening_session_price: 'Quotation' = _grpc_helpers.message_field(12)
    time: datetime = _grpc_helpers.message_field(21)
    evening_session_price_time: datetime = _grpc_helpers.message_field(23)


@dataclass
class GetTechAnalysisRequest(_grpc_helpers.Message):
    indicator_type: 'IndicatorType' = _grpc_helpers.message_field(1)
    instrument_uid: str = _grpc_helpers.string_field(2)
    from_: datetime = _grpc_helpers.message_field(3)
    to: datetime = _grpc_helpers.message_field(4)
    interval: 'IndicatorInterval' = _grpc_helpers.message_field(5)
    type_of_price: 'TypeOfPrice' = _grpc_helpers.message_field(6)
    length: int = _grpc_helpers.int32_field(7)
    deviation: 'Deviation' = _grpc_helpers.message_field(8)
    smoothing: 'Smoothing' = _grpc_helpers.message_field(9)


    @dataclass
    class Smoothing(_grpc_helpers.Message):
        fast_length: int = _grpc_helpers.int32_field(1)
        slow_length: int = _grpc_helpers.int32_field(2)
        signal_smoothing: int = _grpc_helpers.int32_field(3)


    @dataclass
    class Deviation(_grpc_helpers.Message):
        deviation_multiplier: 'Quotation' = _grpc_helpers.message_field(1)


    class IndicatorInterval(IntEnum):
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


    class TypeOfPrice(IntEnum):
        TYPE_OF_PRICE_UNSPECIFIED = 0
        TYPE_OF_PRICE_CLOSE = 1
        TYPE_OF_PRICE_OPEN = 2
        TYPE_OF_PRICE_HIGH = 3
        TYPE_OF_PRICE_LOW = 4
        TYPE_OF_PRICE_AVG = 5


    class IndicatorType(IntEnum):
        INDICATOR_TYPE_UNSPECIFIED = 0
        INDICATOR_TYPE_BB = 1
        INDICATOR_TYPE_EMA = 2
        INDICATOR_TYPE_RSI = 3
        INDICATOR_TYPE_MACD = 4
        INDICATOR_TYPE_SMA = 5


@dataclass
class GetTechAnalysisResponse(_grpc_helpers.Message):
    technical_indicators: List['TechAnalysisItem'
        ] = _grpc_helpers.message_field(1)


    @dataclass
    class TechAnalysisItem(_grpc_helpers.Message):
        timestamp: datetime = _grpc_helpers.message_field(1)
        middle_band: Optional['Quotation'] = _grpc_helpers.message_field(2,
            optional=True)
        upper_band: Optional['Quotation'] = _grpc_helpers.message_field(3,
            optional=True)
        lower_band: Optional['Quotation'] = _grpc_helpers.message_field(4,
            optional=True)
        signal: Optional['Quotation'] = _grpc_helpers.message_field(5,
            optional=True)
        macd: Optional['Quotation'] = _grpc_helpers.message_field(6,
            optional=True)


@dataclass
class GetMarketValuesRequest(_grpc_helpers.Message):
    instrument_id: List[str] = _grpc_helpers.string_field(1)
    values: List['MarketValueType'] = _grpc_helpers.message_field(2)


@dataclass
class GetMarketValuesResponse(_grpc_helpers.Message):
    instruments: List['MarketValueInstrument'] = _grpc_helpers.message_field(1)


@dataclass
class MarketValueInstrument(_grpc_helpers.Message):
    instrument_uid: str = _grpc_helpers.string_field(1)
    values: List['MarketValue'] = _grpc_helpers.message_field(2)


@dataclass
class MarketValue(_grpc_helpers.Message):
    type: Optional['MarketValueType'] = _grpc_helpers.message_field(1,
        optional=True)
    value: Optional['Quotation'] = _grpc_helpers.message_field(2, optional=True
        )
    time: Optional[datetime] = _grpc_helpers.message_field(3, optional=True)


class MarketDataService(BaseService):
    """//Сервис для получения биржевой информации:<br/> 1. Свечи.<br/> 2. Стаканы.<br/> 3. Торговые статусы.<br/> 4. Лента сделок."""
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataServiceStub

    @handle_request_error('GetCandles')
    def get_candles(self, request: 'GetCandlesRequest'=GetCandlesRequest()
        ) ->'GetCandlesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetCandlesRequest())
        response, call = self._stub.GetCandles.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetCandles')
        return protobuf_to_dataclass(response, GetCandlesResponse)

    @handle_request_error('GetLastPrices')
    def get_last_prices(self, request: 'GetLastPricesRequest'=
        GetLastPricesRequest()) ->'GetLastPricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetLastPricesRequest())
        response, call = self._stub.GetLastPrices.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetLastPrices')
        return protobuf_to_dataclass(response, GetLastPricesResponse)

    @handle_request_error('GetOrderBook')
    def get_order_book(self, request: 'GetOrderBookRequest'=
        GetOrderBookRequest()) ->'GetOrderBookResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderBookRequest())
        response, call = self._stub.GetOrderBook.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetOrderBook')
        return protobuf_to_dataclass(response, GetOrderBookResponse)

    @handle_request_error('GetTradingStatus')
    def get_trading_status(self, request: 'GetTradingStatusRequest'=
        GetTradingStatusRequest()) ->'GetTradingStatusResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTradingStatusRequest())
        response, call = self._stub.GetTradingStatus.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetTradingStatus')
        return protobuf_to_dataclass(response, GetTradingStatusResponse)

    @handle_request_error('GetTradingStatuses')
    def get_trading_statuses(self, request: 'GetTradingStatusesRequest'=
        GetTradingStatusesRequest()) ->'GetTradingStatusesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTradingStatusesRequest())
        response, call = self._stub.GetTradingStatuses.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetTradingStatuses')
        return protobuf_to_dataclass(response, GetTradingStatusesResponse)

    @handle_request_error('GetLastTrades')
    def get_last_trades(self, request: 'GetLastTradesRequest'=
        GetLastTradesRequest()) ->'GetLastTradesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetLastTradesRequest())
        response, call = self._stub.GetLastTrades.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetLastTrades')
        return protobuf_to_dataclass(response, GetLastTradesResponse)

    @handle_request_error('GetClosePrices')
    def get_close_prices(self, request: 'GetClosePricesRequest'=
        GetClosePricesRequest()) ->'GetClosePricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetClosePricesRequest())
        response, call = self._stub.GetClosePrices.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetClosePrices')
        return protobuf_to_dataclass(response, GetClosePricesResponse)

    @handle_request_error('GetTechAnalysis')
    def get_tech_analysis(self, request: 'GetTechAnalysisRequest'=
        GetTechAnalysisRequest()) ->'GetTechAnalysisResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTechAnalysisRequest())
        response, call = self._stub.GetTechAnalysis.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetTechAnalysis')
        return protobuf_to_dataclass(response, GetTechAnalysisResponse)

    @handle_request_error('GetMarketValues')
    def get_market_values(self, request: 'GetMarketValuesRequest'=
        GetMarketValuesRequest()) ->'GetMarketValuesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMarketValuesRequest())
        response, call = self._stub.GetMarketValues.with_call(request=
            protobuf_request, metadata=self._metadata)
        log_request(get_tracking_id_from_call(call), 'GetMarketValues')
        return protobuf_to_dataclass(response, GetMarketValuesResponse)


class AsyncMarketDataService(BaseService):
    """//GetCandles — исторические свечи по инструменту"""
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataServiceStub

    @handle_aio_request_error('GetCandles')
    async def get_candles(self, request: 'GetCandlesRequest'=
        GetCandlesRequest()) ->'GetCandlesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetCandlesRequest())
        response_coro = self._stub.GetCandles(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetCandles')
        return protobuf_to_dataclass(response, GetCandlesResponse)

    @handle_aio_request_error('GetLastPrices')
    async def get_last_prices(self, request: 'GetLastPricesRequest'=
        GetLastPricesRequest()) ->'GetLastPricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetLastPricesRequest())
        response_coro = self._stub.GetLastPrices(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetLastPrices')
        return protobuf_to_dataclass(response, GetLastPricesResponse)

    @handle_aio_request_error('GetOrderBook')
    async def get_order_book(self, request: 'GetOrderBookRequest'=
        GetOrderBookRequest()) ->'GetOrderBookResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetOrderBookRequest())
        response_coro = self._stub.GetOrderBook(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetOrderBook')
        return protobuf_to_dataclass(response, GetOrderBookResponse)

    @handle_aio_request_error('GetTradingStatus')
    async def get_trading_status(self, request: 'GetTradingStatusRequest'=
        GetTradingStatusRequest()) ->'GetTradingStatusResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTradingStatusRequest())
        response_coro = self._stub.GetTradingStatus(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetTradingStatus')
        return protobuf_to_dataclass(response, GetTradingStatusResponse)

    @handle_aio_request_error('GetTradingStatuses')
    async def get_trading_statuses(self, request:
        'GetTradingStatusesRequest'=GetTradingStatusesRequest()
        ) ->'GetTradingStatusesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTradingStatusesRequest())
        response_coro = self._stub.GetTradingStatuses(request=
            protobuf_request, metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetTradingStatuses')
        return protobuf_to_dataclass(response, GetTradingStatusesResponse)

    @handle_aio_request_error('GetLastTrades')
    async def get_last_trades(self, request: 'GetLastTradesRequest'=
        GetLastTradesRequest()) ->'GetLastTradesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetLastTradesRequest())
        response_coro = self._stub.GetLastTrades(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetLastTrades')
        return protobuf_to_dataclass(response, GetLastTradesResponse)

    @handle_aio_request_error('GetClosePrices')
    async def get_close_prices(self, request: 'GetClosePricesRequest'=
        GetClosePricesRequest()) ->'GetClosePricesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetClosePricesRequest())
        response_coro = self._stub.GetClosePrices(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetClosePrices')
        return protobuf_to_dataclass(response, GetClosePricesResponse)

    @handle_aio_request_error('GetTechAnalysis')
    async def get_tech_analysis(self, request: 'GetTechAnalysisRequest'=
        GetTechAnalysisRequest()) ->'GetTechAnalysisResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetTechAnalysisRequest())
        response_coro = self._stub.GetTechAnalysis(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetTechAnalysis')
        return protobuf_to_dataclass(response, GetTechAnalysisResponse)

    @handle_aio_request_error('GetMarketValues')
    async def get_market_values(self, request: 'GetMarketValuesRequest'=
        GetMarketValuesRequest()) ->'GetMarketValuesResponse':
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            GetMarketValuesRequest())
        response_coro = self._stub.GetMarketValues(request=protobuf_request,
            metadata=self._metadata)
        response = await response_coro
        log_request(await get_tracking_id_from_coro(response_coro),
            'GetMarketValues')
        return protobuf_to_dataclass(response, GetMarketValuesResponse)


class MarketDataStreamService(BaseService):
    """//MarketDataStream — bidirectional стрим предоставления биржевой информации"""
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataStreamServiceStub

    @handle_request_error_gen('MarketDataStream')
    def market_data_stream(self, requests: Iterable['MarketDataRequest']
        ) ->Iterable['MarketDataResponse']:
        for response in self._stub.MarketDataStream(request_iterator=(
            dataclass_to_protobuf(request, self._protobuf.MarketDataRequest
            ()) for request in requests), metadata=self._metadata):
            yield protobuf_to_dataclass(response, MarketDataResponse)

    @handle_request_error_gen('MarketDataServerSideStream')
    def market_data_server_side_stream(self, request:
        'MarketDataServerSideStreamRequest'=MarketDataServerSideStreamRequest()
        ) ->Iterable['MarketDataResponse']:
        for response in self._stub.MarketDataServerSideStream(request=
            dataclass_to_protobuf(request, self._protobuf.
            MarketDataServerSideStreamRequest()), metadata=self._metadata):
            yield protobuf_to_dataclass(response, MarketDataResponse)


class AsyncMarketDataStreamService(BaseService):
    _protobuf = marketdata_pb2
    _protobuf_grpc = marketdata_pb2_grpc
    _protobuf_stub = _protobuf_grpc.MarketDataStreamServiceStub

    @handle_aio_request_error_gen('MarketDataStream')
    async def market_data_stream(self, request_iterator: AsyncIterable[
        'MarketDataRequest']) ->AsyncIterable['MarketDataResponse']:
        protobuf_request_iterator = (dataclass_to_protobuf(request, self.
            _protobuf.MarketDataRequest()) async for request in
            request_iterator)
        async for response in self._stub.MarketDataStream(request_iterator=
            protobuf_request_iterator, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, MarketDataResponse))

    @handle_aio_request_error_gen('MarketDataServerSideStream')
    async def market_data_server_side_stream(self, request:
        'MarketDataServerSideStreamRequest'=MarketDataServerSideStreamRequest()
        ) ->AsyncIterable['MarketDataResponse']:
        protobuf_request = dataclass_to_protobuf(request, self._protobuf.
            MarketDataServerSideStreamRequest())
        async for response in self._stub.MarketDataServerSideStream(request
            =protobuf_request, metadata=self._metadata):(yield
            protobuf_to_dataclass(response, MarketDataResponse))
