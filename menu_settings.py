from aiogram import F, Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
router = Router()
#dp = Dispatcher()
#dp.include_router(router)

async def handle_menu_command(message: types.Message):
    menu_first_btn = InlineKeyboardButton(
        text="Самое быстрое меню", callback_data="menu_first_btn"
    )

    menu_second_btn = InlineKeyboardButton(
        text="Летнее меню", callback_data="menu_second_btn"
    )

    menu_third_btn = InlineKeyboardButton(
        text="Меню на любой вкус",
        callback_data="menu_third_btn"
    )

    menu_fourth_btn = InlineKeyboardButton(
        text="Универсальное меню",
        callback_data="menu_fourth_btn"
    )

    menu_fifth_btn = InlineKeyboardButton(
        text="Итальяское меню",
        callback_data="menu_fifth_btn"
    )

    menu_sixth_btn = InlineKeyboardButton(
        text="Веганское меню",
        callback_data="menu_sixth_btn"
    )

    menu_seventh_btn = InlineKeyboardButton(
        text="Турецкая неделя",
        callback_data="menu_seventh_btn"
    )

    rows = [
        [menu_first_btn],
        [menu_second_btn],
        [menu_third_btn],
        [menu_fourth_btn],
        [menu_fifth_btn],
        [menu_sixth_btn],
        [menu_seventh_btn]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)

    await message.answer(
        text=f"Выберите один из вариантов меню:",
        reply_markup=markup)


async def process_menu_buttons(callback_query: types.CallbackQuery):
    button_data = callback_query.data
    if button_data == 'menu_first_btn':
        # Действия для первой кнопки
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Вы выбрали 'Самое быстрое меню'."
        )
    elif button_data == 'menu_second_btn':
        # Действия для второй кнопки
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Вы выбрали 'Летнее меню'."
        )
    elif button_data == 'menu_third_btn':
        # Действия для третьей кнопки
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Вы выбрали 'Меню на любой вкус'."
        )
