import telebot
from telebot import types

token = '8114888369:AAERfr2-rxNnPcfnqHUDfABqCLdrly25L9s'
bot = telebot.TeleBot(token)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    # Создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Привет! Вот медddddведь 🐻 и роза 🌹", reply_markup=markup)


# Обработчик команды /button (если нужно)
@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Кнопка":
        bot.send_message(message.chat.id, "https://habr.com/ru/users/lubaznatel/")


# Запуск бота
bot.infinity_polling()