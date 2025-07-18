# pylint:disable=redefined-builtin,too-many-lines
import logging
from datetime import datetime
from typing import Generator, Iterable, Iterator, List, Optional

import grpc
from deprecation import deprecated

from . import _grpc_helpers, utils
from ._errors import handle_request_error, handle_request_error_gen
from .exceptions import RequestError
from .grpc import (
    instruments_pb2,
    instruments_pb2_grpc,
    marketdata_pb2,
    marketdata_pb2_grpc,
    operations_pb2,
    operations_pb2_grpc,
    orders_pb2,
    orders_pb2_grpc,
    sandbox_pb2,
    sandbox_pb2_grpc,
    signals_pb2,
    signals_pb2_grpc,
    stoporders_pb2,
    stoporders_pb2_grpc,
    users_pb2,
    users_pb2_grpc,
)
from .logging import get_tracking_id_from_call, log_request
from .market_data_stream.market_data_stream_manager import MarketDataStreamManager
from .metadata import get_metadata
from .schemas import (
    AssetRequest,
    AssetResponse,
    AssetsRequest,
    AssetsResponse,
    BondResponse,
    BondsResponse,
    Brand,
    BrokerReportRequest,
    BrokerReportResponse,
    CancelOrderRequest,
    CancelOrderResponse,
    CancelStopOrderRequest,
    CancelStopOrderResponse,
    CandleInterval,
    CandleSource,
    CloseSandboxAccountRequest,
    CloseSandboxAccountResponse,
    CreateFavoriteGroupRequest,
    CreateFavoriteGroupResponse,
    CurrenciesResponse,
    CurrencyResponse,
    DeleteFavoriteGroupRequest,
    DeleteFavoriteGroupResponse,
    EditFavoritesActionType,
    EditFavoritesRequest,
    EditFavoritesRequestInstrument,
    EditFavoritesResponse,
    EtfResponse,
    EtfsResponse,
    ExchangeOrderType,
    FilterOptionsRequest,
    FindInstrumentRequest,
    FindInstrumentResponse,
    FutureResponse,
    FuturesResponse,
    GenerateBrokerReportRequest,
    GenerateDividendsForeignIssuerReportRequest,
    GetAccountsRequest,
    GetAccountsResponse,
    GetAccruedInterestsRequest,
    GetAccruedInterestsResponse,
    GetAssetFundamentalsRequest,
    GetAssetFundamentalsResponse,
    GetAssetReportsRequest,
    GetAssetReportsResponse,
    GetBondCouponsRequest,
    GetBondCouponsResponse,
    GetBondEventsRequest,
    GetBondEventsResponse,
    GetBrandRequest,
    GetBrandsRequest,
    GetBrandsResponse,
    GetBrokerReportRequest,
    GetCandlesRequest,
    GetCandlesResponse,
    GetClosePricesRequest,
    GetClosePricesResponse,
    GetConsensusForecastsRequest,
    GetConsensusForecastsResponse,
    GetCountriesRequest,
    GetCountriesResponse,
    GetDividendsForeignIssuerReportRequest,
    GetDividendsForeignIssuerRequest,
    GetDividendsForeignIssuerResponse,
    GetDividendsRequest,
    GetDividendsResponse,
    GetFavoriteGroupsRequest,
    GetFavoriteGroupsResponse,
    GetFavoritesRequest,
    GetFavoritesResponse,
    GetForecastRequest,
    GetForecastResponse,
    GetFuturesMarginRequest,
    GetFuturesMarginResponse,
    GetInfoRequest,
    GetInfoResponse,
    GetLastPricesRequest,
    GetLastPricesResponse,
    GetLastTradesRequest,
    GetLastTradesResponse,
    GetMarginAttributesRequest,
    GetMarginAttributesResponse,
    GetMarketValuesRequest,
    GetMarketValuesResponse,
    GetMaxLotsRequest,
    GetMaxLotsResponse,
    GetOperationsByCursorRequest,
    GetOperationsByCursorResponse,
    GetOrderBookRequest,
    GetOrderBookResponse,
    GetOrderPriceRequest,
    GetOrderPriceResponse,
    GetOrdersRequest,
    GetOrdersResponse,
    GetOrderStateRequest,
    GetSignalsRequest,
    GetSignalsResponse,
    GetStopOrdersRequest,
    GetStopOrdersResponse,
    GetStrategiesRequest,
    GetStrategiesResponse,
    GetTechAnalysisRequest,
    GetTechAnalysisResponse,
    GetTradingStatusesRequest,
    GetTradingStatusesResponse,
    GetTradingStatusRequest,
    GetTradingStatusResponse,
    GetUserTariffRequest,
    GetUserTariffResponse,
    HistoricCandle,
    IndicativesRequest,
    IndicativesResponse,
    InstrumentClosePriceRequest,
    InstrumentExchangeType,
    InstrumentIdType,
    InstrumentRequest,
    InstrumentResponse,
    InstrumentsRequest,
    InstrumentStatus,
    InstrumentType,
    LastPriceType,
    MarketDataRequest,
    MarketDataResponse,
    MarketDataServerSideStreamRequest,
    MoneyValue,
    OpenSandboxAccountRequest,
    OpenSandboxAccountResponse,
    OperationsRequest,
    OperationsResponse,
    OperationState,
    OptionResponse,
    OptionsResponse,
    OrderDirection,
    OrderIdType,
    OrderState,
    OrderStateStreamRequest,
    OrderStateStreamResponse,
    OrderType,
    Page,
    PingDelaySettings,
    PortfolioRequest,
    PortfolioResponse,
    PortfolioStreamRequest,
    PortfolioStreamResponse,
    PositionsRequest,
    PositionsResponse,
    PositionsStreamRequest,
    PositionsStreamResponse,
    PostOrderAsyncRequest,
    PostOrderAsyncResponse,
    PostOrderRequest,
    PostOrderResponse,
    PostStopOrderRequest,
    PostStopOrderRequestTrailingData,
    PostStopOrderResponse,
    PriceType,
    Quotation,
    ReplaceOrderRequest,
    RiskRatesRequest,
    RiskRatesResponse,
    SandboxPayInRequest,
    SandboxPayInResponse,
    ShareResponse,
    SharesResponse,
    StopOrderDirection,
    StopOrderExpirationType,
    StopOrderStatusOption,
    StopOrderType,
    TakeProfitType,
    TimeInForceType,
    TradeSourceType,
    TradesStreamRequest,
    TradesStreamResponse,
    TradingSchedulesRequest,
    TradingSchedulesResponse,
    WithdrawLimitsRequest,
    WithdrawLimitsResponse,
)
from .typedefs import AccountId
from .utils import get_intervals, now

__all__ = (
    "Services",
    "InstrumentsService",
    "MarketDataService",
    "MarketDataStreamService",
    "OperationsService",
    "OperationsStreamService",
    "OrdersStreamService",
    "OrdersService",
    "UsersService",
    "SandboxService",
    "StopOrdersService",
    "SignalService",
)
logger = logging.getLogger(__name__)


