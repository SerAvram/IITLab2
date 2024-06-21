from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Определите обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш бот. Как я могу помочь вам сегодня?')

# Определите обработчик сообщений
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Определите функцию main
def main() -> None:
    # Вставьте сюда ваш токен
    token = '7493472977:AAGeK-hlJUPhUBpFlSFdO0e0FI1uu-rL5x8'

    # Создайте Updater и передайте ему токен вашего бота
    updater = Updater(token, use_context=True)

    # Получите диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Зарегистрируйте обработчики
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запустите бота
    updater.start_polling()

    # Запускайте бота до тех пор, пока вы не нажмете Ctrl-C или процесс не будет завершен
    updater.idle()

if name == 'main':
    main()
