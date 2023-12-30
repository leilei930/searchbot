import os

import telebot

BOT_TOKEN = "6796566165:AAGORuNxZMHyumHYHFzPGGp102mg5g0x3kM"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()