from fastapi import FastAPI
from sqlalchemy import text

from app.database import Base, engine
from app.core.dependencies import get_db
from app.models import user, category, transaction
from app.routers import auth, categories, transactions, forecast
from app.routers import analytics
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Smart Finance API",
    description="API for personal finance management and expense forecasting",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(transactions.router)
app.include_router(forecast.router)
app.include_router(analytics.router)
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Smart Finance API is running"}


@app.get("/health")
def health_check():
    db = next(get_db())
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "db": "ok"}
    except Exception:
        return {"status": "error", "db": "error"}
    finally:
        db.close()