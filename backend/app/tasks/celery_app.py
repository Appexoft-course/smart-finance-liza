from celery import Celery

from app.config import settings

CELERY_BROKER_URL = f"redis://{settings.redis_host}:{settings.redis_port}/0"
CELERY_RESULT_BACKEND = f"redis://{settings.redis_host}:{settings.redis_port}/1"

celery_app = Celery(
    "smart_finance",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
)

celery_app.autodiscover_tasks(["app.tasks"])