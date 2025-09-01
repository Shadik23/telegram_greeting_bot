import asyncpg
from config import BotConfig


async def get_db_pool():
    return await asyncpg.create_pool(BotConfig.get_db_url())


async def get_greeting(pool):
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT greeting_text FROM greetings ORDER BY id LIMIT 1")
        return row['greeting_text'] if row else "Привет! Добро пожаловать!"


async def set_greeting(pool, new_text: str):
    async with pool.acquire() as conn:
        await conn.execute(
            "UPDATE greetings SET greeting_text = $1 WHERE id = 1",
            new_text
        )
        await conn.execute(
            """
            INSERT INTO greetings (id, greeting_text)
            VALUES (1, $1)
            ON CONFLICT (id) DO NOTHING;
            """,
            new_text
        )
