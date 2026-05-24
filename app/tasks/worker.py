from celery import Celery
from app.core.config import settings
from app.tasks.executor import execute_job   # ← прямой импорт

celery_app = Celery("jobs_worker")

celery_app.conf.broker_url = settings.REDIS_URL
celery_app.conf.result_backend = settings.REDIS_URL

celery_app.conf.task_serializer = "json"
celery_app.conf.accept_content = ["json"]
celery_app.conf.result_serializer = "json"
celery_app.conf.timezone = "UTC"

# Прямая регистрация задачи
celery_app.task(name="run_job_task")(execute_job)

print("✅ Celery worker started with direct task registration")
print("Registered task: run_job_task")

if __name__ == "__main__":
    celery_app.start()