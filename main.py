import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties

import config

API_TOKEN = config.token

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

# Кнопки меню
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О нас"), KeyboardButton(text="Наш сайт"), KeyboardButton(text="Наша помощь")],
        [KeyboardButton(text="Контакты"), KeyboardButton(text="Важно!")],
    ],
    resize_keyboard=True  # подгоняет под размер экрана
)

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Привет! Я бот организации Коснуться горизонта. Выбери из кнопок меню, что бы ты хотел узнать.",
        reply_markup=menu_keyboard
    )

@dp.message()
async def handle_buttons_and_echo(message: Message):
    text = message.text.lower()

    if text == "о нас":
        await message.answer_photo(
            photo="https://genlogo.com/u_ajax?handler=GenLogo&command=ajax_site_get_colors&t=%D0%9A%D0%BE%D1%81%D0%BD%D1%83%D1%82%D1%8C%D1%81%D1%8F%20%D0%93%D0%BE%D1%80%D0%B8%D0%B7%D0%BE%D0%BD%D1%82%D0%B0&s=%D0%91%D0%BB%D0%B0%D0%B3%D0%BE%D1%82%D0%B2%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D0%9E%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F&g=0&l=234790&f=284078&c=288885&x=1744031963&oid=554615") ,
        await message.answer("Организация «Коснуться Горизонта» оказывает поддержку детям с инвалидностью и их семьям.")
    elif text == "наш сайт" :
        await message.answer("https://project12495565.tilda.ws/")
    elif text == "наша помощь":
        await message.answer("Мы предоставляем информационную, юридическую и психологическую поддержку семьям, имеющим ребенка-инвалида")
    elif text == "контакты":
        await message.answer("Наши контакты: \n\nEmail: touchthehorizon@email.ru\n\nПрисоединяйтесь к нам в ВКонтакте: [https://vk.com/club227624425?from=groups]")

    elif text == "важно!":
        await message.answer("Помните, помощь детям с инвалидностью важна для их развития и интеграции в общество. Это даёт им шанс на полноценную жизнь, обучение и самореализацию, а также способствует уменьшению барьеров и предвзятости.")
    else:
        await message.reply(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



