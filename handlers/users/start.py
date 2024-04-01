from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.button import foymenu
from keyboards.default.adminbutton import adminmenu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMpZBAAAfUO9xqQuhom1S8wBMW98ausAAI4CwACTuSZSzKxR9LZT4zQLwQ')
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} botimga tashrif buyurganingizdan bag'oyatda xursandman !", reply_markup=foymenu),
    if message.from_user.id == int(6182560423):
        await message.answer(f'Assalomu alaykum adminstrator Muhammadbilol botga xush kelibsiz !', reply_markup=adminmenu),
