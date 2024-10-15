from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api_key = input("Введите ключ к боту:")
bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=MemoryStorage())

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
btn_calculate = KeyboardButton(text='Рассчитать')
btn_info = KeyboardButton(text='Информация')
keyboard.add(btn_calculate)
keyboard.insert(btn_info)

kbrd_inline = InlineKeyboardMarkup()
btn_calc_cal = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
btn_formulas_cal = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kbrd_inline.add(btn_calc_cal)
kbrd_inline.add(btn_formulas_cal)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=keyboard)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kbrd_inline)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5",
                              reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:", reply_markup=ReplyKeyboardRemove())
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_norm = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f"Ваша норма калорий: {calories_norm}")
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
