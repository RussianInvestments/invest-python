import logging
import sys
from pathlib import Path

from iprotopy import protos_generator

from scripts.generate_models.code_generators.package_generator import PackageGenerator

logging.basicConfig(level=logging.DEBUG)


def run_executable(original_run):
    def run(cmd, *a, **kw):
        if isinstance(cmd, (list, tuple)) and cmd and cmd[0] == "python":
            cmd = [sys.executable] + list(cmd[1:])
        return original_run(cmd, *a, **kw)

    return run


if __name__ == "__main__":
    protos_generator.subprocess.run = run_executable(protos_generator.subprocess.run)

    generator = PackageGenerator()
    base_dir = Path().absolute()

    generator.generate_sources(
        proto_dir=base_dir / "protos",
        out_dir=base_dir,
    )
