FROM python:3.9-slim-buster

WORKDIR /app

# Копируем файл зависимостей из папки bot
COPY bot/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код из папки bot/src
COPY bot/src/. /app/

ENV PYTHONUNBUFFERED 1

CMD ["python", "main.py"]