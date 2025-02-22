import asyncio
import json
import requests
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes

# Your bot token from BotFather
TELEGRAM_BOT_TOKEN = "  "
# File to store subscriber chat IDs
CHAT_IDS_FILE = "chat_ids.json"

# Load chat IDs from file, or start with an empty list
def load_chat_ids():
    try:
        with open(CHAT_IDS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save chat IDs back to file
def save_chat_ids(chat_ids):
    with open(CHAT_IDS_FILE, "w") as f:
        json.dump(chat_ids, f)

# Global list of subscribers
chat_ids = load_chat_ids()

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id not in chat_ids:
        chat_ids.append(chat_id)
        save_chat_ids(chat_ids)
        await update.message.reply_text("✅ You have been subscribed to crypto price updates!")
    else:
        await update.message.reply_text("ℹ️ You are already subscribed.")

# Function to get the crypto price (using CoinGecko API)
def get_crypto_price(crypto="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data[crypto]["usd"]
    return price

# Async function to send price updates to all subscribers
async def send_price_update():
    price = get_crypto_price("bitcoin")
    message = f"🔥 Bitcoin Price Update: ${price}"
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    for cid in chat_ids:
        try:
            await bot.send_message(chat_id=cid, text=message)
        except Exception as e:
            print(f"Failed to send message to {cid}: {e}")
    print("Price update sent to all subscribers.")

# Async function that runs in an infinite loop, sending updates every minute
async def periodic_updates():
    while True:
        await send_price_update()
        await asyncio.sleep(60)  # Wait 60 seconds before the next update

# ------------------------
# Main Execution
# ------------------------
if __name__ == "__main__":
    import sys
    # For macOS compatibility: use the default event loop policy
    if sys.platform == "darwin":
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    
    # Build the Telegram Application
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # Get the current event loop and schedule periodic updates in the background
    loop = asyncio.get_event_loop()
    loop.create_task(periodic_updates())
    
    print("Bot is running... Use /start to subscribe for updates.")
    # run_polling() is a blocking call that starts the bot
    app.run_polling()
