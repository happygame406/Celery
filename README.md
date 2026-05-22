# Celery + FastAPI Project 🚀

Современный проект на **FastAPI + Celery + Redis + PostgreSQL**, предназначенный для работы с фоновыми задачами.

Поддерживаемые типы задач:
- `HTTP_CHECK` — проверка доступности сайта
- `WORD_STATS` — анализ частоты слов на странице
- `WORD_STATS_COMPARE` — сравнение результатов двух анализов
- `DICE_COMBS_SIMULATION` — симуляция бросков кубиков методом Монте-Карло 🎲

---

## Ссылки

- **Главный сайт (API)**: [http://localhost:8000](http://localhost:8000) 🌐
- **Интерактивная документация (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs) 📘
- **Альтернативная документация (Redoc)**: [http://localhost:8000/redoc](http://localhost:8000/redoc) 📖

---

## Запуск проекта

```bash
# 1. Клонировать репозиторий
git clone https://github.com/happygame406/Celery.git
cd Celery

# 2. Пересобрать и запустить все контейнеры
docker-compose down
docker-compose up -d --build

# 3. Применить миграции базы данных
docker-compose exec api alembic upgrade head
