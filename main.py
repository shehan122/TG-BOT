import os
import telebot


bot = telebot.TeleBot("2144954458:AAH_pYT1L4axyj-KiKfuicJ3C6ftfRo4abo")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Senura Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()
