from enum import Enum
import sys
import os
import asyncio
import platform
import logging


from aiogram import Bot, Dispatcher, F, Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
# to access bot
TOKEN = os.environ.get("BOT_TOKEN")
# to get updates from telegram
dp = Dispatcher()

my_router =Router(name="my_router")

dp.include_router(my_router)


class Review(StatesGroup):
    name = State()
    age = State()
    rate = State()

# ---------- flow -----------
@my_router.message(F.text == "my router")
async def my_handler(message: Message):
    await message.answer(text="from my router")


# that is dependency injection right there, decoupling objects, rather than using it directly
@dp.message(Command("start", prefix="/"))
async def start_handler(message: Message):
    await message.answer(text="Greetings in the Land of Ooo")


# the order is matter, because it looks for filters it passes, but if no filters is there, then this handler will be picked
@dp.message(lambda message: message.text == "test") # also could be done with F.text == "test"
async def test_message_handler(message: Message):
    await message.answer(text="Test is completed successefully")

@dp.message(F.text == "whoami")
async def any_message_handler(message: Message):
    await message.answer(text=f"Your name is {message.chat.username} and this bot is running on {platform.system()}")

@dp.message(Command("review", prefix="/"))
async def start_review_handler(message: Message, state: FSMContext):
    await state.set_state(Review.name)
    await message.answer(text="what is your name?")

# listen for the name
@dp.message(Review.name)
async def process_name_handler(message: Message, state: FSMContext):
    await state.set_state(state=Review.age)
    await message.answer(text=f"your name {message.text}")


@dp.message(Review.age)
async def process_age_handler(message: Message, state: FSMContext):
    await state.set_state(state=Review.rate)
    await message.answer(f"you are {message.text}yo")

@dp.message(Review.rate)
async def process_rate_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=f"you rated us with {message.text}, thx")

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
