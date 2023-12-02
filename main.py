import sys
import os
import asyncio
import platform
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command

# to access bot
TOKEN = os.environ.get("BOT_TOKEN")
# to get updates from telegram
dp = Dispatcher()

# that is dependency injection right there, decoupling objects, rather than using it directly
@dp.message(Command("start", prefix="/"))
async def start_handler(message: Message):
    await message.answer(text="Greetings in the Land of Ooo")

# the order is matter, because it looks for filters it passes, but if no filters is there, then this handler will be picked
@dp.message(lambda message: message.text == "test") # also could be done with F.text == "test"
async def test_message_handler(message: Message):
    await message.answer(text="Test is completed successefully")

@dp.message()
async def any_message_handler(message: Message):
    await message.answer(text=f"Your name is {message.chat.username} and this bot is running on {platform.system()}")


@dp.edited_message()
async def edited_message_handler(message: Message):
    await message.answer(text="Gatcha")

async def main() -> None:
    if TOKEN is not None:
        bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
        await dp.start_polling(bot)
    else:
        print("token is null")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
