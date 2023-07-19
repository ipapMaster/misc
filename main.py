# pip install python-telegram-bot[ext] --upgrade
import logging  # фиксация действий
import config
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler

# Запустим логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

"""
Функция обработки сообщений
update - принимает
context - доп. информация о сообщении 
"""


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def start(update, context):
    """
    Реакция на команду /start
    """
    user = update.effective_user
    await update.message.reply_html(
        rf'Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-то.'
    )


async def help_command(update, context):
    await update.message.reply_text('Я пока не сильный помощник')


def main():
    application = Application.builder().token(config.bot_token).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.run_polling()


if __name__ == '__main__':
    main()
