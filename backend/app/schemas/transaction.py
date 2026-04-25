from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    type: Literal["income", "expense"]
    category_id: int


class TransactionResponse(BaseModel):
    id: int
    title: str
    amount: float
    type: str
    category_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class TransactionUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    amount: float | None = Field(default=None, gt=0)
    type: Literal["income", "expense"] | None = None
    category_id: int | None = None