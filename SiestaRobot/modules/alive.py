import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/10deb009aa778c8be099a.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Yo!! [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Akame.** \n\n"
  TEXT += "♡ **I'm Working Properly Baka!!** \n\n"
  TEXT += f"♡ **My Darling : [Devoid Namikaze](https://t.me/DEVOID_10)** \n\n"
  TEXT += f"♡ **Library Version :** `{telever}` \n\n"
  TEXT += f"♡ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"♡ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ♡**"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/ShikimoriXupdates"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/JinWooXsupport"), 
                       Button.url("ᴍʏ ᴅᴀʀʟɪɴɢ", "https://t.me/Itz_Light_Yagami")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
