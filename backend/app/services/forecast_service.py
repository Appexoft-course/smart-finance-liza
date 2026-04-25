def calculate_simple_expense_forecast(total_expense: float, months_count: int = 1):
    if months_count <= 0:
        months_count = 1

    average_expense = total_expense / months_count
    forecast_next_month = average_expense * 1.1

    return {
        "average_expense": round(average_expense, 2),
        "forecast_next_month": round(forecast_next_month, 2),
        "method": "simple_average_plus_10_percent",
    }