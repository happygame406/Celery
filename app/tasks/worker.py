from celery import Celery

celery_app = Celery("jobs_worker")

# Прямые настройки Redis
celery_app.conf.broker_url = "redis://redis:6379/0"
celery_app.conf.result_backend = "redis://redis:6379/0"

celery_app.conf.task_serializer = "json"
celery_app.conf.accept_content = ["json"]
celery_app.conf.result_serializer = "json"
celery_app.conf.timezone = "UTC"

# Регистрация задач
celery_app.autodiscover_tasks(["app.tasks.executor"])

print("✅ Celery worker started successfully!")
print("Broker URL: redis://redis:6379/0")