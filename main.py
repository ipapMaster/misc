import telebot
import config
from telebot import types  # для указания типов

# /start

name = ''
surname = ''
age = 0

# инициировали бота
bot = telebot.TeleBot(config.bot_token)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id,
                         "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id,
                         'Я Вас не понял, напишите /start')


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id,
                     'Как твоя фамилия имя?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,
                     'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:  # удостоверимся, что поменялся возраст
        try:
            age = int(message.text)
        except ValueError:
            bot.send_message(message.from_user.id,
                             'Вводите цифры')
            age = 1
            break
    question = f'Тебе {age} лет, и ты {name} {surname}?'
    keyboard = types.InlineKeyboardMarkup()  # клавиатура
    yes = types.InlineKeyboardButton(text='Да',
                                     callback_data='yes')
    keyboard.add(yes)
    no = types.InlineKeyboardButton(text='Нет',
                                    callback_data='no')
    keyboard.add(no)
    bot.send_message(message.from_user.id, text=question,
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global age
    """
    call.data - это callback_data, которую
    мы указали при объявлении кнопки
    """
    if call.data == "yes":
        # тут либо сохраняем, либо обрабатываем данные
        bot.send_message(call.message.chat.id,
                         'Приятно познакомиться')
    elif call.data == "no":
        # инициируем диалог повторно
        age = 0
        bot.send_message(call.message.chat.id,
                         'Тогда начнём сначала... Как тебя зовут?')
        bot.register_next_step_handler(call.message, get_name)


# запустили бота
bot.polling(none_stop=True)
