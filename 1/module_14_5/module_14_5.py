from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from crud_functions import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kbrd_start = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [
                                         KeyboardButton(text='Рассчитать'),
                                         KeyboardButton(text='Информация')
                                     ],
                                     [
                                         KeyboardButton(text='Купить')
                                     ],
                                     [
                                         KeyboardButton(text='Регистрация')
                                     ]
                                 ])

kbrd_inline_calc = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)

kbrd_inline_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Product1', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
            InlineKeyboardButton(text='Product3', callback_data='product_buying'),
            InlineKeyboardButton(text='Product4', callback_data='product_buying')
        ]
    ]
)


async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kbrd_start)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):", reply_markup=ReplyKeyboardRemove())
    await RegistrationState.username.set()


async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()


async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer("Регистрация прошла успешно")
    await state.finish()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kbrd_inline_calc)


async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5",
                              reply_markup=ReplyKeyboardRemove())


async def set_age_for_calc(call):
    await call.message.answer("Введите свой возраст:", reply_markup=ReplyKeyboardRemove())
    await UserState.age.set()


async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_norm = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f"Ваша норма калорий: {calories_norm}")
    await state.finish()


async def get_buying_list(message):
    prod = get_all_products()

    for prod_i in prod:
        await message.answer(f"Название: {prod_i[1]} | Описание: {prod_i[2]} | Цена: {prod_i[3]}")
        with open(prod_i[4], "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=kbrd_inline_buy)


async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!", reply_markup=ReplyKeyboardRemove())


api_key = input("Введите ключ к боту:")
bot = Bot(token=api_key)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.message_handler(commands=["start"])(start)

# Машина состояний расчета калорий
dp.message_handler(text='Рассчитать')(main_menu)
dp.callback_query_handler(text='formulas')(get_formulas)
dp.callback_query_handler(text='calories')(set_age_for_calc)
dp.message_handler(state=UserState.age)(set_growth)
dp.message_handler(state=UserState.growth)(set_weight)
dp.message_handler(state=UserState.weight)(send_calories)

# Машина состояний покупки продукта
dp.message_handler(text='Купить')(get_buying_list)
dp.callback_query_handler(text="product_buying")(send_confirm_message)

# Машина состояний регистрации пользователя
dp.message_handler(text='Регистрация')(sing_up)
dp.message_handler(state=RegistrationState.username)(set_username)
dp.message_handler(state=RegistrationState.email)(set_email)
dp.message_handler(state=RegistrationState.age)(set_age)


@dp.message_handler()
async def all_massages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
