import os
from dotenv import load_dotenv

load_dotenv()


class BotConfig:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_NAME = os.getenv("DB_NAME", "greeting_db")
    DB_USER = os.getenv("DB_USER", "user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

    @classmethod
    def get_db_url(cls):
        return f"postgresql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}/{cls.DB_NAME}"
    