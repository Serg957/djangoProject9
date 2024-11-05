from aiogram import Bot, Dispatcher, types,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, Message
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import  logging

from crud_functions_2 import*
import asyncio


logging.basicConfig(level=logging.INFO)
api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb_in = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button1 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb_in.row(button,button1)

kb_in_buy = InlineKeyboardMarkup(resize_keyboard=True)
Product1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
Product2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
Product3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
Product4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb_in_buy.row(Product1, Product2, Product3, Product4)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button1 = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
button_reg = KeyboardButton(text='Регистрация')
kb.row(button, button1)
kb.add(button_buy)
kb.add(button_reg)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью")


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()



@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    data = await state.get_data()

    name = is_included(data['username'])
    if name is True:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()




@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await state.finish()
    await message.answer('Регистрация прошла успешно', reply_markup=kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        with open(f'pic_files/{product[0]}.png', "rb") as img:
            await message.answer_photo(img, f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}")
    await message.answer("Выберите продукт для покупки", reply_markup=kb_in_buy)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()



@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формула Миффлина-Сан Жеора: '
                                 '(10 * вес + 6.25 * рост - 5 * возраст + 5)')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст: (лет)')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['growth'] = int(message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = int(message.text)
        age = data['age']
        growth = data['growth']
        weight = data['weight']

    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5

    await message.answer(f'Ваша норма калорий: {calories} ккал в день.')
    await state.finish()


products_list = get_all_products()
if __name__ == '__main__':


    executor.start_polling(dp, skip_updates=True)
