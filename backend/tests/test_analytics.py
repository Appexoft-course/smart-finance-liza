from types import SimpleNamespace

from app.services.analytics_service import (
    calculate_balance,
    calculate_expenses_by_category,
)


def test_calculate_balance():
    transactions = [
        SimpleNamespace(amount=1000, type="income", category_id=1),
        SimpleNamespace(amount=300, type="expense", category_id=1),
        SimpleNamespace(amount=200, type="expense", category_id=2),
    ]

    result = calculate_balance(transactions)

    assert result["income"] == 1000
    assert result["expense"] == 500
    assert result["balance"] == 500


def test_calculate_expenses_by_category():
    transactions = [
        SimpleNamespace(amount=300, type="expense", category_id=1),
        SimpleNamespace(amount=200, type="expense", category_id=1),
        SimpleNamespace(amount=1000, type="income", category_id=2),
    ]

    result = calculate_expenses_by_category(transactions)

    assert result["1"] == 500
    assert "2" not in result