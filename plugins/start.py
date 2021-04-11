# ( c ) Bruh_0x

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Client.on_message(filters.command(["start", "start@Pyro_Tg_Bot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>
Above File is sended by Pyro Tg Bot!

Made by **@Bruh_0x** for Noob/Beginners Like Him! (Me) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Updates Channel 🔰️", url="https://t.me/NexaBotsUpdates"
                    ),
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Nexa_bots"
                    )
                ]
            ]
        )
    )

    
@Client.on_message(filters.command(["sticker", "sticker@Pyro_Tg_Bot"]))
async def sticker(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>
Above File is sended by Pyro Tg Bot!

Made by **@Bruh_0x** for Noob/Beginners Like Him! (Me) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "About", callback_data="stick"
                    )
                ]
            ]
        )
    )
    
    
    
# callback shit

@Client.on_callback_query(filters.regex("stick"))
async def stick(_, query: CallbackQuery):
    await Message.send_sticker("CAACAgUAAxkBAAIEyGByiGplc4_5-OJ7eujZWlkZx7WoAAKRAQAC7thQV25-qe8JhyOhHgQ")
