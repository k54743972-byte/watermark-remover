# AI Watermark Remover Telegram Bot

A professional, business-ready Telegram bot built with Python that removes watermarks from images using AI APIs.

## Features
- **AI-Powered**: Uses industry-leading APIs (ClipDrop / WatermarkRemover.io).
- **Robust Error Handling**: Every function is wrapped with error handling.
- **Auto-Retry**: Implements exponential backoff retries for API timeouts.
- **Health Check**: Flask server for monitoring (Render free tier compatible).
- **Logging**: Comprehensive logging for debugging.
- **Environment Driven**: Fully configurable via environment variables.

## Tech Stack
- **Language**: Python 3.12
- **Framework**: `python-telegram-bot` v21
- **Web Server**: Flask
- **APIs**: ClipDrop or WatermarkRemover.io

## Project Structure
```text
telegram-watermark-bot/
├── bot/
│   ├── api_client.py   # API integration logic
│   ├── handlers.py     # Telegram message handlers
│   ├── main.py         # Bot initialization
│   └── utils.py        # Logging and helpers
├── app.py              # Entry point (Flask + Bot)
├── requirements.txt    # Dependencies
├── Procfile            # Deployment config
└── .env.example        # Environment template
```

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example`.
4. Run: `python app.py`

## Deployment on Render
1. Create a **Web Service** on Render.
2. Set Environment Variables: `TELEGRAM_BOT_TOKEN`, `CLIPDROP_API_KEY`, etc.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `python app.py`
