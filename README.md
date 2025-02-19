Live Crypto Price Bot 🚀
This Telegram bot sends real-time Bitcoin price updates every minute using the CoinGecko API. It allows multiple users to subscribe by sending /start and runs efficiently in the background with async execution.

Features
✅ Fetches live Bitcoin prices from CoinGecko
✅ Supports multiple users – subscribe via /start
✅ Runs asynchronously to handle multiple requests efficiently
✅ Stores subscribed users in chat_ids.json

Installation & Setup

1️⃣ Clone the Repository
Clone the repository using:
git clone https://github.com/web3saad/Live-Crypto-Price.git
cd Live-Crypto-Price

2️⃣ Create & Activate Virtual Environment
For macOS/Linux:
python3 -m venv myenv
source myenv/bin/activate

For Windows:
python -m venv myenv
myenv\Scripts\activate

3️⃣ Install Dependencies
Install the required packages:
pip install python-telegram-bot requests

4️⃣ Set Up Telegram Bot
Go to BotFather on Telegram
Create a bot using /newbot and copy your Bot Token
Replace TELEGRAM_BOT_TOKEN in crypto_bot.py with your token

5️⃣ Run the Bot
Run the bot using:
python3 crypto_bot.py

6️⃣ Subscribe for Updates
Open your bot on Telegram
Send /start to receive live Bitcoin price updates every minute
Contributing
Feel free to fork this repo, improve the bot, and submit a pull request! 💡

License
📝 MIT License – Use it freely! 🚀
