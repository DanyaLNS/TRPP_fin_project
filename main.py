import telebot
from gtts import gTTS
from info import *
from telebot import types

# Функция для преобразования текста в звуковой файл
def pdf_to_mp3(message):
    my_audio = gTTS(text=message, lang=language, slow=False)
    my_audio.save(f'result.mp3')

# Функция, отвечающая за работу бот
def telegram_bot(token):
    # Инициализация бота
    bot = telebot.TeleBot(token)
    # Обработка стартового сообщения
    @bot.message_handler(commands=["start"])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b_info = types.KeyboardButton("info")
        markup.add(b_info)
        bot.send_message(message.chat.id, "Здравствуй! \n"
                                          "Этот бот преобразовывает текстовые сообщения в звуковой файл! \n"
                                          "Просто напишите мне, что я должен озвучить и я сделаю это!",
                         reply_markup=markup)
    # Обработка пользовательских сообщений
    @bot.message_handler(content_types=["text"])
    def send_message(message):
        if (message.text in ['info', 'инфо']):
            bot.send_message(message.chat.id, "Я - бот, созданный студентами ИНБО-07-20! \n"
                                              "В нашу команду входят Аникин Данила, Куваков Темир и Глинко Алена...\n"
                                              "Они разработали телеграмм бота, который конвертирует текстовые сообщения в аудио! \n"
                                              "С его помощью вы сможете озвучивать статьи и слушать их в пути до ВУЗа или работы. \n")
        else:
            bot.send_message(message.chat.id, "Подождите, я озвучиваю!")
            pdf_to_mp3(message.text)
            bot.send_audio(message.chat.id, audio=open('result.mp3', 'rb'))
            bot.send_message(message.chat.id, "Готово!")
    # Активация бота
    bot.polling()

# Точка входа в программу
if __name__ == '__main__':
    telegram_bot(token)
