import telebot
from telebot import types
token = "2104780993:AAGQMZyRIYCwuUaS-p8FihQsmUn5SkGcIfM"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь мандарин?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/смотреть_на_мандари=", "/думать_о_смысле_жизни", "котики!")
    bot.send_message(message.chat.id, 'Я умею: \n'
                                      '/look_at_mandarin' '\n'
                                        '/think_about_life' '\n'
                                        'котики! - напиши, если любишь котиков')


@bot.message_handler(commands=['look_at_mandarin'])
def start_message(message):
    bot.send_message(message.chat.id, 'Мандаринки тут - https://pixabay.com/ru/photos/search/%D0%BC%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D0%B8%D0%BD/')

@bot.message_handler(commands=['think_about_life'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ищи свой смысл жизни здесь - https://pixabay.com/ru/images/search/%D0%B5%D0%B4%D0%B0/')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "котики!":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://pixabay.com/ru/images/search/%D0%BA%D0%BE%D1%88%D0%BA%D0%B0/')


if __name__ == '__main__':
    bot.infinity_polling()