class Services:
    def __init__(
        self,
        channel: grpc.Channel,
        token: str,
        sandbox_token: Optional[str] = None,
        app_name: Optional[str] = None,
    ) -> None:
        metadata = get_metadata(token, app_name)
        sandbox_metadata = get_metadata(sandbox_token or token, app_name)
        self.instruments = InstrumentsService(channel, metadata)
        self.market_data = MarketDataService(channel, metadata)
        self.market_data_stream = MarketDataStreamService(channel, metadata)
        self.operations = OperationsService(channel, metadata)
        self.operations_stream = OperationsStreamService(channel, metadata)
        self.orders_stream = OrdersStreamService(channel, metadata)
        self.orders = OrdersService(channel, metadata)
        self.users = UsersService(channel, metadata)
        self.sandbox = SandboxService(channel, sandbox_metadata)
        self.stop_orders = StopOrdersService(channel, metadata)
        self.signals = SignalService(channel, metadata)

    def create_market_data_stream(self) -> MarketDataStreamManager:
        return MarketDataStreamManager(
            market_data_stream_service=self.market_data_stream
        )

    def cancel_all_orders(self, account_id: AccountId) -> None:
        orders_service: OrdersService = self.orders
        stop_orders_service: StopOrdersService = self.stop_orders

        orders_response = orders_service.get_orders(account_id=account_id)
        for order in orders_response.orders:
            orders_service.cancel_order(account_id=account_id, order_id=order.order_id)

        stop_orders_response = stop_orders_service.get_stop_orders(
            account_id=account_id
        )
        for stop_order in stop_orders_response.stop_orders:
            stop_orders_service.cancel_stop_order(
                account_id=account_id, stop_order_id=stop_order.stop_order_id
            )

    # pylint:disable=too-many-nested-blocks
    def get_all_candles(
        self,
        *,
        from_: datetime,
        to: Optional[datetime] = None,
        interval: CandleInterval = CandleInterval(0),
        figi: str = "",
        instrument_id: str = "",
        candle_source_type: Optional[CandleSource] = None,
    ) -> Generator[HistoricCandle, None, None]:
        to = to or now()

        previous_candles = set()
        for current_from, current_to in get_intervals(interval, from_, to):
            candles_response: GetCandlesResponse = self.market_data.get_candles(
                figi=figi,
                interval=interval,
                from_=current_from,
                to=current_to,
                instrument_id=instrument_id,
                candle_source_type=candle_source_type,
            )

            for candle in candles_response.candles:
                if candle not in previous_candles:
                    yield candle
                    previous_candles.add(candle)

            previous_candles = set(candles_response.candles)


