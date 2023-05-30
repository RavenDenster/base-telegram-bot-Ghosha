import telebot
import requests
import json

bot = telebot.TeleBot('6032389111:AAFfr96IEwosRahP973zysGMf3Tu7GLjHWM')
API = '421f1b3e3786d0bc08ed4387d2bccf2f'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погда: {temp}')

        image = 'weather-1.jpg' if temp > 5.0 else 'weather-2.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан не верно')


bot.polling(none_stop=True)
