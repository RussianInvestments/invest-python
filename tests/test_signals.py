# pylint: disable=redefined-outer-name,unused-variable

from unittest import mock

import pytest

from tinkoff.invest.services import SignalService


@pytest.fixture()
def signals_service():
    return mock.create_autospec(spec=SignalService)


def test_get_signals(signals_service):
    response = signals_service.get_signals(request=mock.Mock())  # noqa: F841
    signals_service.get_signals.assert_called_once_with(request=mock.ANY)


def test_get_strategies(signals_service):
    response = signals_service.get_strategies(request=mock.Mock())  # noqa: F841
    signals_service.get_strategies.assert_called_once_with(request=mock.ANY)
