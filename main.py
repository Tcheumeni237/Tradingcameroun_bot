import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from pocketoptionapi import PocketOptionAPI # Ligne pour Pocket

# 1. Récupère les variables de Render
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
POCKET_EMAIL = os.environ.get("POCKET_EMAIL")
POCKET_PASSWORD = os.environ.get("POCKET_PASSWORD")

# 2. Connexion Pocket Option
api = PocketOptionAPI()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /start"""
    keyboard = [
        [InlineKeyboardButton("📊 Obtenir Signal", callback_data='signal')],
        [InlineKeyboardButton("💰 Balance", callback_data='balance')],
        [InlineKeyboardButton("🔌 Connecter Pocket", callback_data='connect')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        '🤖 BIENVENUE SUR MATRIX TOOL\nChoisis une option :', 
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gère les boutons"""
    query = update.callback_query
    await query.answer()

    if query.data == 'connect':
        await query.edit_message_text("Connexion à Pocket Option...")
        check, reason = await asyncio.to_thread(api.connect, POCKET_EMAIL, POCKET_PASSWORD)
        if check:
            await query.edit_message_text("✅ Connecté à Pocket Option avec succès !")
        else:
            await query.edit_message_text(f"❌ Erreur connexion: {reason}")

    elif query.data == 'balance':
        balance = await asyncio.to_thread(api.get_balance)
        await query.edit_message_text(f"💰 Balance: {balance}$")

    elif query.data == 'signal':
        await query.edit
