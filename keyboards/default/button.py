from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


foymenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Web-siteni ko'rish"),
            KeyboardButton(text='Ilovani yuklash'),
        ],
        [
            KeyboardButton(text='Web-site oching', web_app=WebAppInfo(url="https://qoradev.pythonanywhere.com/")),
        ],
    ],
    resize_keyboard=True
)

