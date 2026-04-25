def calculate_balance(transactions):
    income = sum(t.amount for t in transactions if t.type == "income")
    expense = sum(t.amount for t in transactions if t.type == "expense")

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense,
    }


def calculate_expenses_by_category(transactions):
    result = {}

    for transaction in transactions:
        if transaction.type == "expense":
            category_id = str(transaction.category_id)
            result[category_id] = result.get(category_id, 0) + transaction.amount

    return result