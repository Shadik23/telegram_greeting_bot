import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BotConfig
from handlers import router
from db import get_db_pool


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BotConfig.BOT_TOKEN)
    dp = Dispatcher()

    db_pool = await get_db_pool()
    dp["db_pool"] = db_pool

    dp.include_router(router)

    logging.info("Starting bot...")
    await dp.start_polling(bot)

    await db_pool.close()
    logging.info("Bot stopped.")


if __name__ == "__main__":
    asyncio.run(main())
    