import asyncio
import logging
from aiogram import F, Router, types
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import security
#from aiogram.utils.chat_action import ChatActionSender
from aiogram.enums import ParseMode, ChatAction
#from aiogram.types import InlineKeyboardMarkup
#from aiogram.utils.keyboard import InlineKeyboardBuilder

bot= Bot(token=security.TOKEN)
dp = Dispatcher()

#router = Router(name=__name__)

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://ibb.co/0JH1C6K"
    await message.answer_photo(photo=url,
                               caption=f"Здравствуй, <b>{message.from_user.full_name}</b>!\n"
                         f"Выбирай подходящий рецепт/меню и твори!",
                               action=ChatAction.UPLOAD_PHOTO,
                               parse_mode=ParseMode.HTML)


@dp.message(Command("menu"))
async def handle_menu_command(message: types.Message):
    menu_first_btn = InlineKeyboardButton(
        text="Самое быстрое меню", url="https://www.youtube.com/shorts/bvJN1NS7nsY")
    btn_one = InlineKeyboardButton(
        text="Самое быстрое меню",
        url="https://www.youtube.com/shorts/bvJN1NS7nsY")
    row = [menu_first_btn]
    rowg = [btn_one]
    rows = [row, rowg]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text=f"Ссылки на загатовки:",
        reply_markup=markup)

@dp.message(Command("menu"))
async def handle_menu_command(message: types.Message):
    btn = InlineKeyboardButton(text="Самое быстрое меню")
    await message.answer(text=f"Выберите один из 7 вариантов меню на неделю:",
                         reply_markup=markup)

@dp.message(Command("ideas"))
async def handle_menu(message: types.Message):
    await message.answer(f"Что приготовить на:")

@dp.message(Command("search"))
async def handle_menu(message: types.Message):
    await message.answer(f"Давай попробуем найти рецепт!")

@dp.message(Command("cooking_from"))
async def handle_menu(message: types.Message):
    await message.answer(f"Что приготовить из...")

@dp.message(Command("digest"))
async def handle_menu(message: types.Message):
    await message.answer(f"Тематические сборники рецептов:")

@dp.message(Command("otmena"))
async def handle_menu(message: types.Message):
    await message.answer(f"Если вы уверенны, что хотите отменить подписку - нажмите кнопку ниже 🔽")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
