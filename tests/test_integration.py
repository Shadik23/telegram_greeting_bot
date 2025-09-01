import pytest
import httpx
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env.test')

BASE_URL = "http://localhost:8000"
ADMIN_USER = os.getenv("WEB_USERNAME")
ADMIN_PASSWORD = os.getenv("WEB_PASSWORD")
AUTH = (ADMIN_USER, ADMIN_PASSWORD)

@pytest.mark.asyncio
async def test_full_greeting_cycle():
    async with httpx.AsyncClient(timeout=10) as client:
        response_before = await client.get(BASE_URL + "/", auth=AUTH)
        assert response_before.status_code == 200
        assert response_before.json()["current_greeting_text"] == "Привет! Добро пожаловать!"

        new_text = "Автотест прошел успешно!"
        update_payload = {"new_greeting_text": new_text}
        response_update = await client.post(BASE_URL + "/update_greeting", json=update_payload, auth=AUTH)
        assert response_update.status_code == 200
        assert response_update.json()["current_greeting_text"] == new_text
 
        response_after = await client.get(BASE_URL + "/", auth=AUTH)
        assert response_after.status_code == 200
        assert response_after.json()["current_greeting_text"] == new_text
        