import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
POCKET_EMAIL = os.getenv("POCKET_EMAIL")
POCKET_PASSWORD = os.getenv("POCKET_PASSWORD")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut bro ✅ Le bot Trading Cameroun est en ligne!")

async def test_pocket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Email Pocket: {POCKET_EMAIL}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test_pocket))
    
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
