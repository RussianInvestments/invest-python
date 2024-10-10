import logging
from pathlib import Path

from iprotopy import PackageGenerator

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    generator = PackageGenerator()
    base_dir = Path().absolute().parent

    generator.generate_sources(
        proto_dir=base_dir / "protos",
        out_dir=base_dir,
    )