class InstrumentsService(_grpc_helpers.Service):
    _stub_factory = instruments_pb2_grpc.InstrumentsServiceStub

    @handle_request_error("TradingSchedules")
    def trading_schedules(
        self,
        *,
        exchange: str = "",
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
    ) -> TradingSchedulesResponse:
        request = TradingSchedulesRequest()
        request.exchange = exchange
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        response, call = self.stub.TradingSchedules.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.TradingSchedulesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "TradingSchedules")
        return _grpc_helpers.protobuf_to_dataclass(response, TradingSchedulesResponse)

    @handle_request_error("BondBy")
    def bond_by(
        self,
        *,
        id_type: InstrumentIdType = InstrumentIdType(0),
        class_code: str = "",
        id: str = "",
    ) -> BondResponse:
        request = InstrumentRequest()
        request.id_type = id_type
        request.class_code = class_code
        request.id = id
        response, call = self.stub.BondBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "BondBy")
        return _grpc_helpers.protobuf_to_dataclass(response, BondResponse)

    @handle_request_error("Bonds")
    def bonds(
        self,
        *,
        instrument_status: InstrumentStatus = InstrumentStatus(0),
        instrument_exchange: InstrumentExchangeType = InstrumentExchangeType(0),
    ) -> BondsResponse:
        request = InstrumentsRequest()
        request.instrument_status = instrument_status
        request.instrument_exchange = instrument_exchange
        response, call = self.stub.Bonds.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "Bonds")
        return _grpc_helpers.protobuf_to_dataclass(response, BondsResponse)

    @handle_request_error("CurrencyBy")
    def currency_by(
        self,
        *,
        id_type: InstrumentIdType = InstrumentIdType(0),
        class_code: str = "",
        id: str = "",
    ) -> CurrencyResponse:
        request = InstrumentRequest()
        request.id_type = id_type
        request.class_code = class_code
        request.id = id
        response, call = self.stub.CurrencyBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "CurrencyBy")
        return _grpc_helpers.protobuf_to_dataclass(response, CurrencyResponse)

    @handle_request_error("Currencies")
    def currencies(
        self,
        *,
        instrument_status: InstrumentStatus = InstrumentStatus(0),
        instrument_exchange: InstrumentExchangeType = InstrumentExchangeType(0),
    ) -> CurrenciesResponse:
        request = InstrumentsRequest()
        request.instrument_status = instrument_status
        request.instrument_exchange = instrument_exchange
        response, call = self.stub.Currencies.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "Currencies")
        return _grpc_helpers.protobuf_to_dataclass(response, CurrenciesResponse)

    @handle_request_error("EtfBy")
    def etf_by(
        self,
        *,
        id_type: InstrumentIdType = InstrumentIdType(0),
        class_code: str = "",
        id: str = "",
    ) -> EtfResponse:
        request = InstrumentRequest()
        request.id_type = id_type
        request.class_code = class_code
        request.id = id
        response, call = self.stub.EtfBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "EtfBy")
        return _grpc_helpers.protobuf_to_dataclass(response, EtfResponse)

    @handle_request_error("Etfs")
    def etfs(
        self,
        *,
        instrument_status: InstrumentStatus = InstrumentStatus(0),
        instrument_exchange: InstrumentExchangeType = InstrumentExchangeType(0),
    ) -> EtfsResponse:
        request = InstrumentsRequest()
        request.instrument_status = instrument_status
        request.instrument_exchange = instrument_exchange
        response, call = self.stub.Etfs.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "Etfs")
        return _grpc_helpers.protobuf_to_dataclass(response, EtfsResponse)

    @handle_request_error("FutureBy")
    def future_by(
        self,
        *,
        id_type: InstrumentIdType = InstrumentIdType(0),
        class_code: str = "",
        id: str = "",
    ) -> FutureResponse:
        request = InstrumentRequest()
        request.id_type = id_type
        request.class_code = class_code
        request.id = id
        response, call = self.stub.FutureBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "FutureBy")
        return _grpc_helpers.protobuf_to_dataclass(response, FutureResponse)

    @handle_request_error("Futures")
    def futures(
        self,
        *,
        instrument_status: InstrumentStatus = InstrumentStatus(0),
        instrument_exchange: InstrumentExchangeType = InstrumentExchangeType(0),
    ) -> FuturesResponse:
        request = InstrumentsRequest()
        request.instrument_status = instrument_status
        request.instrument_exchange = instrument_exchange
        response, call = self.stub.Futures.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "Futures")
        return _grpc_helpers.protobuf_to_dataclass(response, FuturesResponse)

    @handle_request_error("OptionBy")
    def option_by(
        self,
        *,
        id_type: InstrumentIdType = InstrumentIdType(0),
        class_code: str = "",
        id: str = "",
    ) -> OptionResponse:
        request = InstrumentRequest()
        request.id_type = id_type
        request.class_code = class_code
        request.id = id
        response, call = self.stub.OptionBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "OptionBy")
        return _grpc_helpers.protobuf_to_dataclass(response, OptionResponse)

    @deprecated(details="Use `Client.instruments.options_by(...)` method instead")
    @handle_request_error("Options")
    def options(
        self,
        *,
        instrument_status: InstrumentStatus = InstrumentStatus(0),
        instrument_exchange: InstrumentExchangeType = InstrumentExchangeType(0),
    ) -> OptionsResponse:
        request = InstrumentsRequest()
        request.instrument_status = instrument_status
        request.instrument_exchange = instrument_exchange
        response, call = self.stub.Options.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "Options")
        return _grpc_helpers.protobuf_to_dataclass(response, OptionsResponse)

    @handle_request_error("OptionsBy")
    def options_by(
        self, *, basic_asset_uid: str = "", basic_asset_position_uid: str = ""
    ) -> OptionsResponse:
        request = FilterOptionsRequest()
        request.basic_asset_uid = basic_asset_uid
        request.basic_asset_position_uid = basic_asset_position_uid
        response, call = self.stub.OptionsBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.FilterOptionsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "OptionsBy")
        return _grpc_helpers.protobuf_to_dataclass(response, OptionsResponse)

    @handle_request_error("ShareBy")
    def share_by(
        self,
        *,
        id_type: InstrumentIdType = InstrumentIdType(0),
        class_code: str = "",
        id: str = "",
    ) -> ShareResponse:
        request = InstrumentRequest()
        request.id_type = id_type
        request.class_code = class_code
        request.id = id
        response, call = self.stub.ShareBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "ShareBy")
        return _grpc_helpers.protobuf_to_dataclass(response, ShareResponse)

    @handle_request_error("Shares")
    def shares(
        self,
        *,
        instrument_status: InstrumentStatus = InstrumentStatus(0),
        instrument_exchange: InstrumentExchangeType = InstrumentExchangeType(0),
    ) -> SharesResponse:
        request = InstrumentsRequest()
        request.instrument_status = instrument_status
        request.instrument_exchange = instrument_exchange
        response, call = self.stub.Shares.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "Shares")
        return _grpc_helpers.protobuf_to_dataclass(response, SharesResponse)

    @handle_request_error("Indicatives")
    def indicatives(
        self,
        request: IndicativesRequest,
    ) -> IndicativesResponse:
        response, call = self.stub.Indicatives.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "Indicatives")
        return _grpc_helpers.protobuf_to_dataclass(response, IndicativesResponse)

    @handle_request_error("GetAccruedInterests")
    def get_accrued_interests(
        self,
        *,
        figi: str = "",
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
        instrument_id: str = "",
    ) -> GetAccruedInterestsResponse:
        request = GetAccruedInterestsRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        response, call = self.stub.GetAccruedInterests.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetAccruedInterestsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetAccruedInterests")
        return _grpc_helpers.protobuf_to_dataclass(
            response, GetAccruedInterestsResponse
        )

    @handle_request_error("GetFuturesMargin")
    def get_futures_margin(
        self, *, figi: str = "", instrument_id: str = ""
    ) -> GetFuturesMarginResponse:
        request = GetFuturesMarginRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        response, call = self.stub.GetFuturesMargin.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetFuturesMarginRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetFuturesMargin")
        return _grpc_helpers.protobuf_to_dataclass(response, GetFuturesMarginResponse)

    @handle_request_error("GetInstrumentBy")
    def get_instrument_by(
        self,
        *,
        id_type: InstrumentIdType = InstrumentIdType(0),
        class_code: str = "",
        id: str = "",
    ) -> InstrumentResponse:
        request = InstrumentRequest()
        request.id_type = id_type
        request.class_code = class_code
        request.id = id
        response, call = self.stub.GetInstrumentBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.InstrumentRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetInstrumentBy")
        return _grpc_helpers.protobuf_to_dataclass(response, InstrumentResponse)

    @handle_request_error("GetDividends")
    def get_dividends(
        self,
        *,
        figi: str = "",
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
        instrument_id: str = "",
    ) -> GetDividendsResponse:
        request = GetDividendsRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        response, call = self.stub.GetDividends.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetDividendsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetDividends")
        return _grpc_helpers.protobuf_to_dataclass(response, GetDividendsResponse)

    @handle_request_error("GetBondCoupons")
    def get_bond_coupons(
        self,
        *,
        figi: str = "",
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
        instrument_id: str = "",
    ) -> GetBondCouponsResponse:
        request = GetBondCouponsRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        response, call = self.stub.GetBondCoupons.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetBondCouponsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetBondCoupons")
        return _grpc_helpers.protobuf_to_dataclass(response, GetBondCouponsResponse)

    @handle_request_error("GetBondEvents")
    def get_bond_events(self, request: GetBondEventsRequest) -> GetBondEventsResponse:
        response, call = self.stub.GetBondEvents.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetBondEventsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetBondEvents")
        return _grpc_helpers.protobuf_to_dataclass(response, GetBondEventsResponse)

    @handle_request_error("GetAssetBy")
    def get_asset_by(
        self,
        *,
        id: str = "",
    ) -> AssetResponse:
        request = AssetRequest()
        request.id = id
        response, call = self.stub.GetAssetBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.AssetRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetAssetBy")
        return _grpc_helpers.protobuf_to_dataclass(response, AssetResponse)

    @handle_request_error("GetAssets")
    def get_assets(
        self,
        request: AssetsRequest,
    ) -> AssetsResponse:
        if request is None:
            request = AssetsRequest()
        response, call = self.stub.GetAssets.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.AssetsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetAssets")
        return _grpc_helpers.protobuf_to_dataclass(response, AssetsResponse)

    @handle_request_error("GetFavorites")
    def get_favorites(
        self,
        *,
        group_id: Optional[str] = None,
    ) -> GetFavoritesResponse:
        request = GetFavoritesRequest()
        if group_id is not None:
            request.group_id = group_id
        response, call = self.stub.GetFavorites.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetFavoritesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetFavorites")
        return _grpc_helpers.protobuf_to_dataclass(response, GetFavoritesResponse)

    @handle_request_error("EditFavorites")
    def edit_favorites(
        self,
        *,
        instruments: Optional[List[EditFavoritesRequestInstrument]] = None,
        action_type: Optional[EditFavoritesActionType] = None,
        group_id: Optional[str] = None,
    ) -> EditFavoritesResponse:
        request = EditFavoritesRequest()
        if action_type is not None:
            request.action_type = action_type
        if instruments is not None:
            request.instruments = instruments
        if group_id is not None:
            request.group_id = group_id
        response, call = self.stub.EditFavorites.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.EditFavoritesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "EditFavorites")
        return _grpc_helpers.protobuf_to_dataclass(response, EditFavoritesResponse)

    @handle_request_error("CreateFavoriteGroup")
    def create_favorite_group(
        self,
        request: CreateFavoriteGroupRequest,
    ) -> CreateFavoriteGroupResponse:
        response, call = self.stub.CreateFavoriteGroup.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.CreateFavoriteGroupRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "CreateFavoriteGroup")
        return _grpc_helpers.protobuf_to_dataclass(
            response, CreateFavoriteGroupResponse
        )

    @handle_request_error("DeleteFavoriteGroup")
    def delete_favorite_group(
        self,
        request: DeleteFavoriteGroupRequest,
    ) -> DeleteFavoriteGroupResponse:
        response, call = self.stub.DeleteFavoriteGroup.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.DeleteFavoriteGroupRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "DeleteFavoriteGroup")
        return _grpc_helpers.protobuf_to_dataclass(
            response, DeleteFavoriteGroupResponse
        )

    @handle_request_error("GetFavoriteGroups")
    def get_favorite_groups(
        self,
        request: GetFavoriteGroupsRequest,
    ) -> GetFavoriteGroupsResponse:
        response, call = self.stub.GetFavoriteGroups.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetFavoriteGroupsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetFavoriteGroups")
        return _grpc_helpers.protobuf_to_dataclass(response, GetFavoriteGroupsResponse)

    @handle_request_error("GetCountries")
    def get_countries(
        self,
    ) -> GetCountriesResponse:
        request = GetCountriesRequest()
        response, call = self.stub.GetCountries.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetCountriesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetCountries")
        return _grpc_helpers.protobuf_to_dataclass(response, GetCountriesResponse)

    @handle_request_error("FindInstrument")
    def find_instrument(
        self,
        *,
        query: str = "",
        instrument_kind: Optional[InstrumentType] = None,
        api_trade_available_flag: Optional[bool] = None,
    ) -> FindInstrumentResponse:
        request = FindInstrumentRequest()
        request.query = query
        if instrument_kind is not None:
            request.instrument_kind = instrument_kind
        if api_trade_available_flag is not None:
            request.api_trade_available_flag = api_trade_available_flag
        response, call = self.stub.FindInstrument.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.FindInstrumentRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "FindInstrument")
        return _grpc_helpers.protobuf_to_dataclass(response, FindInstrumentResponse)

    @handle_request_error("GetBrands")
    def get_brands(
        self,
        paging: Optional[Page] = None,
    ) -> GetBrandsResponse:
        request = GetBrandsRequest()
        if paging is not None:
            request.paging = paging
        response, call = self.stub.GetBrands.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetBrandsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetBrands")
        return _grpc_helpers.protobuf_to_dataclass(response, GetBrandsResponse)

    @handle_request_error("GetBrandBy")
    def get_brands_by(self, id: str = "") -> Brand:
        request = GetBrandRequest()
        request.id = id
        response, call = self.stub.GetBrandBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetBrandRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetBrandBy")
        return _grpc_helpers.protobuf_to_dataclass(response, Brand)

    @handle_request_error("GetAssetFundamentals")
    def get_asset_fundamentals(
        self, request: GetAssetFundamentalsRequest
    ) -> GetAssetFundamentalsResponse:
        response, call = self.stub.GetAssetFundamentals.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetAssetFundamentalsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetAssetFundamentals")
        return _grpc_helpers.protobuf_to_dataclass(
            response, GetAssetFundamentalsResponse
        )

    @handle_request_error("GetAssetReports")
    def get_asset_reports(
        self, request: GetAssetReportsRequest
    ) -> GetAssetReportsResponse:
        response, call = self.stub.GetAssetReports.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetAssetReportsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetAssetReports")
        return _grpc_helpers.protobuf_to_dataclass(response, GetAssetReportsResponse)

    @handle_request_error("GetConsensusForecasts")
    def get_consensus_forecasts(
        self, request: GetConsensusForecastsRequest
    ) -> GetConsensusForecastsResponse:
        response, call = self.stub.GetConsensusForecasts.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetConsensusForecastsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetConsensusForecasts")
        return _grpc_helpers.protobuf_to_dataclass(
            response, GetConsensusForecastsResponse
        )

    @handle_request_error("GetForecastBy")
    def get_forecast_by(self, request: GetForecastRequest) -> GetForecastResponse:
        response, call = self.stub.GetForecastBy.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.GetForecastRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetForecastBy")
        return _grpc_helpers.protobuf_to_dataclass(response, GetForecastResponse)

    @handle_request_error("GetRiskRates")
    def get_risk_rates(self, request: RiskRatesRequest) -> RiskRatesResponse:
        response, call = self.stub.GetRiskRates.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, instruments_pb2.RiskRatesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetRiskRates")
        return _grpc_helpers.protobuf_to_dataclass(response, RiskRatesResponse)


