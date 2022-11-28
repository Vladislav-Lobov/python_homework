# Домашняя работа от 22 ноября 2022 года (семинар №9)

# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в него систему логирования

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('log.csv', 'a', encoding='UTF-8')
    file.write('{0:>20}, {1:<12}, {2:>30}, {3:>22}\n'.format(
        str(update.effective_user.first_name), str(update.effective_user.id),
        str(update.message.text),
        datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    file.close()


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(
        f'''Привет {update.effective_user.first_name}!!! Я телеграм-бот 
                                     \n Я помогу тебе вычислить математическое выражение. 
                                     \n Начни с команды: /calculate <выражение>
                                     \n Используй скобки для очередности вычисления
                                     \n Используй символ j для мнимой части комплексного числа
                                     \n Примеры: 78 - 4 / (2 + 2) или 56 * (2 - 11j) / 30'''
    )


async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    msg = msg.replace('/calculate', '')
    try:
        result = eval(msg)
    except ZeroDivisionError:
        result = 'Ошибка: деление на ноль'
    except SyntaxError:
        result = 'Ошибка: вы ввели неверный символ'
    await update.message.reply_text(f'----> {result}')


app = ApplicationBuilder().token("--ЗДЕСЬ_БУДЕТ_ТОКЕН--").build()

app.add_handler(CommandHandler("calculate", calculate))
app.add_handler(MessageHandler(filters.TEXT, text))

print('Telegram bot запущен...')
app.run_polling()