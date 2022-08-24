import telebot as tb
import config
import coordinates

bot = tb.TeleBot(config.BOT_API_TOKEN)
answer=coordinates.get_all_data()
@bot.message_handler(commands=['start'])
def start_messages(message):
    bot.send_message(message.from_user.id, answer)
    markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = tb.types.KeyboardButton('Show info')
    markup.add(btn1)
    print('OK')

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Show info"):
        bot.send_message(message.chat.id, text=answer)

bot.polling()