class MarketDataService(_grpc_helpers.Service):
    _stub_factory = marketdata_pb2_grpc.MarketDataServiceStub

    @handle_request_error("GetCandles")
    def get_candles(
        self,
        *,
        figi: str = "",
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
        interval: CandleInterval = CandleInterval(0),
        instrument_id: str = "",
        candle_source_type: Optional[CandleSource] = None,
        limit: Optional[int] = None,
    ) -> GetCandlesResponse:
        request = GetCandlesRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        request.candle_source_type = candle_source_type
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        if limit is not None:
            request.limit = limit
        request.interval = interval
        response, call = self.stub.GetCandles.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetCandlesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetCandles")
        return _grpc_helpers.protobuf_to_dataclass(response, GetCandlesResponse)

    @handle_request_error("GetLastPrices")
    def get_last_prices(
        self,
        *,
        figi: Optional[List[str]] = None,
        instrument_id: Optional[List[str]] = None,
        last_price_type: LastPriceType = LastPriceType.LAST_PRICE_UNSPECIFIED,
        instrument_status: Optional[InstrumentStatus] = None,
    ) -> GetLastPricesResponse:
        figi = figi or []
        instrument_id = instrument_id or []

        request = GetLastPricesRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        request.last_price_type = last_price_type
        if instrument_status:
            request.instrument_status = instrument_status
        response, call = self.stub.GetLastPrices.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetLastPricesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetLastPrices")
        return _grpc_helpers.protobuf_to_dataclass(response, GetLastPricesResponse)

    @handle_request_error("GetOrderBook")
    def get_order_book(
        self, *, figi: str = "", depth: int = 0, instrument_id: str = ""
    ) -> GetOrderBookResponse:
        request = GetOrderBookRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        request.depth = depth
        response, call = self.stub.GetOrderBook.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetOrderBookRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetOrderBook")
        return _grpc_helpers.protobuf_to_dataclass(response, GetOrderBookResponse)

    @handle_request_error("GetTradingStatus")
    def get_trading_status(
        self, *, figi: str = "", instrument_id: str = ""
    ) -> GetTradingStatusResponse:
        request = GetTradingStatusRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        response, call = self.stub.GetTradingStatus.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetTradingStatusRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetTradingStatus")
        return _grpc_helpers.protobuf_to_dataclass(response, GetTradingStatusResponse)

    @handle_request_error("GetTradingStatuses")
    def get_trading_statuses(
        self, *, instrument_ids: Optional[List[str]] = None
    ) -> GetTradingStatusesResponse:
        request = GetTradingStatusesRequest()
        if instrument_ids:
            request.instrument_id = instrument_ids
        response, call = self.stub.GetTradingStatuses.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetTradingStatusesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetTradingStatuses")
        return _grpc_helpers.protobuf_to_dataclass(response, GetTradingStatusesResponse)

    @handle_request_error("GetLastTrades")
    def get_last_trades(
        self,
        *,
        figi: str = "",
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
        instrument_id: str = "",
        trade_source: "TradeSourceType" = TradeSourceType.TRADE_SOURCE_UNSPECIFIED,
    ) -> GetLastTradesResponse:
        request = GetLastTradesRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        if trade_source is not None:
            request.trade_source = trade_source
        response, call = self.stub.GetLastTrades.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetLastTradesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetLastTrades")
        return _grpc_helpers.protobuf_to_dataclass(response, GetLastTradesResponse)

    @handle_request_error("GetClosePrices")
    def get_close_prices(
        self,
        *,
        instruments: Optional[List[InstrumentClosePriceRequest]] = None,
        instrument_status: Optional[InstrumentStatus] = None,
    ) -> GetClosePricesResponse:
        request = GetClosePricesRequest()
        if instruments:
            request.instruments = instruments
        if instrument_status:
            request.instrument_status = instrument_status
        response, call = self.stub.GetClosePrices.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetClosePricesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetClosePrices")
        return _grpc_helpers.protobuf_to_dataclass(response, GetClosePricesResponse)

    @handle_request_error("GetTechAnalysis")
    def get_tech_analysis(
        self,
        *,
        request: GetTechAnalysisRequest,
    ) -> GetTechAnalysisResponse:
        response, call = self.stub.GetTechAnalysis.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetTechAnalysisRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetTechAnalysis")
        return _grpc_helpers.protobuf_to_dataclass(response, GetTechAnalysisResponse)

    @handle_request_error("GetMarketValues")
    def get_market_values(
        self,
        *,
        request: GetMarketValuesRequest,
    ) -> GetMarketValuesResponse:
        response, call = self.stub.GetMarketValues.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.GetMarketValuesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetMarketValues")
        return _grpc_helpers.protobuf_to_dataclass(response, GetMarketValuesResponse)


