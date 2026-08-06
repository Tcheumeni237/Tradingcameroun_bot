import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
POCKET_EMAIL = os.getenv("POCKET_EMAIL")
POCKET_PASSWORD = os.getenv("POCKET_PASSWORD")

# Sécurité : crash direct si token manquant
if not TOKEN:
    raise ValueError("ERREUR: TELEGRAM_TOKEN manquant dans Environment sur Render!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut bro ✅ Le bot Trading Cameroun est en ligne!")

async def test_pocket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if POCKET_EMAIL:
        await update.message.reply_text(f"Email Pocket: {POCKET_EMAIL}")
    else:
        await update.message.reply_text("POCKET_EMAIL pas défini dans Environment")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test_pocket))
    
    print("Bot started...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
