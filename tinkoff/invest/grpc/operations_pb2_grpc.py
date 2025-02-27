# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tinkoff.invest.grpc import (
    operations_pb2 as tinkoff_dot_invest_dot_grpc_dot_operations__pb2,
)


class OperationsServiceStub(object):
    """С помощью методов сервиса можно получить:<br/><br/> **1**. Список операций по счету.<br/> **2**.
    Портфель по счету.<br/> **3**. Позиции ценных бумаг на счете.<br/> **4**.
    Доступный остаток для вывода средств.<br/> **5**. Различные отчеты.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOperations = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetOperations',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsResponse.FromString,
                )
        self.GetPortfolio = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetPortfolio',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioResponse.FromString,
                )
        self.GetPositions = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetPositions',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsResponse.FromString,
                )
        self.GetWithdrawLimits = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetWithdrawLimits',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsResponse.FromString,
                )
        self.GetBrokerReport = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetBrokerReport',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportResponse.FromString,
                )
        self.GetDividendsForeignIssuer = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetDividendsForeignIssuer',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerResponse.FromString,
                )
        self.GetOperationsByCursor = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.OperationsService/GetOperationsByCursor',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetOperationsByCursorRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetOperationsByCursorResponse.FromString,
                )


class OperationsServiceServicer(object):
    """С помощью методов сервиса можно получить:<br/><br/> **1**. Список операций по счету.<br/> **2**.
    Портфель по счету.<br/> **3**. Позиции ценных бумаг на счете.<br/> **4**.
    Доступный остаток для вывода средств.<br/> **5**. Различные отчеты.
    """

    def GetOperations(self, request, context):
        """Получить список операций по счету.
        При работе с методом учитывайте [особенности взаимодействия](/invest/services/operations/operations_problems).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPortfolio(self, request, context):
        """Получить портфель по счету.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPositions(self, request, context):
        """Получить список позиций по счету.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWithdrawLimits(self, request, context):
        """Получить доступный остаток для вывода средств.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBrokerReport(self, request, context):
        """Получить брокерский отчет.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDividendsForeignIssuer(self, request, context):
        """Получить отчет «Справка о доходах за пределами РФ».
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOperationsByCursor(self, request, context):
        """Получить список операций по счету с пагинацией.
        При работе с методом учитывайте [особенности взаимодействия](/invest/services/operations/operations_problems).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperations,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsResponse.SerializeToString,
            ),
            'GetPortfolio': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPortfolio,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioResponse.SerializeToString,
            ),
            'GetPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPositions,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsResponse.SerializeToString,
            ),
            'GetWithdrawLimits': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWithdrawLimits,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsResponse.SerializeToString,
            ),
            'GetBrokerReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBrokerReport,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportResponse.SerializeToString,
            ),
            'GetDividendsForeignIssuer': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDividendsForeignIssuer,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerResponse.SerializeToString,
            ),
            'GetOperationsByCursor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperationsByCursor,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetOperationsByCursorRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetOperationsByCursorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.OperationsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OperationsService(object):
    """С помощью методов сервиса можно получить:<br/><br/> **1**. Список операций по счету.<br/> **2**.
    Портфель по счету.<br/> **3**. Позиции ценных бумаг на счете.<br/> **4**.
    Доступный остаток для вывода средств.<br/> **5**. Различные отчеты.
    """

    @staticmethod
    def GetOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetOperations',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.OperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPortfolio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetPortfolio',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetPositions',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWithdrawLimits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetWithdrawLimits',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.WithdrawLimitsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBrokerReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetBrokerReport',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.BrokerReportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDividendsForeignIssuer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetDividendsForeignIssuer',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetDividendsForeignIssuerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOperationsByCursor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsService/GetOperationsByCursor',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetOperationsByCursorRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.GetOperationsByCursorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class OperationsStreamServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PortfolioStream = channel.unary_stream(
                '/tinkoff.public.invest.api.contract.v1.OperationsStreamService/PortfolioStream',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamResponse.FromString,
                )
        self.PositionsStream = channel.unary_stream(
                '/tinkoff.public.invest.api.contract.v1.OperationsStreamService/PositionsStream',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsStreamRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsStreamResponse.FromString,
                )


class OperationsStreamServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PortfolioStream(self, request, context):
        """Server-side stream обновлений портфеля.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PositionsStream(self, request, context):
        """Server-side stream обновлений информации по изменению позиций портфеля.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationsStreamServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PortfolioStream': grpc.unary_stream_rpc_method_handler(
                    servicer.PortfolioStream,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamResponse.SerializeToString,
            ),
            'PositionsStream': grpc.unary_stream_rpc_method_handler(
                    servicer.PositionsStream,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsStreamRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.OperationsStreamService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OperationsStreamService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PortfolioStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsStreamService/PortfolioStream',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PortfolioStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PositionsStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tinkoff.public.invest.api.contract.v1.OperationsStreamService/PositionsStream',
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsStreamRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_operations__pb2.PositionsStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
