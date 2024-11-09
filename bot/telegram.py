import telebot
from telebot import types

API_KEY = "Telegram API Key"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_gif(message):
    gif_url = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjRpYzExdDhxMnR1ZnoxODcxeDI5d3I2OXVucTAwYXF0dGpoZWFuOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7WvAUvZZTRpSuudobh/giphy.gif"
    
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="🚀 Start 🚀", url="https://t.me/lineabuild_bot/linea")
    join_channel_button = types.InlineKeyboardButton(text="Join Community", url="https://x.com/LineaBuild")
    
    keyboard.add(url_button)
    keyboard.add(join_channel_button)

    bot.send_animation(chat_id=message.chat.id, animation=gif_url, reply_markup=keyboard)

bot.infinity_polling()