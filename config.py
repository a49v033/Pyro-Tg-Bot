# ( c ) Bruh_0x
# Those this are configs which needs to run bot! (Me Noob)
# without "import os" bot can't get those values from Heroku Configs! (Me Noob)

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
