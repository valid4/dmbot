from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.emoji import emojize
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add('Записаться').add('Свободные даты').add('Отзывы').add('Контакты').add('Справка')

kb_adm = ReplyKeyboardMarkup(resize_keyboard=True)
kb_adm.add('Записаться').add('Свободные даты').add('Отзывы').add('Контакты').add('Справка').add('Admin_Panel')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Изменить отзывы').add('Изменить Контакты').add('Изменить Справку').add('Изменить Свободные даты').add('Рассылка').add('Ссылка на Интерфейс просмотра дат')

'''date_day = InlineKeyboardMarkup(row_width=7)
date_day.add(InlineKeyboardButton(text='Ponedelnik'))
date_time = InlineKeyboardMarkup()'''

contacts = InlineKeyboardMarkup(row_width=3)
contacts.add(InlineKeyboardButton(text='Admin', url='https://t.me/vlad_is_lovvve'),
            InlineKeyboardButton(text='Сайт', url='https://google.com'),
            InlineKeyboardButton(text='Инстагарм', url='https://www.instagram.com/'),
            InlineKeyboardButton(text='Телеграм канал', url='https://t.me/vlad_is_lovvve'))


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'Hello',
                         reply_markup=kb)
    await message.answer_sticker('CAACAgIAAxkBAANiZMWs_AIftFJRdkKg-ansP-gaX2MAArwXAAKpXxBKpt0jX0Tfm_IvBA')
    '''if message.from_user.id == int(os.getenv(('ADMIN_ID'))):
        await message.answer('Вы вошли как администратор', reply_markup=kb_adm)'''

@dp.message_handler(text='Записаться')
async def enroll(message: types.Message):
    await message.answer(f'Выберете дату')#, reply_markup=date_day)

@dp.message_handler(text='Контакты')
async def contacts_drop(message: types.Message):
    await message.answer(f'Телефон для справок 88005553535 проще позвонить, чем у кого-то занимать!', reply_markup=contacts)

@dp.message_handler(text='Свободные даты')
async def dates(message: types.Message):
    await message.answer(f'Свободных дат нет')

@dp.message_handler(text='Отзывы')
async def reaction(message: types.Message):
    await message.answer(f'Все ахуенно!!!')

@dp.message_handler(text='Справка')
async def reference(message: types.Message):
    await message.answer(f'Туда сюда и готово')

@dp.message_handler(text='Admin_Panel')
async def admpanel(message: types.Message):
    if message.from_user.id == int(os.getenv(('ADMIN_ID'))):
        await message.answer(f'Вы вошли в админ панель', reply_markup=admin_panel)
    else:
        await message.reply('К сожалению, данной команды нет в списке. Выберите из списка')
    
@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('К сожалению, данной команды нет в списке. Выберите из списка')



if __name__ == '__main__':
    executor.start_polling(dp)