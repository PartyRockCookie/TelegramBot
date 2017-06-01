import os
import telebot

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def echo_message(message):
    bot.reply_to(message, u"Welcome to the bot")

@bot.message_handler(commands=['test'])
def test_message(message):
    bot.reply_to(message, "hi")


@bot.inline_handler(lambda query: query.query == 'text')
def temp(msg):
        bot.send_message(1,1)
bot.polling()

