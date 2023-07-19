# pip install python-telegram-bot[ext] --upgrade
import logging  # фиксация действий
import config
from telegram.ext import Application, MessageHandler, filters

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


def main():
    application = Application.builder().token(config.bot_token).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
