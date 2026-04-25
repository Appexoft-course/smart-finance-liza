from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.services.analytics_service import (
    calculate_balance,
    calculate_expenses_by_category,
)

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/balance")
def get_balance(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    transactions = db.query(Transaction).filter(
        Transaction.user_id == current_user.id
    ).all()

    return calculate_balance(transactions)


@router.get("/expenses-by-category")
def get_expenses_by_category(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    transactions = db.query(Transaction).filter(
        Transaction.user_id == current_user.id
    ).all()

    return calculate_expenses_by_category(transactions)