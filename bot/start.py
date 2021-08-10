import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from services import UserService
from decouple import config


API_TOKEN =config('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    _, created = UserService.create_user(message.from_user)
    if created:
        await bot.send_message(message.chat.id, "You are registered")
    else:
        await bot.send_message(message.chat.id, "You are already registered")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
