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
