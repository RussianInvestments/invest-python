import logging
from pathlib import Path
from typing import Dict, Set

from iprotopy.importer import Importer as BaseImporter

logger = logging.getLogger(__name__)


class Importer(BaseImporter):
    def __init__(self):
        super().__init__()
        self._defined_in_package: Dict[Path, Set[str]] = {}

    def define_dependency(self, name: str, package: Path):
        if name in self._definitions:
            logger.warning("Class %s already registered", name)
        self._definitions[name] = package
        defined = self._defined_in_package.get(package)
        if defined is None:
            defined = set()
            self._defined_in_package[package] = defined
        defined.add(name)

    def import_dependency(self, name: str, package: Path):
        if name in self._default_dependencies or name in self._defined_in_package.get(
            package, set()
        ):
            return

        dependencies = self._dependencies.get(package, set())
        dependencies.add(name)
        self._dependencies[package] = dependencies

    def remove_circular_dependencies(self):
        for package, deps in self._dependencies.items():
            local = self._defined_in_package.get(package, set())
            deps.difference_update(local)