class MarketDataStreamService(_grpc_helpers.Service):
    _stub_factory = marketdata_pb2_grpc.MarketDataStreamServiceStub

    @staticmethod
    def _convert_market_data_stream_request(
        request_iterator: Iterable[MarketDataRequest],
    ) -> Iterable[marketdata_pb2.MarketDataRequest]:
        for request in request_iterator:
            yield _grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.MarketDataRequest()
            )

    @handle_request_error_gen("MarketDataStream")
    def market_data_stream(
        self,
        request_iterator: Iterable[MarketDataRequest],
    ) -> Iterator[MarketDataResponse]:
        for response in self.stub.MarketDataStream(
            request_iterator=self._convert_market_data_stream_request(request_iterator),
            metadata=self.metadata,
        ):
            yield _grpc_helpers.protobuf_to_dataclass(response, MarketDataResponse)

    @staticmethod
    def _convert_market_data_server_side_stream_request(
        request_iterator: Iterable[MarketDataServerSideStreamRequest],
    ) -> Iterable[marketdata_pb2.MarketDataServerSideStreamRequest]:
        for request in request_iterator:
            yield _grpc_helpers.dataclass_to_protobuff(
                request, marketdata_pb2.MarketDataServerSideStreamRequest()
            )

    @handle_request_error_gen("MarketDataServerSideStream")
    def market_data_server_side_stream(
        self,
        request_iterator: Iterable[MarketDataServerSideStreamRequest],
    ) -> Iterable[MarketDataResponse]:
        for response in self.stub.MarketDataServerSideStream(
            request_iterator=self._convert_market_data_server_side_stream_request(
                request_iterator
            ),
            metadata=self.metadata,
        ):
            yield _grpc_helpers.protobuf_to_dataclass(response, MarketDataResponse)


class OperationsService(_grpc_helpers.Service):
    _stub_factory = operations_pb2_grpc.OperationsServiceStub

    @handle_request_error("GetOperations")
    def get_operations(
        self,
        *,
        account_id: str = "",
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
        state: OperationState = OperationState(0),
        figi: str = "",
    ) -> OperationsResponse:
        request = OperationsRequest()
        request.account_id = account_id
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        request.state = state
        request.figi = figi
        response, call = self.stub.GetOperations.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.OperationsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetOperations")
        return _grpc_helpers.protobuf_to_dataclass(response, OperationsResponse)

    @handle_request_error("GetPortfolio")
    def get_portfolio(self, *, account_id: str = "") -> PortfolioResponse:
        request = PortfolioRequest()
        request.account_id = account_id
        response, call = self.stub.GetPortfolio.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.PortfolioRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetPortfolio")
        return _grpc_helpers.protobuf_to_dataclass(response, PortfolioResponse)

    @handle_request_error("GetPositions")
    def get_positions(self, *, account_id: str = "") -> PositionsResponse:
        request = PositionsRequest()
        request.account_id = account_id
        response, call = self.stub.GetPositions.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.PositionsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetPositions")
        return _grpc_helpers.protobuf_to_dataclass(response, PositionsResponse)

    @handle_request_error("GetWithdrawLimits")
    def get_withdraw_limits(self, *, account_id: str = "") -> WithdrawLimitsResponse:
        request = WithdrawLimitsRequest()
        request.account_id = account_id
        response, call = self.stub.GetWithdrawLimits.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.WithdrawLimitsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetWithdrawLimits")
        return _grpc_helpers.protobuf_to_dataclass(response, WithdrawLimitsResponse)

    @handle_request_error("GetBrokerReport")
    def get_broker_report(
        self,
        *,
        generate_broker_report_request: Optional[GenerateBrokerReportRequest] = None,
        get_broker_report_request: Optional[GetBrokerReportRequest] = None,
    ) -> BrokerReportResponse:
        request = BrokerReportRequest()
        if generate_broker_report_request:
            request.generate_broker_report_request = generate_broker_report_request
        if get_broker_report_request:
            request.get_broker_report_request = get_broker_report_request
        response, call = self.stub.GetBrokerReport.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.BrokerReportRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetBrokerReport")
        return _grpc_helpers.protobuf_to_dataclass(response, BrokerReportResponse)

    @handle_request_error("GetDividendsForeignIssuer")
    def get_dividends_foreign_issuer(
        self,
        *,
        generate_div_foreign_issuer_report: Optional[
            GenerateDividendsForeignIssuerReportRequest
        ] = None,
        get_div_foreign_issuer_report: Optional[
            GetDividendsForeignIssuerReportRequest
        ] = None,
    ) -> GetDividendsForeignIssuerResponse:
        request = GetDividendsForeignIssuerRequest()
        if generate_div_foreign_issuer_report is not None:
            request.generate_div_foreign_issuer_report = (
                generate_div_foreign_issuer_report
            )
        if get_div_foreign_issuer_report is not None:
            request.get_div_foreign_issuer_report = get_div_foreign_issuer_report
        response, call = self.stub.GetDividendsForeignIssuer.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.GetDividendsForeignIssuerRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetDividendsForeignIssuer")
        return _grpc_helpers.protobuf_to_dataclass(
            response, GetDividendsForeignIssuerResponse
        )

    @handle_request_error("GetOperationsByCursor")
    def get_operations_by_cursor(
        self,
        request: GetOperationsByCursorRequest,
    ) -> GetOperationsByCursorResponse:
        response, call = self.stub.GetOperationsByCursor.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.GetOperationsByCursorRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetOperationsByCursor")
        return _grpc_helpers.protobuf_to_dataclass(
            response, GetOperationsByCursorResponse
        )


