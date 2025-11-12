from ast import (
    AsyncFunctionDef,
    Call,
    Constant,
    FunctionDef,
    Load,
    Name,
    Subscript,
    alias,
    arg,
    arguments,
    expr,
)

from iprotopy.imports import ImportFrom
from iprotopy.service_method_generator import (
    BaseServiceMethodGenerator as DefaultBaseServiceMethodGenerator,
)


class BaseServiceMethodGenerator(DefaultBaseServiceMethodGenerator):
    tracking_id_getter: str | None = None
    error_handler: str = ...
    is_async: bool = False

    def _get_annotation(self, class_type: str, is_stream: bool) -> expr:
        self._importer.import_dependency(class_type)
        if is_stream:
            if self.is_async:
                iterator_cls_name = "AsyncIterable"
            else:
                iterator_cls_name = "Iterable"
            self._importer.add_import(
                ImportFrom(
                    module="typing", names=[alias(name=iterator_cls_name)], level=0
                )
            )
            return Subscript(
                value=Name(id=iterator_cls_name, ctx=Load()),
                slice=Constant(value=class_type),
                ctx=Load(),
            )
        return Constant(value=class_type)

    def _get_args(self, input_class: str) -> arguments:
        input_annotation = self._get_annotation(input_class, self._is_input_stream)
        if not self._is_input_stream:
            default_request = Call(
                func=Name(id=input_class, ctx=Load()),
                args=[],
                keywords=[],
            )
        else:
            default_request = None
        return arguments(
            posonlyargs=[],
            args=[
                arg(arg="self"),
                arg(
                    arg=self._input_arg_name,
                    annotation=input_annotation,
                ),
            ],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[default_request] if default_request else [],
        )

    def create(self, method):
        input_class = method.input_type.type
        output_class = method.output_type.type

        args = self._get_args(input_class)

        output_annotation = self._get_annotation(output_class, self._is_output_stream)
        body = self._get_function_body(method)
        self._add_function_body_imports()

        decorator_list = [
            Call(
                func=Name(id=self.error_handler, ctx=Load()),
                args=[Constant(value=method.name)],
                keywords=[],
            )
        ]
        if self.is_async:
            return AsyncFunctionDef(
                name=method.name,
                args=args,
                body=body,
                decorator_list=decorator_list,
                returns=output_annotation,
            )
        return FunctionDef(
            name=method.name,
            args=args,
            body=body,
            decorator_list=decorator_list,
            returns=output_annotation,
        )

    def _add_function_body_imports(self):
        # self._importer.add_import(
        #     ImportFrom(
        #         module="tinkoff.invest._grpc_helpers",
        #         names=[alias(name="dataclass_to_protobuf")],
        #         level=0,
        #     )
        # )
        # self._importer.add_import(
        #     ImportFrom(
        #         module="tinkoff.invest._grpc_helpers",
        #         names=[alias(name="protobuf_to_dataclass")],
        #         level=0,
        #     )
        # )
        super()._add_function_body_imports()
        self._importer.add_import(
            ImportFrom(
                module="tinkoff.invest._errors",
                names=[
                    alias(name=self.error_handler),
                ],
                level=0,
            )
        )
        if self.tracking_id_getter:
            self._importer.add_import(
                ImportFrom(
                    module="tinkoff.invest.logging",
                    names=[
                        alias(name=self.tracking_id_getter),
                        alias(name="log_request"),
                    ],
                    level=0,
                )
            )


class BaseSyncServiceAnyUnaryFunctionGenerator(BaseServiceMethodGenerator):
    tracking_id_getter: str = "get_tracking_id_from_call"
    error_handler: str = "handle_request_error"


class BaseSyncServiceAnyStreamFunctionGenerator(BaseServiceMethodGenerator):
    error_handler: str = "handle_request_error_gen"


class BaseAIOServiceAnyUnaryFunctionGenerator(BaseServiceMethodGenerator):
    tracking_id_getter: str = "get_tracking_id_from_coro"
    error_handler: str = "handle_aio_request_error"
    is_async: bool = True


class BaseAIOServiceAnyStreamFunctionGenerator(BaseServiceMethodGenerator):
    error_handler: str = "handle_aio_request_error_gen"
    is_async: bool = True
