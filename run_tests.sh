set -e

echo "--- 1. Запуск тестового окружения (используя .env.test) ---"
docker compose -f docker-compose.yml -f docker-compose.override.yml --env-file .env.test up -d --build --force-recreate

echo "--- 2. Ожидание готовности Базы Данных ---"
retries=15
while [ $retries -gt 0 ]; do
    docker compose exec -T db pg_isready -U user -d greeting_db_test && break
    retries=$((retries-1))
    echo "Ожидание БД... Осталось попыток: $retries"
    sleep 2
done
if [ $retries -eq 0 ]; then
    echo "!!! База Данных не запустилась вовремя. Проверьте логи."
    exit 1
fi
echo "--- База Данных готова! ---"


echo "--- 3. Установка Python-зависимостей для тестов ---"
pip3 install -r requirements.test.txt

echo "--- 4. ЗАПУСК ТЕСТОВ ---"
pytest tests/

TEST_EXIT_CODE=$?

echo "--- 5. Очистка: остановка и удаление тестового окружения ---"
docker compose -f docker-compose.yml -f docker-compose.override.yml --env-file .env.test down -v

exit $TEST_EXIT_CODE
