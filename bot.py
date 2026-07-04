import os
import threading
import logging
from flask import Flask, jsonify
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.handlers import start, handle_image, error_handler
from bot.utils import setup_logging
from dotenv import load_dotenv

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

def run_bot():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not found!")
        return
        
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))
    application.add_error_handler(error_handler)
    
    logger.info("Starting Telegram bot...")
    application.run_polling()

if __name__ == "__main__":
    # Start bot thread
    threading.Thread(target=run_bot, daemon=True).start()
    
    # Start Flask
    port = int(os.getenv("PORT", 8080))
    logger.info(f"Starting health check server on port {port}...")
    app.run(host="0.0.0.0", port=port)
