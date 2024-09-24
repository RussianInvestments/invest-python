import logging
import os

import pytest

from tinkoff.invest import (
    EditFavoritesActionType,
    EditFavoritesRequest as DataclassModel,
)
from tinkoff.invest._grpc_helpers import protobuf_to_dataclass
from tinkoff.invest.grpc.instruments_pb2 import EditFavoritesRequest as ProtoModel

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture()
def unsupported_model() -> ProtoModel:
    pb_obj = ProtoModel()
    pb_obj.action_type = 137
    return pb_obj


class TestProtobufToDataclass:
    def test_protobuf_to_dataclass_does_not_raise_by_default(
        self, unsupported_model: ProtoModel, caplog
    ):
        expected = EditFavoritesActionType.EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED

        actual = protobuf_to_dataclass(
            pb_obj=unsupported_model, dataclass_type=DataclassModel
        ).action_type

        assert expected == actual

    @pytest.mark.parametrize("use_default_enum_if_error", ["True", "true", "1"])
    def test_protobuf_to_dataclass_does_not_raise_when_set_true(
        self, unsupported_model: ProtoModel, use_default_enum_if_error: str
    ):
        expected = EditFavoritesActionType.EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED

        os.environ["USE_DEFAULT_ENUM_IF_ERROR"] = use_default_enum_if_error
        actual = protobuf_to_dataclass(
            pb_obj=unsupported_model, dataclass_type=DataclassModel
        ).action_type

        assert expected == actual

    @pytest.mark.parametrize("use_default_enum_if_error", ["False", "false", "0"])
    def test_protobuf_to_dataclass_does_raise_when_set_false(
        self, unsupported_model: ProtoModel, use_default_enum_if_error: str
    ):
        os.environ["USE_DEFAULT_ENUM_IF_ERROR"] = use_default_enum_if_error
        with pytest.raises(ValueError):
            _ = protobuf_to_dataclass(
                pb_obj=unsupported_model, dataclass_type=DataclassModel
            ).action_type
