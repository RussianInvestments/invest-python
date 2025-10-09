# pylint: disable=redefined-outer-name,unused-variable
import os
from unittest import mock

import pytest

from tinkoff.invest import (
    Client,
    InstrumentIdType,
    InstrumentRequest,
    InstrumentsRequest,
    InstrumentStatus,
)
from tinkoff.invest.schemas import StructuredNote
from tinkoff.invest.services import InstrumentsService


@pytest.fixture()
def instruments_service():
    return mock.MagicMock(spec=InstrumentsService)


@pytest.fixture()
def instruments_client_service():
    with Client(token=os.environ["INVEST_SANDBOX_TOKEN"]) as client:
        yield client.instruments


def test_trading_schedules(instruments_service):
    responce = instruments_service.trading_schedules(  # noqa: F841
        exchange=mock.Mock(),
        from_=mock.Mock(),
        to=mock.Mock(),
    )
    instruments_service.trading_schedules.assert_called_once()


def test_bond_by(instruments_service):
    responce = instruments_service.bond_by(  # noqa: F841
        id_type=mock.Mock(),
        class_code=mock.Mock(),
        id=mock.Mock(),
    )
    instruments_service.bond_by.assert_called_once()


def test_bonds(instruments_service):
    responce = instruments_service.bonds(  # noqa: F841
        instrument_status=mock.Mock(),
    )
    instruments_service.bonds.assert_called_once()


def test_currency_by(instruments_service):
    responce = instruments_service.currency_by(  # noqa: F841
        id_type=mock.Mock(),
        class_code=mock.Mock(),
        id=mock.Mock(),
    )
    instruments_service.currency_by.assert_called_once()


def test_currencies(instruments_service):
    responce = instruments_service.currencies(  # noqa: F841
        instrument_status=mock.Mock(),
    )
    instruments_service.currencies.assert_called_once()


def test_etf_by(instruments_service):
    responce = instruments_service.etf_by(  # noqa: F841
        id_type=mock.Mock(),
        class_code=mock.Mock(),
        id=mock.Mock(),
    )
    instruments_service.etf_by.assert_called_once()


def test_etfs(instruments_service):
    responce = instruments_service.etfs(  # noqa: F841
        instrument_status=mock.Mock(),
    )
    instruments_service.etfs.assert_called_once()


def test_future_by(instruments_service):
    responce = instruments_service.future_by(  # noqa: F841
        id_type=mock.Mock(),
        class_code=mock.Mock(),
        id=mock.Mock(),
    )
    instruments_service.future_by.assert_called_once()


def test_futures(instruments_service):
    responce = instruments_service.futures(  # noqa: F841
        instrument_status=mock.Mock(),
    )
    instruments_service.futures.assert_called_once()


def test_share_by(instruments_service):
    responce = instruments_service.share_by(  # noqa: F841
        id_type=mock.Mock(),
        class_code=mock.Mock(),
        id=mock.Mock(),
    )
    instruments_service.share_by.assert_called_once()


def test_shares(instruments_service):
    responce = instruments_service.shares(  # noqa: F841
        instrument_status=mock.Mock(),
    )
    instruments_service.shares.assert_called_once()


def test_get_accrued_interests(instruments_service):
    responce = instruments_service.get_accrued_interests(  # noqa: F841
        figi=mock.Mock(),
        from_=mock.Mock(),
        to=mock.Mock(),
    )
    instruments_service.get_accrued_interests.assert_called_once()


def test_get_futures_margin(instruments_service):
    responce = instruments_service.get_futures_margin(  # noqa: F841
        figi=mock.Mock(),
    )
    instruments_service.get_futures_margin.assert_called_once()


def test_get_instrument_by(instruments_service):
    responce = instruments_service.get_instrument_by(  # noqa: F841
        id_type=mock.Mock(),
        class_code=mock.Mock(),
        id=mock.Mock(),
    )
    instruments_service.get_instrument_by.assert_called_once()


def test_get_dividends(instruments_service):
    responce = instruments_service.get_dividends(  # noqa: F841
        figi=mock.Mock(),
        from_=mock.Mock(),
        to=mock.Mock(),
    )
    instruments_service.get_dividends.assert_called_once()


def test_get_favorites(instruments_service):
    response = instruments_service.get_favorites()  # noqa: F841
    instruments_service.get_favorites.assert_called_once()


def test_get_favorites_with_group(instruments_service):
    response = instruments_service.get_favorites(group_id=mock.Mock())  # noqa: F841
    instruments_service.get_favorites.assert_called_once()


def test_edit_favorites(instruments_service):
    response = instruments_service.edit_favorites(  # noqa: F841
        instruments=mock.Mock(),
        action_type=mock.Mock(),
    )
    instruments_service.edit_favorites.assert_called_once()


def test_create_favorite_group(instruments_service):
    request = mock.Mock()
    response = instruments_service.create_favorite_group(  # noqa: F841
        request=request,
    )
    instruments_service.create_favorite_group.assert_called_once_with(request=request)


def test_delete_favorite_group(instruments_service):
    request = mock.Mock()
    response = instruments_service.delete_favorite_group(  # noqa: F841
        request=request,
    )
    instruments_service.delete_favorite_group.assert_called_once_with(request=request)


def test_get_favorite_groups(instruments_service):
    request = mock.Mock()
    response = instruments_service.get_favorite_groups(  # noqa: F841
        request=request,
    )
    instruments_service.get_favorite_groups.assert_called_once_with(request=request)


def test_get_risk_rates(instruments_service):
    request = mock.Mock()
    response = instruments_service.get_risk_rates(  # noqa: F841
        request=request,
    )
    instruments_service.get_risk_rates.assert_called_once_with(request=request)


def test_get_insider_deals(instruments_service):
    request = mock.Mock()
    response = instruments_service.get_insider_deals(request=request)  # noqa: F841
    instruments_service.get_insider_deals.assert_called_once_with(request=request)


def test_structured_notes(instruments_client_service):
    request = InstrumentsRequest(
        instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL
    )
    response = instruments_client_service.structured_notes(request=request)
    assert len(response.instruments) > 0


def test_structured_notes_by(instruments_client_service):
    request = InstrumentRequest(
        id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id="BBG012S2DCJ8"
    )
    response = instruments_client_service.structured_note_by(request=request)
    assert isinstance(response.instrument, StructuredNote)
