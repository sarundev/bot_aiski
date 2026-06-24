import os
import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your marketing copy
WELCOME_TEXT = (
    "🚗 *Car transport companies across Europe — this is for you.*\n\n"
    "Transporting Highway gives you direct access to vehicle transport orders throughout Europe.\n\n"
    "✅ *More loads, less empty runs*\n"
    "✅ *Direct orders — no middlemen*\n"
    "✅ *Fast & reliable payments*\n"
    "✅ *Simple platform, easy to use*\n\n"
    "Join hundreds of transport companies already moving cars with us.\n\n"
    "📩 *Here is your file! Register now and start receiving orders:*"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    # 1. Send the promotional message
    await context.bot.send_message(
        chat_id=chat_id, 
        text=WELCOME_TEXT, 
        parse_mode="Markdown"
    )
    
    # 2. Automatically send the document/file
    # Ensure your file (e.g., registration_guide.pdf) is in the same folder as this script
    file_path = "registration_guide.pdf" 
    
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            await context.bot.send_document(
                chat_id=chat_id, 
                document=file, 
                caption="📄 Transporting Highway - Registration Guide & Info"
            )
    else:
        logging.error(f"File {file_path} not found.")

async def main():
    # Token retrieved safely from Render environment variables
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        print("Error: No TELEGRAM_BOT_TOKEN found in environment variables.")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot is initializing and running...")
    
    # Using the native asynchronous manager blocks to handle initialization, polling, and finalization safely on Python 3.14+
    async with application:
        await application.initialize()
        await application.start()
        await application.updater.start_polling()
        
        # Keeps the bot running indefinitely
        while True:
            await asyncio.sleep(3600)

if __name__ == "__main__":
    # Explicitly creating and running the async loop solves the Python 3.14 background thread error
    asyncio.run(main())