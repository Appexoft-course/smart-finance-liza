def validate_transaction_amount(amount: float):
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than zero")


def is_expense(transaction_type: str) -> bool:
    return transaction_type == "expense"


def is_income(transaction_type: str) -> bool:
    return transaction_type == "income"