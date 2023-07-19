# pip install python-telegram-bot[ext] --upgrade
import logging  # фиксация действий
import config
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

# Запустим логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

reply_buttons = [
    ['/address', '/site'],
    ['/help', '/start']
]

TIMER = 5

markup = ReplyKeyboardMarkup(reply_buttons, one_time_keyboard=False)


def remove_job(name, context):
    current_job = context.job_queue.get_jobs_by_name(name)
    if not current_job:
        return False
    for job in current_job:
        job.schedule_removal()
    return True


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
        rf'Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-то.',
        reply_markup=markup
    )


async def set_timer(update, context):
    chat_id = update.effective_message.chat_id
    job_removed = remove_job(str(chat_id), context)
    context.job_queue.run_once(task, TIMER,
                               chat_id=chat_id,
                               name=str(chat_id),
                               data=TIMER)
    text = f'Буду через {TIMER} сек!'
    if job_removed:
        text += ' Старая задача удалена.'
    await update.effective_message.reply_text(text)


async def task(context):
    await context.bot.send_message(context.job.chat_id,
                                   text=f'Вот и прошли {TIMER} сек.')


async def help_command(update, context):
    await update.message.reply_text('Я простой справочник')


async def unset(update, context):
    chat_id = update.message.chat_id
    job_removed = remove_job(str(chat_id), context)
    text = 'Таймер отменён' if job_removed else 'Таймеры не были установлены'
    await update.message.reply_text(text)


async def address(update, context):
    await update.message.reply_text('Адрес ИПАП: СПб, Можайская, 2')


async def site(update, context):
    await update.message.reply_text('https://google.com')


async def close_keyboard(update, context):
    await update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())


def main():
    application = Application.builder().token(config.bot_token).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('address', address))
    application.add_handler(CommandHandler('site', site))
    application.add_handler(CommandHandler('close', close_keyboard))
    application.add_handler(CommandHandler('set', set_timer))
    application.add_handler(CommandHandler('unset', unset))
    application.run_polling()


if __name__ == '__main__':
    main()