class OperationsStreamService(_grpc_helpers.Service):
    _stub_factory = operations_pb2_grpc.OperationsStreamServiceStub

    @handle_request_error_gen("PortfolioStream")
    def portfolio_stream(
        self,
        *,
        accounts: Optional[List[str]] = None,
        ping_delay_ms: Optional[int] = None,
    ) -> Iterable[PortfolioStreamResponse]:
        request = PortfolioStreamRequest()
        ping_settings = PingDelaySettings()
        if ping_delay_ms is not None:
            ping_settings.ping_delay_ms = ping_delay_ms
        request.ping_settings = ping_settings
        if accounts:
            request.accounts = accounts
        else:
            raise ValueError("accounts can not be empty")
        for response in self.stub.PortfolioStream(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.PortfolioStreamRequest()
            ),
            metadata=self.metadata,
        ):
            yield _grpc_helpers.protobuf_to_dataclass(response, PortfolioStreamResponse)

    @handle_request_error_gen("PositionsStream")
    def positions_stream(
        self,
        *,
        accounts: Optional[List[str]] = None,
        ping_delay_ms: Optional[int] = None,
        with_initial_positions: Optional[bool] = None,
    ) -> Iterable[PositionsStreamResponse]:
        request = PositionsStreamRequest()
        if accounts:
            request.accounts = accounts
        else:
            raise ValueError("accounts can not be empty")
        ping_settings = PingDelaySettings()
        if ping_delay_ms is not None:
            ping_settings.ping_delay_ms = ping_delay_ms
        request.ping_settings = ping_settings
        if with_initial_positions:
            request.with_initial_positions = with_initial_positions
        for response in self.stub.PositionsStream(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.PositionsStreamRequest()
            ),
            metadata=self.metadata,
        ):
            yield _grpc_helpers.protobuf_to_dataclass(response, PositionsStreamResponse)


class OrdersStreamService(_grpc_helpers.Service):
    _stub_factory = orders_pb2_grpc.OrdersStreamServiceStub

    @handle_request_error_gen("TradesStream")
    def trades_stream(
        self,
        *,
        accounts: Optional[List[str]] = None,
        ping_delay_ms: Optional[int] = None,
    ) -> Iterable[TradesStreamResponse]:
        request = TradesStreamRequest()
        if ping_delay_ms is not None:
            request.ping_delay_ms = ping_delay_ms
        if accounts:
            request.accounts = accounts
        else:
            raise ValueError("accounts can not be empty")
        for response in self.stub.TradesStream(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.TradesStreamRequest()
            ),
            metadata=self.metadata,
        ):
            yield _grpc_helpers.protobuf_to_dataclass(response, TradesStreamResponse)

    @handle_request_error_gen("OrderStateStream")
    def order_state_stream(
        self, *, request: OrderStateStreamRequest
    ) -> Iterable[OrderStateStreamResponse]:
        for response in self.stub.OrderStateStream(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.OrderStateStreamRequest()
            ),
            metadata=self.metadata,
        ):
            yield _grpc_helpers.protobuf_to_dataclass(
                response, OrderStateStreamResponse
            )


class OrdersService(_grpc_helpers.Service):
    _stub_factory = orders_pb2_grpc.OrdersServiceStub

    @handle_request_error("PostOrder")
    def post_order(
        self,
        *,
        figi: str = "",
        quantity: int = 0,
        price: Optional[Quotation] = None,
        direction: OrderDirection = OrderDirection(0),
        account_id: str = "",
        order_type: OrderType = OrderType(0),
        order_id: str = "",
        instrument_id: str = "",
        time_in_force: TimeInForceType = TimeInForceType(0),
        price_type: PriceType = PriceType(0),
        confirm_margin_trade: bool = False,
    ) -> PostOrderResponse:
        request = PostOrderRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        request.quantity = quantity
        if price is not None:
            request.price = price
        request.direction = direction
        request.account_id = account_id
        request.order_type = order_type
        if not utils.empty_or_uuid(order_id):
            raise RequestError(
                grpc.StatusCode.INVALID_ARGUMENT,
                "order_id should be empty or uuid",
                None,
            )
        request.order_id = order_id
        request.time_in_force = time_in_force
        request.price_type = price_type
        if confirm_margin_trade:
            request.confirm_margin_trade = confirm_margin_trade
        response, call = self.stub.PostOrder.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.PostOrderRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "PostOrder")
        return _grpc_helpers.protobuf_to_dataclass(response, PostOrderResponse)

    @handle_request_error("PostOrderAsync")
    def post_order_async(
        self, request: PostOrderAsyncRequest
    ) -> PostOrderAsyncResponse:
        if not utils.empty_or_uuid(request.order_id):
            raise RequestError(
                grpc.StatusCode.INVALID_ARGUMENT,
                "order_id should be empty or uuid",
                None,
            )
        response, call = self.stub.PostOrderAsync.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.PostOrderAsyncRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "PostOrderAsync")
        return _grpc_helpers.protobuf_to_dataclass(response, PostOrderAsyncResponse)

    @handle_request_error("CancelOrder")
    def cancel_order(
        self,
        *,
        account_id: str = "",
        order_id: str = "",
        order_id_type: Optional["OrderIdType"] = None,
    ) -> CancelOrderResponse:
        request = CancelOrderRequest()
        request.account_id = account_id
        request.order_id = order_id
        request.order_id_type = order_id_type
        response, call = self.stub.CancelOrder.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.CancelOrderRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "CancelOrder")
        return _grpc_helpers.protobuf_to_dataclass(response, CancelOrderResponse)

    @handle_request_error("GetOrderState")
    def get_order_state(
        self,
        *,
        account_id: str = "",
        order_id: str = "",
        price_type: PriceType = PriceType(0),
        order_id_type: Optional["OrderIdType"] = None,
    ) -> OrderState:
        request = GetOrderStateRequest()
        request.account_id = account_id
        request.order_id = order_id
        request.price_type = price_type
        request.order_id_type = order_id_type
        response, call = self.stub.GetOrderState.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.GetOrderStateRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetOrderState")
        return _grpc_helpers.protobuf_to_dataclass(response, OrderState)

    @handle_request_error("GetOrders")
    def get_orders(self, *, account_id: str = "") -> GetOrdersResponse:
        request = GetOrdersRequest()
        request.account_id = account_id
        response, call = self.stub.GetOrders.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.GetOrdersRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetOrders")
        return _grpc_helpers.protobuf_to_dataclass(response, GetOrdersResponse)

    @handle_request_error("ReplaceOrder")
    def replace_order(self, request: ReplaceOrderRequest) -> PostOrderResponse:
        response, call = self.stub.ReplaceOrder.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.ReplaceOrderRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "ReplaceOrder")
        return _grpc_helpers.protobuf_to_dataclass(response, PostOrderResponse)

    @handle_request_error("GetMaxLots")
    def get_max_lots(self, request: GetMaxLotsRequest) -> GetMaxLotsResponse:
        response, call = self.stub.GetMaxLots.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.GetMaxLotsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetMaxLots")
        return _grpc_helpers.protobuf_to_dataclass(response, GetMaxLotsResponse)

    @handle_request_error("GetOrderPrice")
    def get_order_price(self, request: GetOrderPriceRequest) -> GetOrderPriceResponse:
        response, call = self.stub.GetOrderPrice.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.GetOrderPriceRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetOrderPrice")
        return _grpc_helpers.protobuf_to_dataclass(response, GetOrderPriceResponse)


