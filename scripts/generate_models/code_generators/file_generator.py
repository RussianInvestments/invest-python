import logging
from ast import ClassDef, Module
from pathlib import Path
from types import NoneType

from iprotopy.domestic_importer import DomesticImporter
from iprotopy.enum_generator import EnumGenerator
from iprotopy.importer import Importer
from iprotopy.type_mapper import TypeMapper
from proto_schema_parser import Message, Option, Parser
from proto_schema_parser.ast import (
    Comment,
    Enum,
    Extension,
    File,
    Import as ProtoImport,
    Package,
    Service,
)

from scripts.generate_models.code_generators.message_class_field_generator import (
    MessageClassGenerator,
)
from scripts.generate_models.code_generators.service_generators import ServiceGenerator

logger = logging.getLogger(__name__)


class SourceGenerator:
    def __init__(
        self,
        proto_file: Path,
        out_dir: Path,
        pyfile: Path,
        parser: Parser,
        type_mapper: TypeMapper,
        global_importer: Importer,
    ):
        self._parser = parser
        self._type_mapper = type_mapper
        self._importer = DomesticImporter(global_importer, pyfile)
        self._proto_file = proto_file
        self._out_dir = out_dir
        self._pyfile = pyfile

    def generate_source(self) -> Module:
        logger.debug(f"Generating source for {self._proto_file}")
        with open(self._proto_file) as f:
            text = f.read()

        file: File = self._parser.parse(text)

        enums: list[ClassDef] = []
        messages: list[ClassDef] = []
        services: list[ClassDef] = []

        for element in file.file_elements:
            if isinstance(element, Enum):
                proto_enum_processor = EnumGenerator(self._importer)
                enums.append(proto_enum_processor.process_enum(element))
            elif isinstance(element, Message):
                proto_message_processor = MessageClassGenerator(
                    self._importer, self._type_mapper
                )
                messages.append(proto_message_processor.process_proto_message(element))
            elif isinstance(element, Service):
                service_generator = ServiceGenerator(self._importer, self._pyfile)
                services.append(service_generator.process_sync_service(element))
                services.append(service_generator.process_aio_service(element))
            elif isinstance(
                element, (Extension, Comment, ProtoImport, Option, Package, NoneType)
            ):
                continue
            else:
                raise NotImplementedError(f"Unknown element {element}")
        return Module(body=[*enums, *messages, *services], type_ignores=[])
