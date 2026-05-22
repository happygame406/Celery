# Celery + FastAPI Project

Современный проект на FastAPI + Celery + SQLModel + PostgreSQL + Redis.

## Запуск проекта

```bash
# 1. Клонировать репозиторий
git clone <your-repo>
cd Celery

# 2. Запуск через Docker Compose
docker-compose up -d --build

# 3. Применить миграции
docker-compose exec api alembic upgrade head