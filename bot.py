import telebot

# Ваш токен бота
TOKEN = '7493472977:AAGeK-hlJUPhUBpFlSFdO0e0FI1uu-rL5x8'

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я готов к работе. Попробуйте отправить мне сообщение.")

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)  # Простое эхо

# Запуск бота
bot.polling()
