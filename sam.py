#👀

import pyrogram
import asyncio
import random

from asyncio import sleep as slp
from pyrogram import Client, filters
from pyrogram.types import User, Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from info import API_ID
from info import API_HASH
from info import BOT_TOKEN
from info import ADMINS
from info import TIME
from info import BOT_USERNAME

#=======================================================================

START_MSG = '<b>Hai {},\nIam A Simple Telegram Bot To Delete Group Messages In Specific Time</b>'

START_IMG = ["https://telegra.ph/file/abed06af605d2cebc8dc3.jpg",
             "https://telegra.ph/file/c73194c9b504990733cd8.jpg"]
HELP_MSG = "<b>Add Me To Your Group And Promote Me As Admin</b> \n \n<code>⚠️ I Can't Delete Messages Of Other Bots ⚠️</code>"      

#=======================================================================

Sam = Client(
    session_name="Auto-Delete",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

#=======================================================================

@Sam.on_message(filters.command(['start']) & filters.private)
def start(client, cmd):
         buttons = [
                      [
                         InlineKeyboardButton('❤️', callback_data="A"),
                         InlineKeyboardButton('🌹', callback_data="B"),
                         InlineKeyboardButton('✨', callback_data="C"),
                         InlineKeyboardButton('💖', callback_data="D")
                      ],
                      [
                         InlineKeyboardButton('Help', callback_data="help"),
                      ]
                   ]
         cmd.reply_photo(photo=random.choice(START_IMG), caption=START_MSG.format(cmd.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons))
               

@Sam.on_message(filters.group & filters.all)
async def deleter(bot: Client, cmd: Message):
         if cmd.from_user.id not in ADMINS:
                  await slp(int(TIME))
                  await cmd.delete()

#==CALLBACK=====================================================================

@Sam.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):
                  if query.data == "help":
                           helpbtn = [
                                         [
                                           InlineKeyboardButton('❤️', callback_data="E"),
                                           InlineKeyboardButton('🌹', callback_data="F"),
                                           InlineKeyboardButton('✨', callback_data="G"),
                                           InlineKeyboardButton('💖', callback_data="H")
                                         ],
                                         [
                                           InlineKeyboardButton("➕ Add To Your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                                         ],
                                         [
                                            InlineKeyboardButton('❌ Close', callback_data="close"),
                                            InlineKeyboardButton('📜 Source Code', url='https://github.com/Arun-TG/AutoDelete/tree/Bot-Only')
                                         ]
                                     ]
                           await query.message.edit(text=HELP_MSG, reply_markup=InlineKeyboardMarkup(helpbtn))
                  
                  elif query.data.startswith("close"):
                           await query.message.delete()
#=======================================================================

Sam.run()
print("Bot Started!")

#=======================================================================
