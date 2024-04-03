import re
import sys


def set_version(new_value: str, constant_name: str, file_path: str) -> None:
    with open(file_path, "r") as file:
        file_data = file.read()

    constant_pattern = re.compile(rf'{constant_name}\s*=\s*["\'].*?["\']', re.MULTILINE)
    file_data = constant_pattern.sub(f'{constant_name} = "{new_value}"', file_data)

    with open(file_path, "w") as file:
        file.write(file_data)


def main() -> None:
    version = sys.argv[1]
    set_version(version, "__version__", "tinkoff/invest/__init__.py")
    set_version(version, "APP_VERSION", "tinkoff/invest/constants.py")


if __name__ == "__main__":
    main()
