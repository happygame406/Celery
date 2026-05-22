<<<<<<< HEAD
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
FROM python:3.14-slim

WORKDIR /app

ENV PYTHONDONTWRYTEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENTRYPOINT ["celery", "-A", "app.core.celery_app:celery_app", "worker", "--loglevel=info"]
CMD ["-Q", "default", "--hostname=default@%h", "-c", "1"]
>>>>>>> 6cb3aec290b93be653045ba185c05f0837820868
