import os

from pyrogram import Client as Bot

from config import API_ID, API_HASH, BOT_TOKEN, DOWNLOAD_LOCATION

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

print("Pyro-Tg-Bot Started Successfully")

bot.run()
