# Домашняя работа от 25 ноября 2022 года (10 семинар)
# Прикрутить телеграм бота к задаче по сложению многочленов.

from sympy import Symbol, collect
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from datetime import datetime
import random

counter = {}
summand1 = ''
summand2 = ''
stickers = [
    'CAACAgIAAxkBAAEGmIFjhQ3FQS4rix0sPqpyG4_WWnuOcQACkRIAAvzw4UodOfjG8l2MsysE',
    'CAACAgIAAxkBAAEGmINjhQ4BN7T5cMZ2MQ3TS09E-es9QAACLhcAAhVHQUi-H5Qdq8jupCsE',
    'CAACAgIAAxkBAAEGmIVjhQ4rHcHQ5gzxnNlAqDQcb_xodgACOQADrWW8FHR8_JWrMmzqKwQ',
    'CAACAgIAAxkBAAEGmItjhQ7grnAIgMIlqHlGArTDWOvdEAACOgADUomRI8sVLObWKjS6KwQ',
    'CAACAgIAAxkBAAEGmI1jhQ7-LYxeHkgQhsCY8iVt7kfBYgACQQADUomRI9XWV0rTZHFWKwQ',
    'CAACAgIAAxkBAAEGmI9jhQ9DidID6VRRpE-UHeEC7GaGdQACEhEAAj9w8Uo66W_N-9GmTysE',
    'CAACAgIAAxkBAAEGmJFjhQ9esHyFpoF9FTiBye1NAAHpoBwAAiYUAAJTjPFK5VLETk23h-crBA',
    'CAACAgEAAxkBAAEGmJNjhQ-VdwLF_MTImI4hFfx-RxT8fwAC6wEAAjgOghGzhgTO4ZxJOSsE',
    'CAACAgEAAxkBAAEGmJVjhQ-1mnCedFirsYJG8qZGYJlfGwAC6AEAAjgOghGslKjQTMGLCCsE',
    'CAACAgEAAxkBAAEGmJdjhQ_IKfSuWZm0vWMgXw-V1xYcFAACLgEAAmlAwUU75COP0TwvfCsE'
]


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('log.csv', 'a', encoding='UTF-8')
    file.write('{0:>15}, {1:<12}, {2:>30}, {3:>22}\n'.format(
        str(update.effective_user.first_name), str(update.effective_user.id),
        str(update.message.text),
        datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    file.close()


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    global counter, summand1, summand2
    log(update, context)
    counter[update.message.from_user.id] = counter.get(update.message.from_user.id, 0) + 1

    if counter[update.message.from_user.id] < 2:
        await update.message.reply_text(
            f'''Привет {update.effective_user.first_name}!!! Я телеграмм-бот 
            \n Я помогу вычислить сумму многочленов 
            \n отправляй первый многочлен 
            \n например: 5*x**6 + 4*x**3 + 2*x**2 +6 
            \n или x**2 + 3*x - 12''')
    elif counter[update.message.from_user.id] == 2:
        summand1 = update.message.text
        await update.message.reply_text(
            f'''Снова привет, {update.effective_user.first_name}! 
             \n Теперь отправляй второй многочлен''')
    elif counter[update.message.from_user.id] == 3:
        summand2 = update.message.text
        x = Symbol('x')
        stick = random.choice(stickers)
        try:
            result = str(collect(summand1 + ' + ' + summand2, x))
            result = f'''{summand1} + {summand2} = 
                     \n = {result}'''
        except TypeError:
            result = f'Ошибка... Вы ввели недопустимый символ'
            stick = 'CAACAgEAAxkBAAEGmMFjhRMVkMBIYZw487QGIrEROQ2EhQAC8gEAAjgOghFkeRhU3RO6BisE'
        except ValueError:
            result = f'Ошибка... Вы ввели недопустимое выражение'
            stick = 'CAACAgEAAxkBAAEGmMNjhRMtWGP4vl07cjZXQl5UmObj5gAC-QEAAjgOghHcO4dxtT-qtisE'
        finally:
            await update.message.reply_sticker(stick)
            await update.message.reply_text(result)
            counter[update.message.from_user.id] = 1
            await update.message.reply_text(
                f'''{update.effective_user.first_name}, 
                   \n жду первый многочлен''')


app = ApplicationBuilder().token("---ЗДЕСЬ-БУДЕТ-ТОКЕН---").build()

app.add_handler(MessageHandler(filters.TEXT, text))

print('Telegram bot запущен...')
app.run_polling()