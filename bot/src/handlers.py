from aiogram import Router, types
from aiogram.filters import CommandStart
from db import get_greeting

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: types.Message, db_pool) -> None:
    greeting_text = await get_greeting(db_pool)
    await message.answer(greeting_text + "!!!")
