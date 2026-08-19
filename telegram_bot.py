# -*- coding: utf-8 -*-
"""
Bot de Telegram para el tablero "Río San Francisco".
Envía un botón que abre el tablero DENTRO de Telegram (Web App).

REQUISITOS ANTES DE CORRERLO:
1. El tablero (tablero_rio_san_francisco.html + manifest.webmanifest + icons/)
   debe estar publicado en una URL con https:// (Netlify, GitHub Pages, etc).
   Telegram NO permite Web Apps en http:// ni en file://.
2. Crea el bot con @BotFather en Telegram:
     - Envía /newbot y sigue las instrucciones.
     - Copia el "token" que te da (algo como 123456:ABC-...).
3. Instala la librería:
     pip install python-telegram-bot --upgrade

CÓMO CORRERLO:
     python telegram_bot.py

Deja esta terminal/proceso corriendo (o súbelo a un servidor / Render / Railway /
PythonAnywhere) para que el bot responda todo el tiempo.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ---------- CONFIGURA ESTOS DOS VALORES ----------
BOT_TOKEN = "PON_AQUI_EL_TOKEN_DE_BOTFATHER"
DASHBOARD_URL = "https://tu-sitio.netlify.app/tablero_rio_san_francisco.html"
# --------------------------------------------------


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "📊 Abrir tablero del río",
            web_app=WebAppInfo(url=DASHBOARD_URL)
        )]
    ])
    await update.message.reply_text(
        "Monitoreo en vivo del Río San Francisco (Panajachel, Sololá).\n"
        "Toca el botón para abrir el tablero:",
        reply_markup=keyboard
    )


async def rio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Mismo botón, disponible también con /rio
    await start(update, context)


def main():
    if "PON_AQUI" in BOT_TOKEN or "tu-sitio" in DASHBOARD_URL:
        print("⚠️  Antes de correr el bot, edita BOT_TOKEN y DASHBOARD_URL arriba en este archivo.")
        return
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rio", rio))
    print("Bot corriendo. Presiona Ctrl+C para detenerlo.")
    app.run_polling()


if __name__ == "__main__":
    main()
