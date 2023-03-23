from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✮ 𝙰ᴅᴅ 𝙼ᴇ 𝚃ᴏ 𝚈ᴏᴜʀ 𝙶ʀᴏᴜᴘ ✮",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ 𝙷ᴇʟᴩ ✮",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✮ 𝚂ᴇᴛᴛɪɴɢ𝚂 ✮", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✮ 𝙰ᴅᴅ 𝙼ᴇ 𝚃ᴏ 𝚈ᴏᴜʀ 𝙶ʀᴏᴜᴘ ✮",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ 𝙷ᴇʟᴩ ✮", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✮ 𝚂ᴜᴩᴩᴏʀᴛ ✮", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="✮ 𝙾ᴡɴᴇʀ'𝚇𝙳  ✮", user_id=OWNER
            )
        ]
        
