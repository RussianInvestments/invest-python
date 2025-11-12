import re
import typing
from ast import (
    Assign,
    AsyncFor,
    Attribute,
    Await,
    Call,
    Constant,
    Expr,
    FunctionDef,
    GeneratorExp,
    Load,
    Name,
    Return,
    Store,
    Yield,
    comprehension,
    keyword,
    stmt,
)

from iprotopy.service_method_generator import (
    ServiceMethodGenerator as DefaultServiceMethodGenerator,
)
from proto_schema_parser.ast import Method

from scripts.generate_models.code_generators.base_generators import (
    BaseAIOServiceAnyStreamFunctionGenerator,
    BaseAIOServiceAnyUnaryFunctionGenerator,
    BaseServiceMethodGenerator,
)


def _get_dataclass_from_protobuf_call(request_class_name: str) -> Call:
    return Call(
        func=Name(id="dataclass_to_protobuf", ctx=Load()),
        args=[
            Name(id="request", ctx=Load()),
            Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id="self", ctx=Load()),
                        attr="_protobuf",
                        ctx=Load(),
                    ),
                    attr=request_class_name,
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
        ],
        keywords=[],
    )


def _get_stub_initialization(
    request_variable_name: str, method_name: str, is_stream: bool
) -> Call:
    return Call(
        func=Attribute(
            value=Attribute(
                value=Name(id="self", ctx=Load()),
                attr="_stub",
                ctx=Load(),
            ),
            attr=method_name,
            ctx=Load(),
        ),
        args=[],
        keywords=[
            keyword(
                arg="request" if not is_stream else "request_iterator",
                value=Name(id=request_variable_name, ctx=Load()),
            ),
            keyword(
                arg="metadata",
                value=Attribute(
                    value=Name(id="self", ctx=Load()),
                    attr="_metadata",
                    ctx=Load(),
                ),
            ),
        ],
    )


def _get_protobuf_to_dataclass_call(response_class_name: str) -> Call:
    return Call(
        func=Name(id="protobuf_to_dataclass", ctx=Load()),
        args=[
            Name(id="response", ctx=Load()),
            Name(id=response_class_name, ctx=Load()),
        ],
        keywords=[],
    )


class ServiceMethodUnaryUnaryFunctionGenerator(
    BaseAIOServiceAnyUnaryFunctionGenerator,
):
    _input_arg_name: str = "request"
    _is_input_stream: bool = False
    _is_output_stream: bool = False

    def _get_function_body(self, method: Method) -> list[stmt]:
        method_name = method.name
        request_class_name = method.input_type.type
        response_class_name = method.output_type.type
        body = [
            Assign(
                targets=[Name(id="protobuf_request", ctx=Store())],
                value=_get_dataclass_from_protobuf_call(request_class_name),
            ),
            Assign(
                targets=[Name(id="response_coro", ctx=Store())],
                value=_get_stub_initialization(
                    "protobuf_request", method_name, is_stream=False
                ),
            ),
            Assign(
                targets=[Name(id="response", ctx=Store())],
                value=Await("response_coro"),
            ),
            Expr(
                value=Call(
                    func=Name(id="log_request", ctx=Load()),
                    args=[
                        Await(
                            Call(
                                func=Name(id="get_tracking_id_from_coro", ctx=Load()),
                                args=[Name(id="response_coro", ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Constant(value=method.name),
                    ],
                    keywords=[],
                )
            ),
            Return(value=_get_protobuf_to_dataclass_call(response_class_name)),
        ]
        return body


class ServiceMethodStreamUnaryFunctionGenerator(
    BaseAIOServiceAnyUnaryFunctionGenerator
):
    _input_arg_name: str = "request_iterator"
    _is_input_stream: bool = True
    _is_output_stream: bool = False

    def _get_function_body(self, method: Method) -> list[stmt]:
        raise NotImplementedError(
            f"Stream Unary for {method.name} is not implemented yet"
        )


class ServiceMethodUnaryStreamFunctionGenerator(
    BaseAIOServiceAnyStreamFunctionGenerator
):
    _input_arg_name: str = "request"
    _is_input_stream: bool = False
    _is_output_stream: bool = True

    def _get_function_body(self, method: Method) -> list[stmt]:
        method_name = method.name
        request_class_name = method.input_type.type
        response_class_name = method.output_type.type
        body = [
            Assign(
                targets=[Name(id="protobuf_request", ctx=Store())],
                value=_get_dataclass_from_protobuf_call(request_class_name),
            ),
            AsyncFor(
                target=Name(id="response", ctx=Store()),
                iter=_get_stub_initialization(
                    "protobuf_request", method_name, is_stream=False
                ),
                body=[
                    Yield(value=_get_protobuf_to_dataclass_call(response_class_name))
                ],
                orelse=[],
            ),
        ]
        return body


class ServiceMethodStreamStreamFunctionGenerator(
    BaseAIOServiceAnyStreamFunctionGenerator
):
    _input_arg_name: str = "request_iterator"
    _is_input_stream: bool = True
    _is_output_stream: bool = True

    def _get_function_body(self, method: Method) -> list[stmt]:
        method_name = method.name
        request_class_name = method.input_type.type
        response_class_name = method.output_type.type
        body = [
            Assign(
                targets=[Name(id="protobuf_request_iterator", ctx=Store())],
                value=GeneratorExp(
                    elt=_get_dataclass_from_protobuf_call(request_class_name),
                    generators=[
                        comprehension(
                            target=Name(id="request", ctx=Store()),
                            iter=Name(id="request_iterator", ctx=Load()),
                            ifs=[],
                            is_async=1,
                        )
                    ],
                ),
            ),
            AsyncFor(
                target=Name(id="response", ctx=Store()),
                iter=_get_stub_initialization(
                    "protobuf_request_iterator", method_name, is_stream=True
                ),
                body=[
                    Yield(value=_get_protobuf_to_dataclass_call(response_class_name))
                ],
                orelse=[],
            ),
        ]
        return body


class AIOServiceMethodGenerator(DefaultServiceMethodGenerator):
    _method_generators: typing.Dict[
        typing.Tuple[bool, bool], typing.Type[BaseServiceMethodGenerator]
    ] = {
        (False, False): ServiceMethodUnaryUnaryFunctionGenerator,
        (True, False): ServiceMethodStreamUnaryFunctionGenerator,
        (False, True): ServiceMethodUnaryStreamFunctionGenerator,
        (True, True): ServiceMethodStreamStreamFunctionGenerator,
    }

    def process_service_method(self, method: Method) -> FunctionDef:
        func_def = super().process_service_method(method)
        func_def.name = (
            re.sub(r"(?<!^)(?=[A-Z])", "_", method.name).replace("-", "_").lower()
        )  # to snake_case
        return func_def