class UsersService(_grpc_helpers.Service):
    _stub_factory = users_pb2_grpc.UsersServiceStub

    @handle_request_error("GetAccounts")
    def get_accounts(self) -> GetAccountsResponse:
        request = GetAccountsRequest()
        response, call = self.stub.GetAccounts.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, users_pb2.GetAccountsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetAccounts")
        return _grpc_helpers.protobuf_to_dataclass(response, GetAccountsResponse)

    @handle_request_error("GetMarginAttributes")
    def get_margin_attributes(
        self, *, account_id: str = ""
    ) -> GetMarginAttributesResponse:
        request = GetMarginAttributesRequest()
        request.account_id = account_id
        response, call = self.stub.GetMarginAttributes.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, users_pb2.GetMarginAttributesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetMarginAttributes")
        return _grpc_helpers.protobuf_to_dataclass(
            response, GetMarginAttributesResponse
        )

    @handle_request_error("GetUserTariff")
    def get_user_tariff(self) -> GetUserTariffResponse:
        request = GetUserTariffRequest()
        response, call = self.stub.GetUserTariff.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, users_pb2.GetUserTariffRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetUserTariff")
        return _grpc_helpers.protobuf_to_dataclass(response, GetUserTariffResponse)

    @handle_request_error("GetInfo")
    def get_info(self) -> GetInfoResponse:
        request = GetInfoRequest()
        response, call = self.stub.GetInfo.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, users_pb2.GetInfoRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetInfo")
        return _grpc_helpers.protobuf_to_dataclass(response, GetInfoResponse)


class SandboxService(_grpc_helpers.Service):
    _stub_factory = sandbox_pb2_grpc.SandboxServiceStub

    @handle_request_error("OpenSandboxAccount")
    def open_sandbox_account(
        self, name: Optional[str] = ""
    ) -> OpenSandboxAccountResponse:
        request = OpenSandboxAccountRequest()
        request.name = name
        response, call = self.stub.OpenSandboxAccount.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, sandbox_pb2.OpenSandboxAccountRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "OpenSandboxAccount")
        return _grpc_helpers.protobuf_to_dataclass(response, OpenSandboxAccountResponse)

    @deprecated(details="Use `SandboxClient.users.get_accounts(...)` method instead")
    @handle_request_error("GetSandboxAccounts")
    def get_sandbox_accounts(self) -> GetAccountsResponse:
        request = GetAccountsRequest()
        response, call = self.stub.GetSandboxAccounts.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, users_pb2.GetAccountsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSandboxAccounts")
        return _grpc_helpers.protobuf_to_dataclass(response, GetAccountsResponse)

    @handle_request_error("CloseSandboxAccount")
    def close_sandbox_account(
        self, *, account_id: str = ""
    ) -> CloseSandboxAccountResponse:
        request = CloseSandboxAccountRequest()
        request.account_id = account_id
        response, call = self.stub.CloseSandboxAccount.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, sandbox_pb2.CloseSandboxAccountRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "CloseSandboxAccount")
        return _grpc_helpers.protobuf_to_dataclass(
            response, CloseSandboxAccountResponse
        )

    @deprecated(details="Use `SandboxClient.orders.post_order(...)` method instead")
    @handle_request_error("PostSandboxOrder")
    def post_sandbox_order(
        self,
        *,
        figi: str = "",
        quantity: int = 0,
        price: Optional[Quotation] = None,
        direction: OrderDirection = OrderDirection(0),
        account_id: str = "",
        order_type: OrderType = OrderType(0),
        order_id: str = "",
        instrument_id: str = "",
        time_in_force: TimeInForceType = TimeInForceType(0),
        price_type: PriceType = PriceType(0),
    ) -> PostOrderResponse:
        request = PostOrderRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        request.quantity = quantity
        if price is not None:
            request.price = price
        request.direction = direction
        request.account_id = account_id
        request.order_type = order_type
        if not utils.empty_or_uuid(order_id):
            raise RequestError(
                grpc.StatusCode.INVALID_ARGUMENT,
                "order_id should be empty or uuid",
                None,
            )
        request.order_id = order_id
        request.time_in_force = time_in_force
        request.price_type = price_type
        response, call = self.stub.PostSandboxOrder.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.PostOrderRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "PostSandboxOrder")
        return _grpc_helpers.protobuf_to_dataclass(response, PostOrderResponse)

    @deprecated(details="Use `SandboxClient.orders.replace_order(...)` method instead")
    @handle_request_error("ReplaceSandboxOrder")
    def replace_sandbox_order(
        self,
        request: "ReplaceOrderRequest",
    ) -> PostOrderResponse:
        response, call = self.stub.ReplaceSandboxOrder.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.ReplaceOrderRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "ReplaceSandboxOrder")
        return _grpc_helpers.protobuf_to_dataclass(response, PostOrderResponse)

    @deprecated(details="Use `SandboxClient.orders.get_orders(...)` method instead")
    @handle_request_error("GetSandboxOrders")
    def get_sandbox_orders(self, *, account_id: str = "") -> GetOrdersResponse:
        request = GetOrdersRequest()
        request.account_id = account_id
        response, call = self.stub.GetSandboxOrders.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.GetOrdersRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSandboxOrders")
        return _grpc_helpers.protobuf_to_dataclass(response, GetOrdersResponse)

    @deprecated(details="Use `SandboxClient.orders.cancel_order(...)` method instead")
    @handle_request_error("CancelSandboxOrder")
    def cancel_sandbox_order(
        self,
        *,
        account_id: str = "",
        order_id: str = "",
        order_id_type: Optional["OrderIdType"] = None,
    ) -> CancelOrderResponse:
        request = CancelOrderRequest()
        request.account_id = account_id
        request.order_id = order_id
        request.order_id_type = order_id_type
        response, call = self.stub.CancelSandboxOrder.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.CancelOrderRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "CancelSandboxOrder")
        return _grpc_helpers.protobuf_to_dataclass(response, CancelOrderResponse)

    @deprecated(
        details="Use `SandboxClient.orders.get_order_state(...)` method instead"
    )
    @handle_request_error("GetSandboxOrderState")
    def get_sandbox_order_state(
        self,
        *,
        account_id: str = "",
        order_id: str = "",
        price_type: PriceType = PriceType(0),
        order_id_type: Optional["OrderIdType"] = None,
    ) -> OrderState:
        request = GetOrderStateRequest()
        request.account_id = account_id
        request.order_id = order_id
        request.price_type = price_type
        request.order_id_type = order_id_type
        response, call = self.stub.GetSandboxOrderState.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.GetOrderStateRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSandboxOrderState")
        return _grpc_helpers.protobuf_to_dataclass(response, OrderState)

    @deprecated(
        details="Use `SandboxClient.operations.get_positions(...)` method instead"
    )
    @handle_request_error("GetSandboxPositions")
    def get_sandbox_positions(self, *, account_id: str = "") -> PositionsResponse:
        request = PositionsRequest()
        request.account_id = account_id
        response, call = self.stub.GetSandboxPositions.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.PositionsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSandboxPositions")
        return _grpc_helpers.protobuf_to_dataclass(response, PositionsResponse)

    @deprecated(
        details="Use `SandboxClient.operations.get_operations(...)` method instead"
    )
    @handle_request_error("GetSandboxOperations")
    def get_sandbox_operations(
        self,
        *,
        account_id: str = "",
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
        state: OperationState = OperationState(0),
        figi: str = "",
    ) -> OperationsResponse:
        request = OperationsRequest()
        request.account_id = account_id
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        request.state = state
        request.figi = figi
        response, call = self.stub.GetSandboxOperations.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.OperationsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSandboxOperations")
        return _grpc_helpers.protobuf_to_dataclass(response, OperationsResponse)

    @deprecated(
        details="Use `SandboxClient.operations.get_operations_by_cursor` method instead"
    )
    @handle_request_error("GetOperationsByCursor")
    def get_operations_by_cursor(
        self,
        request: GetOperationsByCursorRequest,
    ) -> GetOperationsByCursorResponse:
        response, call = self.stub.GetSandboxOperationsByCursor.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.GetOperationsByCursorRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetOperationsByCursor")
        return _grpc_helpers.protobuf_to_dataclass(
            response, GetOperationsByCursorResponse
        )

    @deprecated(
        details="Use `SandboxClient.operations.get_portfolio(...)` method instead"
    )
    @handle_request_error("GetSandboxPortfolio")
    def get_sandbox_portfolio(self, *, account_id: str = "") -> PortfolioResponse:
        request = PortfolioRequest()
        request.account_id = account_id
        response, call = self.stub.GetSandboxPortfolio.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.PortfolioRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSandboxPortfolio")
        return _grpc_helpers.protobuf_to_dataclass(response, PortfolioResponse)

    @handle_request_error("SandboxPayIn")
    def sandbox_pay_in(
        self, *, account_id: str = "", amount: Optional[MoneyValue] = None
    ) -> SandboxPayInResponse:
        request = SandboxPayInRequest()
        request.account_id = account_id
        if amount is not None:
            request.amount = amount
        response, call = self.stub.SandboxPayIn.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, sandbox_pb2.SandboxPayInRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "SandboxPayIn")
        return _grpc_helpers.protobuf_to_dataclass(response, SandboxPayInResponse)

    @deprecated(
        details="Use `SandboxClient.operations.get_withdraw_limits(...)` method instead"
    )
    @handle_request_error("GetSandboxWithdrawLimits")
    def get_sandbox_withdraw_limits(
        self,
        *,
        account_id: str = "",
    ) -> WithdrawLimitsResponse:
        request = WithdrawLimitsRequest()
        request.account_id = account_id
        response, call = self.stub.GetSandboxWithdrawLimits.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, operations_pb2.WithdrawLimitsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSandboxWithdrawLimits")
        return _grpc_helpers.protobuf_to_dataclass(response, WithdrawLimitsResponse)

    @handle_request_error("GetSandboxMaxLots")
    def get_sandbox_max_lots(
        self,
        *,
        request: GetMaxLotsRequest,
    ) -> GetMaxLotsResponse:
        response, call = self.stub.GetSandboxMaxLots.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.GetMaxLotsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSandboxMaxLots")
        return _grpc_helpers.protobuf_to_dataclass(response, GetMaxLotsResponse)

    @handle_request_error("PostSandboxOrderAsync")
    def post_sandbox_order_async(
        self,
        *,
        request: PostOrderAsyncRequest,
    ) -> PostOrderAsyncResponse:
        response, call = self.stub.PostSandboxOrderAsync.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, orders_pb2.PostOrderAsyncRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "PostSandboxOrderAsync")
        return _grpc_helpers.protobuf_to_dataclass(response, PostOrderAsyncResponse)


