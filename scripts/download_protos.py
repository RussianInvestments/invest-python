import os
import shutil
import sys
from http import HTTPStatus
from pathlib import Path
from zipfile import ZipFile

import requests

BRANCH = "main"

URL = f"https://github.com/RussianInvestments/investAPI/archive/refs/heads/{BRANCH}.zip"
OUTPUT_PATH = "protos/tinkoff/invest/grpc"
PROTOS_TMP_ZIP = "protos.zip"
ZIP_PROTOS_ROOT_PATH_BRANCH = BRANCH.replace("/", "-")
ZIP_PROTOS_ROOT_PATH = f"investAPI-{ZIP_PROTOS_ROOT_PATH_BRANCH}"
ZIP_PROTOS_PATH = f"{ZIP_PROTOS_ROOT_PATH}/src/docs/contracts"
FILES = [
    "google/api/field_behavior.proto",
    "common.proto",
    "instruments.proto",
    "marketdata.proto",
    "operations.proto",
    "orders.proto",
    "sandbox.proto",
    "signals.proto",
    "stoporders.proto",
    "users.proto",
]

LINES_TO_REPLACE = [
    (f'import "{file_name}";', f'import "tinkoff/invest/grpc/{file_name}";')
    for file_name in FILES
]


def main() -> int:
    _clear_in_start()
    _download_protos()
    _extract_protos()
    _move_protos()
    _clear_in_end()
    _modify_protos()
    return 0


def _clear_in_start():
    shutil.rmtree(OUTPUT_PATH, ignore_errors=True)


def _download_protos():
    session = requests.session()
    response = session.get(URL, stream=True)
    if response.status_code != HTTPStatus.OK:
        return

    with open(PROTOS_TMP_ZIP, "wb") as f:
        for chunk in response:
            f.write(chunk)


def _extract_protos():
    with ZipFile(PROTOS_TMP_ZIP) as zf:
        for name in FILES:
            zf.extract(f"{ZIP_PROTOS_PATH}/{name}", path=".")


def _move_protos():
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    for name in FILES:
        folders = "/".join(name.split("/")[:-1])
        Path(f"{OUTPUT_PATH}/{folders}").mkdir(parents=True, exist_ok=True)
        shutil.move(f"{ZIP_PROTOS_PATH}/{name}", f"{OUTPUT_PATH}/{folders}")


def _clear_in_end():
    os.remove(PROTOS_TMP_ZIP)
    shutil.rmtree(ZIP_PROTOS_ROOT_PATH)


def _modify_protos():
    for name in FILES:
        with open(f"{OUTPUT_PATH}/{name}", "r", encoding="utf-8") as f:
            protofile_text = f.read()

        for str_to_replace, replaced_str in LINES_TO_REPLACE:
            protofile_text = protofile_text.replace(str_to_replace, replaced_str)

        with open(f"{OUTPUT_PATH}/{name}", "w+", encoding="utf-8") as f:
            f.write(protofile_text)


if __name__ == "__main__":
    sys.exit(main())
