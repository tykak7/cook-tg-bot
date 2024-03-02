import asyncio
import logging
from aiogram import types
from aiogram import Bot, Dispatcher

#import menu_settings
import security
#from routers.commands.base_commands import router
from routers import router as main_router

bot= Bot(token=security.TOKEN)
dp = Dispatcher()
dp.include_router(main_router)

#router = Router(name=__name__)


#@Dispatcher(bot).callback_query_handler(lambda c: c.data.startswith('menu_first_btn'))
@dp.callback_query(lambda c: c.data == 'menu_first_btn')
async def new_menu_buttons(callback_query: types.CallbackQuery):
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
            text="Вы выбрали 'Летнее меню'.")

    elif button_data == 'menu_third_btn':
        # Действия для третьей кнопки
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Вы выбрали 'Меню на любой вкус'."
        )
    await new_menu_buttons(callback_query)

    #await bot.answer_callback_query(callback_query.id)
    #await bot.send_message(callback_query.from_user.id, 'Well done!')
#async def menu_button_process(callback_query: types.CallbackQuery):
#    await process_menu_button


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
