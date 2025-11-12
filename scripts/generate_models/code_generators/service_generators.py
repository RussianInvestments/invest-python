from ast import ClassDef

from iprotopy.service_generator import ServiceGenerator as DefaultServiceGenerator
from iprotopy.service_method_generator import (
    ServiceMethodGenerator as DefaultServiceMethodGenerator,
)
from proto_schema_parser.ast import Comment, Method, Service

from scripts.generate_models.code_generators.generators_of_async_methods import (
    AIOServiceMethodGenerator,
)
from scripts.generate_models.code_generators.generators_of_sync_methods import (
    SyncServiceMethodGenerator,
)


class ServiceGenerator(DefaultServiceGenerator):
    def _process_service(
        self, service: Service, generator_cls: type[DefaultServiceMethodGenerator]
    ) -> ClassDef:
        body = []

        self._try_add_docstring(body, service)

        body.extend(self._get_protobuf_attributes(service))

        for element in service.elements:
            if isinstance(element, Comment):
                continue
            elif isinstance(element, Method):
                service_method_generator = generator_cls(self._importer)
                body.append(service_method_generator.process_service_method(element))
                continue
            else:
                raise NotImplementedError(f"Unknown element {element}")

        bases = self._get_bases()
        return ClassDef(
            name=service.name,
            bases=bases,
            keywords=[],
            body=body,
            decorator_list=[],
        )

    def process_sync_service(self, service: Service) -> ClassDef:
        return self._process_service(service, SyncServiceMethodGenerator)

    def process_aio_service(self, service: Service):
        class_def = self._process_service(service, AIOServiceMethodGenerator)
        class_def.name = f"Async{class_def.name}"
        return class_def
