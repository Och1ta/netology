import telebot

token = '5531471818:AAHAm0Kw8Eiy0CzN9kf29S89bhfPAX9DhbA'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
