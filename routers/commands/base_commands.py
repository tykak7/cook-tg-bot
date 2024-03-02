from aiogram import F, Router, types
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import CommandStart, Command

from ideas_settings import handle_ideas_command
from menu_settings import handle_menu_command

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://ibb.co/0JH1C6K"
    await message.answer_photo(photo=url,
                               caption=f"Здравствуй, <b>{message.from_user.full_name}</b>!\n"
                                       f"Ты легко можешь ориентироваться в боте с помощью меню. Можешь совершить поиск рецепта, выбрать меню на неделю и т.д.",
                               action=ChatAction.UPLOAD_PHOTO,
                               parse_mode=ParseMode.HTML)


@router.message(Command("menu"))
async def handle_menu(message: types.Message):
    await handle_menu_command(message)


@router.message(Command("ideas"))
async def handle_ideas(message: types.Message):
    await handle_ideas_command(message)


@router.message(Command("search"))
async def handle_search(message: types.Message):
    await message.answer(f"Давай попробуем найти рецепт!")


@router.message(Command("cooking_from"))
async def handle_cooking_from(message: types.Message):
    await message.answer(f"Что приготовить из...")


@router.message(Command("digest"))
async def handle_digest(message: types.Message):
    await message.answer(f"Тематические сборники рецептов:")


@router.message(Command("otmena"))
async def handle_otmena(message: types.Message):
    await message.answer(f"Если вы уверенны, что хотите отменить подписку - нажмите кнопку ниже 🔽")
