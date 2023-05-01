""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2022 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want
"""

from env import LOG_ID
import asyncio
from pyrogram import Client, filters
from data import AlexaData
from TeamAlexa.database.AlexaDB import add_telegraph_user
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    if query.data == "ABOUT_CMD":
        await query.message.edit(
            text=AlexaData.ABOUT_STRING,
            reply_markup=InlineKeyboardMarkup(AlexaData.HELP_BACK),
        )
    elif query.data == "CMDS_CMD":
        await query.message.edit(
            text=AlexaData.CMDS_STRING,
            reply_markup=InlineKeyboardMarkup(AlexaData.HELP_BACK),
        )
    elif query.data == "TEAM_CMD":
        await query.message.edit(
            text=AlexaData.TEAM_STRING,
            reply_markup=InlineKeyboardMarkup(AlexaData.HELP_BACK),
            disable_web_page_preview=True
        )
    elif query.data == "HELP_BACK":
        await query.message.edit(
            text=AlexaData.HELP_STRING,
            reply_markup=InlineKeyboardMarkup(AlexaData.H_BUTTON),
        )


@Client.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await add_telegraph_user(message.from_user.id)
    alexamusic = await message.reply("🤭🤏✌️")
    await asyncio.sleep(2)
    await alexamusic.edit("**sᴛᴀʀᴛɪɴɢ ʙᴏᴛ**")
    await asyncio.sleep(2)
    await alexamusic.edit("**ɪ ᴀᴍ ᴅᴏɪɴɢ ᴍʏ ʟᴏᴠᴇ 💕**")
    await asyncio.sleep(2)    
    await alexamusic.delete()
    umm = await message.reply_sticker("CAACAgIAAxkBAAEForNjAykaq_efq4Wd-9KZv-nNxJRn3AACIgMAAm2wQgO8x8PfoXC1eCkE")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7d7df33268ac53f8480fe.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ᴛᴇᴀᴍ ᴀʟᴇxᴀ ᴘʀᴏᴊᴇᴄᴛ ғᴏʀ ᴜᴘʟᴏᴀᴅɪɴɢ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴀsᴀᴅ ᴀʟɪ](https://t.me/Dr_Asad_Ali)
┣★ ᴜᴘᴅᴀᴛᴇs : [ᴀʟᴇxᴀ ʙᴏᴛ](https://t.me/Alexa_BotUpdates)
┣★ sᴜᴘᴘᴏʀᴛ : [ᴀʟᴇxᴀ sᴜᴘᴘᴏʀᴛ](https://t.me/Alexa_Help)
┣★ ʀᴜɴ ➛  : /help ᴛᴏ sᴇᴇ ʜᴇʟᴘ ᴍᴇɴᴜ
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/Dr_Asad_Ali) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 ❰ ᴊᴏɪɴ ʜᴇʀᴇ ❱ 🌹", url=f"https://t.me/Alexa_Help")
                ]
                
           ]
        ),
    )                       
    sender_id = message.from_user.id
    sender_name = message.from_user.username
    return await client.send_message(LOG_ID, f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** @{sender_name}")

@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help(client, message):
    lamao = await message.reply_text(
        text=AlexaData.HELP_STRING,
        reply_markup=InlineKeyboardMarkup(AlexaData.H_BUTTON),
    )