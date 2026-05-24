# 🎯 Система фоновых задач — Celery + FastAPI

Современный проект для выполнения асинхронных задач с использованием **FastAPI**, **Celery**, **Redis** и **PostgreSQL**.

---

## ✨ Реализованные задачи

| Задача                    | Описание                                              | Статус |
|--------------------------|-------------------------------------------------------|--------|
| `HTTP_CHECK`             | Проверка доступности веб-сайта                        | ✅     |
| `WORD_STATS`             | Анализ частоты слов на странице                       | ✅     |
| `WORD_STATS_COMPARE`     | Сравнение результатов анализа двух страниц            | ✅     |
| `DICE_COMBS_SIMULATION`  | Симуляция бросков 5 кубиков (метод Монте-Карло)       | ✅     |

---

## 🚀 Быстрый запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/happygame406/Celery.git
cd Celery

# 2. Запустить проект
docker-compose down
docker-compose up -d --build

# 3. Применить миграции
docker-compose exec api alembic upgrade head
```
## 📍 Полезные ссылки

Главный API: http://localhost:8000
Swagger (документация): http://localhost:8000/docs
---
## 🎲 Примеры запросов
### 1. Симуляция кубиков (Monte Carlo)
```bash
JSON{
  "title": "Симуляция кубиков",
  "job_type": "DICE_COMBS_SIMULATION",
  "payload": {
    "trials": 50000
  }
}
```

### 2. Анализ слов на странице
```bash
JSON{
  "title": "Анализ python.org",
  "job_type": "WORD_STATS",
  "payload": {
    "url": "https://www.python.org/",
    "top_n": 15
  }
}
```

### 3. Сравнение двух страниц
```bash
JSON{
  "title": "Сравнение двух сайтов",
  "job_type": "WORD_STATS_COMPARE",
  "payload": {
    "left_job_id": "uuid_первой_задачи",
    "right_job_id": "uuid_второй_задачи"
  }
}
```
---
## 🛠 Технологии

Backend: FastAPI
Фоновые задачи: Celery + Redis
База данных: PostgreSQL + SQLModel
Миграции: Alembic
Контейнеризация: Docker Compose
---
## 📌 Особенности

Полная асинхронная обработка задач
Валидация входных данных
Обработка ошибок и логирование
Сохранение всех результатов в базу данных
Удобная документация через Swagger UI
