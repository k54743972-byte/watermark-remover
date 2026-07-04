import os
import threading
import logging
from flask import Flask, jsonify
from bot.main import create_application
from bot.utils import setup_logging
from dotenv import load_dotenv

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health_check():
    return jsonify({"status": "ok", "message": "Bot is running"}), 200

def run_bot():
    try:
        logger.info("Starting Telegram Bot...")
        application = create_application()
        application.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    port = int(os.getenv("PORT", 8080))
    logger.info(f"Starting health check server on port {port}...")
    app.run(host='0.0.0.0', port=port)
