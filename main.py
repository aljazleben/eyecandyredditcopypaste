import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("7992625095:AAHAz8gXdvaRVMbDpaFANA_bjpnVelbKLPQ")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    lines = user_text.split("\n")

    # Wrap each non-empty line in triple backticks
    formatted = "\n".join([f"```\n{line}\n```" for line in lines if line.strip()])

    await update.message.reply_text(formatted, parse_mode=None)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()