class StopOrdersService(_grpc_helpers.Service):
    _stub_factory = stoporders_pb2_grpc.StopOrdersServiceStub

    @handle_request_error("PostStopOrder")
    def post_stop_order(
        self,
        *,
        figi: str = "",
        quantity: int = 0,
        price: Optional[Quotation] = None,
        stop_price: Optional[Quotation] = None,
        direction: StopOrderDirection = StopOrderDirection(0),
        account_id: str = "",
        expiration_type: StopOrderExpirationType = StopOrderExpirationType(0),
        stop_order_type: StopOrderType = StopOrderType(0),
        expire_date: Optional[datetime] = None,
        instrument_id: str = "",
        exchange_order_type: ExchangeOrderType = ExchangeOrderType(0),
        take_profit_type: TakeProfitType = TakeProfitType(0),
        trailing_data: Optional[PostStopOrderRequestTrailingData] = None,
        price_type: PriceType = PriceType(0),
        order_id: str = "",
        confirm_margin_trade: bool = False,
    ) -> PostStopOrderResponse:
        request = PostStopOrderRequest()
        request.figi = figi
        request.instrument_id = instrument_id
        request.quantity = quantity
        if price is not None:
            request.price = price
        if stop_price is not None:
            request.stop_price = stop_price
        request.direction = direction
        request.account_id = account_id
        request.expiration_type = expiration_type
        request.stop_order_type = stop_order_type
        if expire_date is not None:
            request.expire_date = expire_date
        request.exchange_order_type = exchange_order_type
        request.take_profit_type = take_profit_type
        if trailing_data is not None:
            request.trailing_data = trailing_data
        request.price_type = price_type
        request.order_id = order_id
        if confirm_margin_trade:
            request.confirm_margin_trade = confirm_margin_trade
        response, call = self.stub.PostStopOrder.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, stoporders_pb2.PostStopOrderRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "PostStopOrder")
        return _grpc_helpers.protobuf_to_dataclass(response, PostStopOrderResponse)

    @handle_request_error("GetStopOrders")
    def get_stop_orders(
        self,
        *,
        account_id: str = "",
        status: StopOrderStatusOption = StopOrderStatusOption(0),
        from_: Optional[datetime] = None,
        to: Optional[datetime] = None,
    ) -> GetStopOrdersResponse:
        request = GetStopOrdersRequest()
        request.account_id = account_id
        request.status = status
        if from_ is not None:
            request.from_ = from_
        if to is not None:
            request.to = to
        response, call = self.stub.GetStopOrders.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, stoporders_pb2.GetStopOrdersRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetStopOrders")
        return _grpc_helpers.protobuf_to_dataclass(response, GetStopOrdersResponse)

    @handle_request_error("CancelStopOrder")
    def cancel_stop_order(
        self, *, account_id: str = "", stop_order_id: str = ""
    ) -> CancelStopOrderResponse:
        request = CancelStopOrderRequest()
        request.account_id = account_id
        request.stop_order_id = stop_order_id
        response, call = self.stub.CancelStopOrder.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, stoporders_pb2.CancelStopOrderRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "CancelStopOrder")
        return _grpc_helpers.protobuf_to_dataclass(response, CancelStopOrderResponse)


class SignalService(_grpc_helpers.Service):
    _stub_factory = signals_pb2_grpc.SignalServiceStub

    @handle_request_error("GetStrategies")
    def get_strategies(
        self,
        *,
        request: GetStrategiesRequest,
    ) -> GetStrategiesResponse:
        response, call = self.stub.GetStrategies.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, signals_pb2.GetStrategiesRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetStrategies")
        return _grpc_helpers.protobuf_to_dataclass(response, GetStrategiesResponse)

    @handle_request_error("GetSignals")
    def get_signals(
        self,
        *,
        request: GetSignalsRequest,
    ) -> GetSignalsResponse:
        response, call = self.stub.GetSignals.with_call(
            request=_grpc_helpers.dataclass_to_protobuff(
                request, signals_pb2.GetSignalsRequest()
            ),
            metadata=self.metadata,
        )
        log_request(get_tracking_id_from_call(call), "GetSignals")
        return _grpc_helpers.protobuf_to_dataclass(response, GetSignalsResponse)
