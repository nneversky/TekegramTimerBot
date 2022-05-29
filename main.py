import telebot
import timer
import config
from telebot import types

bot = telebot.TeleBot(config.telebotApi)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Hello, this bot is designed to auto-post your messages in telegram channels, use the command /autoposting')


@bot.message_handler(commands=['autoposting'])
def autopost(message):
    kb = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text='Autoposting', callback_data='auto')
    kb.add(btn_1)
    bot.send_message(message.chat.id, 'Hello use autoposting', reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data == 'auto')
def check_callback(callback):
    a_1 = bot.send_message(callback.message.chat.id, 'Please enter time for use autoposting, for example: 14:37')
    bot.register_next_step_handler(a_1, choice_time)


def choice_time(message):
    global a_2
    a_2 = message.text
    a_1 = bot.send_message(message.chat.id, 'Please enter your message')
    bot.register_next_step_handler(a_1, choice)


@bot.message_handler(content_types=['text', 'photo', 'video', 'sticker'])
def choice(message):
    bot.reply_to(message, f'Thanks, your message will be sent in telegram channel {config.telebotLink[1:]} to {a_2}')
    a_3 = timer.timer_1(list(a_2))
    if a_3 == True:
        bot.copy_message(chat_id=config.telebotLink, from_chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, 'Your message has been delivered')


bot.infinity_polling()
