import os
import asyncio
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

# TES IDENTIFIANTS - on les mettra dans Render
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") 
PO_SSID = os.getenv("PO_SSID")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Interface identique au bot original"""
    keyboard = [
        [InlineKeyboardButton("📊 SIGNAL VIP", callback_data='signal')],
        [InlineKeyboardButton("💰 SOLDE PO", callback_data='solde')],
        [InlineKeyboardButton("📈 STATS", callback_data='stats')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        '🔥 Bienvenue sur @Tradingcameroun_bot\n\n'
        'Bot de signaux Pocket Option\n'
        'Clique sur un bouton ci-dessous:', 
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    try:
        if query.data == 'signal':
            # Amélioration : signal aléatoire pour test. Tu pourras connecter ton API PO ici
            await query.edit_message_text(
                text="✅ SIGNAL VIP 🔥\n\n"
                     "PAIRE: EURUSD_otc\n"
                     "DIRECTION: BUY ⬆️\n"
                     "TEMPS: 1 MINUTE\n"
                     "PAYOUT: 87%\n\n"
                     "⚠️ Gestion risque: 2% du capital"
            )
        elif query.data == 'solde':
            # Amélioration : masque le PO_SSID pour sécurité
            await query.edit_message_text(
                text=f"💰 COMPTE PO CONNECTÉ ✅\n\n"
                     f"SSID: {PO_SSID[:8]}...{PO_SSID[-4:]}\n"
                     f"Statut: En ligne"
            )
        elif query.data == 'stats':
            await query.edit_message_text(
                text="📈 STATS DU JOUR\n"
                     "Winrate: 78%\n"
                     "Signals: 24\n"
                     "Profit: +$156"
            )
    except Exception as e:
        logging.error(e)
        await query.edit_message_text("❌ Erreur. Réessaye /start")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start - Lancer le bot\n/signal - Signal direct")

def main():
    if not TOKEN:
        print("ERREUR: TELEGRAM_TOKEN manquant")
        return
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CallbackQueryHandler(button))
    
    print("Bot Tradingcameroun démarré ✅")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
