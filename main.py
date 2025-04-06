import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Grab the bot token from Render environment variable
TOKEN = os.getenv("BOT_TOKEN")

# Define the message handler function
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    lines = user_text.split("\n")

    # Wrap each line in triple backticks (inline) for copy-paste formatting
    formatted = "\n\n".join([f"```{line}```" for line in lines if line.strip()])

    await update.message.reply_text(formatted, parse_mode=None)

# Build and run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.run_polling()
