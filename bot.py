from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes
import os

TOKEN = os.getenv("8672468675:AAHGwLhoCo459SUvyWzPVPYfKCQ2mtZdPuQ")  # مهم

BAD_WORDS = ["bad", "fuck", "shit"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 ښه راغلاست! ګروپ خوندي دی 😎")

async def filter_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    # لینک بلاک
    if "http" in text or "t.me" in text:
        await update.message.delete()
        return

    # بد الفاظ بلاک
    for word in BAD_WORDS:
        if word in text:
            await update.message.delete()
            return

app = ApplicationBuilder().token(8672468675:AAHGwLhoCo459SUvyWzPVPYfKCQ2mtZdPuQ).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, filter_all))

app.run_polling()
