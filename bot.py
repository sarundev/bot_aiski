import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your actual bot token from BotFather
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8913338474:AAHqrhqc0XIN5GS8NZ2YiamygMO6W9ZE2io')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Text imitating the format of the image provided, using aisakikh.com details
    text = (
        "<b>Templates: 🚛 Car Transport Orders Across Europe</b>\n\n"
        "📍 Daily transport requests\n\n"
        "https://www.transportinghighway.com/"
    )
    
    # Creating inline keyboard buttons similar to the image
    markup = InlineKeyboardMarkup(row_width=2)
    btn_website = InlineKeyboardButton("✨ Visit Channel", url="https://t.me/TRANSPORTINGT")
    btn_services = InlineKeyboardButton("📊 View Orders", url="https://t.me/TRANSPORTINGT")
    markup.add(btn_website, btn_services)
    
    # Send the message with HTML formatting and the inline keyboard
    bot.send_message(
        message.chat.id, 
        text, 
        parse_mode="HTML", 
        reply_markup=markup
    )

if __name__ == '__main__':
    print("transport Telegram bot is starting...")
    bot.infinity_polling()
