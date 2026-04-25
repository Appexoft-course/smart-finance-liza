import pytest

from app.services.transaction_service import (
    is_expense,
    is_income,
    validate_transaction_amount,
)


def test_validate_transaction_amount_success():
    validate_transaction_amount(100)


def test_validate_transaction_amount_error():
    with pytest.raises(ValueError):
        validate_transaction_amount(0)


def test_is_expense():
    assert is_expense("expense") is True
    assert is_expense("income") is False


def test_is_income():
    assert is_income("income") is True
    assert is_income("expense") is False