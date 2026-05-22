# Celery + FastAPI Project

Современный проект на FastAPI + Celery + SQLModel + PostgreSQL + Redis.

## Запуск проекта

```bash
# 1. Клонировать репозиторий
git clone https://github.com/happygame406/Celery
cd Celery

# 2. Пересобрать и запустить все контейнеры
docker-compose down 
docker-compose up -d --build

# 3. Применить миграции
docker-compose exec api alembic upgrade head
