from celery import Celery
from app.core.config import settings

celery_app = Celery("jobs_worker")

celery_app.conf.broker_url = settings.REDIS_URL
celery_app.conf.result_backend = settings.REDIS_URL

celery_app.conf.task_serializer = "json"
celery_app.conf.accept_content = ["json"]
celery_app.conf.result_serializer = "json"
celery_app.conf.timezone = "UTC"

celery_app.autodiscover_tasks([
    "app.tasks.executor",
    "app.tasks.tasks",
])

print("✅ Celery worker started successfully!")