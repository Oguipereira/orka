from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "orka",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["app.workers.tasks"],
)

celery_app.conf.beat_schedule = {
    "sync-data-every-hour": {
        "task": "app.workers.tasks.sync_all_integrations",
        "schedule": 3600.0,
    },
    "calculate-metrics-daily": {
        "task": "app.workers.tasks.calculate_metrics",
        "schedule": 86400.0,
    },
}
