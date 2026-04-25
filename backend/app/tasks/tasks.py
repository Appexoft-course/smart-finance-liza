from app.tasks.celery_app import celery_app
from app.services.forecast_service import calculate_simple_expense_forecast
from app.tasks.celery_app import celery_app


@celery_app.task
def calculate_expense_forecast(total_expense: float, months_count: int = 1):
    return calculate_simple_expense_forecast(total_expense, months_count)

@celery_app.task
def calculate_expense_forecast(total_expense: float, months_count: int = 1):
    if months_count <= 0:
        months_count = 1

    average_expense = total_expense / months_count
    forecast_next_month = average_expense * 1.1

    return {
        "average_expense": round(average_expense, 2),
        "forecast_next_month": round(forecast_next_month, 2),
        "method": "simple_average_plus_10_percent",
    }