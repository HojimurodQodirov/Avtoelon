from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard_color = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Молочный цвет")],
            [KeyboardButton(text="Дельфин")],
            [KeyboardButton(text="Мокрый асфальт")],
            [KeyboardButton(text="Церный")],
            [KeyboardButton(text="Серебристый")],
            [KeyboardButton(text="Carana")],
            [KeyboardButton(text="Перламутрово-коричневый")],
            [KeyboardButton(text="Мелто-зеланый")],
            [KeyboardButton(text="Сича-голубой")],
            [KeyboardButton(text="Вишня")],
            [KeyboardButton(text="Синий")],
            [KeyboardButton(text="Красный")],
            [KeyboardButton(text="Серый")],
            [KeyboardButton(text="Коричневый")],
            [KeyboardButton(text="Бронза")],
            [KeyboardButton(text="Хамелеон")],
            [KeyboardButton(text="Бирюзовый")],
            [KeyboardButton(text="Бежевый")],
            [KeyboardButton(text="Бордовый")],
            [KeyboardButton(text="Голубой")],
            [KeyboardButton(text="Жёлтый")],
            [KeyboardButton(text="Зеленый")],
            [KeyboardButton(text="Сиреневый")],
            [KeyboardButton(text="Золотистый")],
            [KeyboardButton(text="Оранжевый")]
        ],
        resize_keyboard=True
    )

keyboard_currency = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="sum")],
            [KeyboardButton(text="e.y")]
        ],
        resize_keyboard=True
    )

keyboard_fuel = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="benzin")],
            [KeyboardButton(text="gaz")],
            [KeyboardButton(text="dizel")],
            [KeyboardButton(text="elektrichestvo")],
            [KeyboardButton(text="gibrid")],
        ],
        resize_keyboard=True
    )

keyboard_transm = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="mehanik")],
            [KeyboardButton(text="avtomat")]
        ],
        resize_keyboard=True
    )

keyboard_dwheel = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="передний")],
            [KeyboardButton(text="задний")],
            [KeyboardButton(text="полный")],

        ],
        resize_keyboard=True
    )
