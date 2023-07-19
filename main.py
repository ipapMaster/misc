import telebot
import config
from telebot import types  # для указания типов
# /start

# инициировали бота
bot = telebot.TeleBot(config.bot_token)
@bot.message_handler(commands=['start']) # реагируем на /start
def start(message):
    markup = types.InlineKeyboardMarkup()
    but = types.InlineKeyboardButton('Google',
                                     url='https://google.com')
    markup.add(but)
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}! Нажми на кнопку)'.format(message.from_user),
                     reply_markup=markup)

# запустили бота
bot.polling(none_stop=True)
