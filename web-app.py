from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6032389111:AAFfr96IEwosRahP973zysGMf3Tu7GLjHWM')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://www.youtube.com/')))
    await message.answer('Привет, мой друг!', reply_markup=markup)

executor.start_polling(dp)