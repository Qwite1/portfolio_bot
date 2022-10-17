import asyncio

from aiogram import Router, F, Bot, types
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database.db import mongo_easy_insert, mongo_easy_upsert
from handlers.client.main_menu import select_language
from keyboards.main_menu_kb import main_kb
from states.admin_state import Admin_menu
from utils.language_distributor import distributor

router = Router()
router.message.filter()

flags = {"throttling_key": "True"}

@dp.message_handler((F.text == '💸 Цены'))
async def price(message: types.Message):
    await db.add_statistics_bot_price()
    await message.answer("Выберите интересующий раздел")


@dp.message_handler((F.text == '🎁 Готовое решение'))
async def turnkey_solution(message: types.Message):
    await message.answer("Готовое решение - бот с небольшим функционалом, включающий в себя стандартный набор функций и админку для настройки", reply_markup=client_kb.price)
    await message.answer("FAQ-бот включает в себя:\n\n"
                         "⚪️ Приветственное сообщение\n"
                         "⚪️ Раздел 'О нас'\n"
                         "⚪️ Раздел 'Контакты'\n"
                         "⚪️ Раздел 'Товары/Услуги'\n"
                         "⚪️ Админку для редактирования текста\n\n"
                         "Стоимость такого бота - <b>500р</b>\n\n"
                         "Доп. услуги:\n\n"
                         "🔵 Загрузка на ваш сервер - 200р\n"
                         "🔵 Другие доработки обсуждаются индивидуально")
    await message.answer("Интернет магазин на примере @Gardelia_Flowers_bot\n"
                         "Магазин включает в себя:\n\n"
                         "⚪️ Приветственное сообщение\n"
                         "⚪️ Каталог с возможностью пополнения\n"
                         "⚪️ Обратную связь\n"
                         "⚪️ Базу клиентов\n"
                         "⚪️ Рассылку подписчикам\n"
                         "⚪️ Статистику внутри бота\n"
                         "⚪️ И другие незначительные функции\n\n"
                         "Стоимость такого бота - <b>3000р</b>\n\n"
                         "Доп. услуги:\n\n"
                         "🔵 Настройка бота - 200р\n"
                         "🔵 Загрузка на ваш сервер - 200р\n"
                         "🔵 Другие доработки обсуждаются индивидуально\n")


@dp.message_handler((F.text == '🗝 Индивидуальная разработка'))
async def price(message: types.Message):
    await message.answer("Индивидуальная разработка - комплексное решение по созданию бота")
    await message.answer("Разработка бота с нуля, подразумевает проработку ТЗ, создание базы данных, написание бота, исправление ошибок и многое другое.\n\n"
                         "Цена на создание чат-бота складывается исходя из сложности, поэтому имеет смысл назвать минимальную стоимость бота.\n\n"
                         "Минимальная цена: 4000р\n\n"
                         "После создания чат-бота, от меня вы получите дальнейшую поддержку и бесплатную консультацию")