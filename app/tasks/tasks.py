from celery import current_app
from uuid import UUID
from app.tasks.executor import execute_job


@current_app.task(name="run_job_task", bind=True, max_retries=3)
def run_job_task(self, job_id: UUID):
    """Основная задача Celery"""
    return execute_job(job_id)