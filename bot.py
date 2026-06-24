import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your actual bot token from BotFather
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8894742602:AAHxlsyD5z9N0yfGnAUk7FqwF74XKK-0BbA')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Text imitating the format of the image provided, using aisakikh.com details
    text = (
        "<b>Templates: 🚀 Aisaki Digital Services</b>\n\n"
        "📍 Facebook Ads, TikTok growth, and online business promotion\n\n"
        "https://www.aisakikh.com"
    )
    
    # Creating inline keyboard buttons similar to the image
    markup = InlineKeyboardMarkup(row_width=2)
    btn_website = InlineKeyboardButton("✨ Visit Website", url="https://www.aisakikh.com")
    btn_services = InlineKeyboardButton("📊 View Orders", url="https://www.aisakikh.com/Service")
    markup.add(btn_website, btn_services)
    
    # Send the message with HTML formatting and the inline keyboard
    bot.send_message(
        message.chat.id, 
        text, 
        parse_mode="HTML", 
        reply_markup=markup
    )

if __name__ == '__main__':
    print("Aisaki Digital Telegram bot is starting...")
    bot.infinity_polling()
