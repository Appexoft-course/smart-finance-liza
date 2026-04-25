from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.tasks.tasks import calculate_expense_forecast

router = APIRouter(prefix="/forecast", tags=["Forecast"])


@router.post("/expenses")
def create_expense_forecast_task(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    expenses = (
        db.query(Transaction)
        .filter(
            Transaction.user_id == current_user.id,
            Transaction.type == "expense",
        )
        .all()
    )

    total_expense = sum(t.amount for t in expenses)
    months_count = 1

    task = calculate_expense_forecast.delay(total_expense, months_count)

    return {
        "task_id": task.id,
        "status": "forecast task started",
    }


@router.get("/expenses/{task_id}")
def get_expense_forecast_result(task_id: str):
    task = calculate_expense_forecast.AsyncResult(task_id)

    return {
        "task_id": task_id,
        "status": task.status,
        "result": task.result if task.ready() else None,
    }