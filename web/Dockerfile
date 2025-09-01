FROM python:3.9-slim-buster

WORKDIR /app

# Копируем файл зависимостей из папки web
COPY web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код из папки web/src
COPY web/src/. /app/

ENV PYTHONUNBUFFERED 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]