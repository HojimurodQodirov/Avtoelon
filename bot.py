import logging
import random
import re
import urllib
import requests
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
import asyncio

from bs4 import BeautifulSoup

from keyboard import keyboard_color, keyboard_currency, keyboard_fuel, keyboard_dwheel, keyboard_transm

API_TOKEN = '7922732370:AAH15y7Sg0qdsoi3VfsZBx2CuW3ybDX9aXA'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()


class Registration(StatesGroup):
    waiting_for_full_name = State()
    waiting_for_phone_number = State()
    waiting_for_password = State()


class AvtoFilter(StatesGroup):
    waiting_for_brends = State()
    waiting_for_name = State()
    waiting_for_position = State()
    waiting_for_fuel = State()
    waiting_for_transmition = State()
    waiting_for_dwheel = State()
    waiting_for_auto_run = State()
    waiting_for_color = State()
    waiting_for_currency = State()
    waiting_for_price_from = State()
    waiting_for_price_to = State()
    waiting_for_year_from = State()
    waiting_for_year_to = State()


@router.message(F.text.in_("/start"))
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Введите ваше полное имя:")
    await state.set_state(Registration.waiting_for_full_name)


@router.message(Registration.waiting_for_full_name)
async def process_full_name(message: Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer("Теперь введите ваш номер телефона (в формате +123456789):")
    await state.set_state(Registration.waiting_for_phone_number)


@router.message(Registration.waiting_for_phone_number)
async def process_phone_number(message: Message, state: FSMContext):
    phone_number = message.text
    if not phone_number.startswith('+') or not phone_number[1:].isdigit():
        await message.answer("Неверный формат номера телефона. Попробуйте снова.")
        return
    await state.update_data(phone_number=phone_number)
    await message.answer("Теперь введите пароль:")
    await state.set_state(Registration.waiting_for_password)


@router.message(Registration.waiting_for_password)
async def process_password(message: Message, state: FSMContext):
    password = message.text
    user_data = await state.get_data()
    user_data['password'] = password

    await message.answer(
        f"Регистрация завершена!\n"
        f"Ваши данные:\n"
        f"Полное имя: {user_data['full_name']}\n"
        f"Номер телефона: {user_data['phone_number']}\n"
        f"Пароль: {user_data['password']}"
    )

    await state.clear()


@router.message(F.text.in_("/car"))
async def parser(message: types.Message, state: FSMContext):
    await message.answer("Введите имя бренда:")
    await state.set_state(AvtoFilter.waiting_for_brends)


@router.message(AvtoFilter.waiting_for_brends)
async def process_brends(message: Message, state: FSMContext):
    brends = message.text.lower()
    await state.update_data(brends=brends)
    await message.answer("Теперь введите имя машины:")
    await state.set_state(AvtoFilter.waiting_for_name)


@router.message(AvtoFilter.waiting_for_name)
async def process_car_name(message: Message, state: FSMContext):
    name = message.text.lower()
    await state.update_data(name=name)
    await message.answer("Теперь введите позицию:")
    await state.set_state(AvtoFilter.waiting_for_position)


@router.message(AvtoFilter.waiting_for_position)
async def process_position(message: Message, state: FSMContext):
    position = message.text
    await state.update_data(position=position)
    await message.answer("Теперь введите тип топлива:", reply_markup=keyboard_fuel)
    await state.set_state(AvtoFilter.waiting_for_fuel)


@router.message(AvtoFilter.waiting_for_fuel)
async def process_fuel(message: Message, state: FSMContext):
    fuel = message.text
    if fuel == "benzin":
        await state.update_data(fuel="1")
    elif fuel == "gaz":
        await state.update_data(fuel="2")
    elif fuel == "dizel":
        await state.update_data(fuel="3")
    elif fuel == "elektrichestvo":
        await state.update_data(fuel="4")
    elif fuel == "gibrid":
        await state.update_data(fuel="5")

    await message.answer("Теперь введите коробку передач:", reply_markup=keyboard_transm)
    await state.set_state(AvtoFilter.waiting_for_transmition)


@router.message(AvtoFilter.waiting_for_transmition)
async def process_transmition(message: Message, state: FSMContext):
    transmition = message.text
    if transmition == "mehanik":
        await state.update_data(transmition="1")
    elif transmition == "avtomat":
        await state.update_data(transmition="2")
    await message.answer("Теперь введите привод:", reply_markup=keyboard_dwheel)
    await state.set_state(AvtoFilter.waiting_for_dwheel)


@router.message(AvtoFilter.waiting_for_dwheel)
async def process_dwheel(message: Message, state: FSMContext):
    dwheel = message.text
    if dwheel == "передний":
        await state.update_data(dwheel="1")
    elif dwheel == "задний":
        await state.update_data(dwheel="2")
    elif dwheel == "полный":
        await state.update_data(dwheel="3")

    await message.answer("Теперь введите макс. пробег:")
    await state.set_state(AvtoFilter.waiting_for_auto_run)


@router.message(AvtoFilter.waiting_for_auto_run)
async def process_auto_run(message: Message, state: FSMContext):
    auto_run = message.text
    await state.update_data(auto_run=auto_run)

    await message.answer("Теперь выберите цвет:", reply_markup=keyboard_color)
    await state.set_state(AvtoFilter.waiting_for_color)


@router.message(AvtoFilter.waiting_for_color)
async def process_color(message: Message, state: FSMContext):
    color = message.text
    if color == "Молочный цвет":
        await state.update_data(color="1")
    elif color == "Дельфин":
        await state.update_data(color="2")
    elif color == "Мокрый асфальт":
        await state.update_data(color="3")
    elif color == "Церный":
        await state.update_data(color="4")
    elif color == "Серебристый":
        await state.update_data(color="5")
    elif color == "Carana":
        await state.update_data(color="6")
    elif color == "Перламутрово-коричневый":
        await state.update_data(color="7")
    elif color == "Мелто-зеланый":
        await state.update_data(color="8")
    elif color == "Сича-голубой":
        await state.update_data(color="9")
    elif color == "Вишня":
        await state.update_data(color="10")
    elif color == "Синий":
        await state.update_data(color="11")
    elif color == "Красный":
        await state.update_data(color="12")
    elif color == "Серый":
        await state.update_data(color="13")
    elif color == "Коричневый":
        await state.update_data(color="14")
    elif color == "Бронза":
        await state.update_data(color="15")
    elif color == "Хамелеон":
        await state.update_data(color="16")
    elif color == "Бирюзовый":
        await state.update_data(color="17")
    elif color == "Бежевый":
        await state.update_data(color="18")
    elif color == "Бордовый":
        await state.update_data(color="19")
    elif color == "Голубой":
        await state.update_data(color="20")
    elif color == "Жёлтый":
        await state.update_data(color="21")
    elif color == "Зеленый":
        await state.update_data(color="22")
    elif color == "Сиреневый":
        await state.update_data(color="23")
    elif color == "Золотистый":
        await state.update_data(color="24")
    elif color == "Оранжевый":
        await state.update_data(color="25")

    await message.answer("Теперь выберите валюту:", reply_markup=keyboard_currency)
    await state.set_state(AvtoFilter.waiting_for_currency)


@router.message(AvtoFilter.waiting_for_currency)
async def process_currency(message: Message, state: FSMContext):
    currency = message.text
    if currency == "sum":
        await state.update_data(currency="2")
    elif currency == "e.y":
        await state.update_data(currency="1")
    keyboard_remove = ReplyKeyboardRemove()

    await message.answer("Теперь введите минимальную цену.", reply_markup=keyboard_remove)
    await state.set_state(AvtoFilter.waiting_for_price_from)


@router.message(AvtoFilter.waiting_for_price_from)
async def process_price_from(message: Message, state: FSMContext):
    price_from = message.text
    await state.update_data(price_from=price_from)
    await message.answer("Теперь введите максимальную цену:")
    await state.set_state(AvtoFilter.waiting_for_price_to)


@router.message(AvtoFilter.waiting_for_price_to)
async def process_price_to(message: Message, state: FSMContext):
    price_to = message.text
    await state.update_data(price_to=price_to)
    await message.answer("Теперь введите минимальный год выпуска:")
    await state.set_state(AvtoFilter.waiting_for_year_from)


@router.message(AvtoFilter.waiting_for_year_from)
async def process_year_from(message: Message, state: FSMContext):
    year_from = message.text
    await state.update_data(year_from=year_from)
    await message.answer("Теперь введите максимальный год выпуска:")
    await state.set_state(AvtoFilter.waiting_for_year_to)





@router.message(AvtoFilter.waiting_for_year_to)
async def process_year_to(message: Message, state: FSMContext):
    year_to = message.text
    await state.update_data(year_to=year_to)

    filter_data = await state.get_data()
    brends = urllib.parse.quote(filter_data.get('brends', ''))
    name = urllib.parse.quote(filter_data.get('name', ''))
    position = urllib.parse.quote(filter_data.get('position', ''))
    fuel = filter_data.get('fuel', '')
    transmition = filter_data.get('transmition', '')
    dwheel = filter_data.get('dwheel', '')
    auto_run = urllib.parse.quote(filter_data.get('auto_run', ''))
    color = filter_data.get('color', '')
    currency = filter_data.get('currency', '')
    year_from = filter_data.get('year_from', '')
    year_to = filter_data.get('year_to', '')

    url = f"https://avtoelon.uz/avto/sedan/{brends}/{name}/pozitsiya-{position}/?auto-fuel={fuel}&auto-car-transm={transmition}&car-dwheel={dwheel}&auto-run[to]={auto_run}&auto-color={color}&price-currency={currency}&price[from]=1%20111&price[to]=19%20000&year[from]={year_from}&year[to]={year_to}"

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    posts = soup.find_all('div', class_='row list-item a-elem')

    random.shuffle(posts)

    posts = posts[:10]

    for post in posts:
        image = post.find('img')['src'] if post.find('img') else None
        title = post.find('a', class_='a-el-info-title').text.strip() if post.find('a',
                                                                                   class_='a-el-info-title') else None
        relative_link = post.find('a', class_='a-el-info-title')['href'] if post.find('a',
                                                                                      class_='a-el-info-title') else None
        full_link = f"{url}{relative_link}" if relative_link else None
        price = post.find('span', class_='price').text.strip() if post.find('span', class_='price') else None
        description = post.find('div', class_='desc').text.strip() if post.find('div', class_='desc') else None
        region = post.find('a', class_='a-info-text__region').text.strip() if post.find('a',
                                                                                        class_='a-info-text__region') else None
        date = post.find('span', class_='date').text.strip() if post.find('span', class_='date') else None
        views = post.find('span', class_='nb-views-int').text.strip() if post.find('span',
                                                                                   class_='nb-views-int') else None
        description = re.sub(r'\s+', ' ', description) if description else None

        # await bot.send_photo(message.chat.id, photo=f'{image}')
        await message.answer(photo=f'{image}', text=f"{description}\n{price}\n{region}\n{date}\n{views}")


if __name__ == "__main__":
    dp.include_router(router)

    async def main():
        await dp.start_polling(bot)

    asyncio.run(main())