from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
# 🔗 Ambil logika chatbot dari core.py
from core import get_bot_reply

# 🔑 Ganti dengan TOKEN dari BotFather
TOKEN = "8503613463:AAGQmkLojvBlYvCdwafqkF9zL4apDMIawFU"


# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋\n"
        "Saya bot ulya printing.\n\n"
        "Silakan tanya seputar:\n"
        "- Jam operasional\n"
        "- Lokasi belajar\n"
      
    )


# Menangani semua pesan teks
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    jawaban = get_bot_reply(user_text)  # 🔥 HUBUNG KE core.py
    await update.message.reply_text(jawaban)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Bot Telegram ulya printing...")
    app.run_polling()


if __name__ == "__main__":
    main()