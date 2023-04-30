# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved Modified, Enhanced And Database Added By ©️ Team Alexa
""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2022 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

class AlexaData(object):
    STATS = "🌹 **ᴛᴏᴛᴀʟ ᴜsᴇʀs** : {}\n🌹 **ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs** : {}\n\n**──────────────**\n➛ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{}`\n**──────────────**"
    BCAST_USG = "**💐 ᴜꜱᴀɢᴇ**:\n`/broadcast` [ᴍᴇꜱꜱᴀɢᴇ] ᴏʀ ʀᴇᴘʟᴀʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴᴛᴏ ᴄʜᴀᴛs ᴀɴᴅ ᴜsᴇʀs"
    BCAST_DN = "🌹 **ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {} chat(s) and {} user(s).**"
    IN_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🤩 ᴊᴏɪɴ ᴜs", url="https://t.me/Alexa_Help"),
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs 🐲", url="https://t.me/Alexa_BotUpdatest")
            ],
            [
                InlineKeyboardButton("🌐 ᴡᴇʙ ᴘʀᴇᴠɪᴇᴡ 🌐", url=generated_link)
            ]
        ]
    )
    INLINE_SELECT = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🤩 ᴊᴏɪɴ ᴜs", url="https://t.me/Alexa_Help"),
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs 🐲", url="https://t.me/Alexa_BotUpdatest")
            ],
            [
                InlineKeyboardButton("📼 ʏᴏᴜᴛᴜʙᴇ 📼", url="https://youtube/jankarikiduniya")
            ]
        ]
    )
    ERROR_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌋 ʀᴇᴘᴏʀᴛ ᴇʀʀᴏʀ", url="https://t.me/Jankari_Ki_Duniya"),
                InlineKeyboardButton("ᴊᴏɪɴ 🌋", url="https://t.me/Alexa_Help")
            ]
        ]
    )
    REPLAY_MSG = "🌹 ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɪɴᴄʟᴜᴅᴇ ᴛᴇxᴛ ᴀꜰᴛᴇʀ ᴛʜᴇ /upload ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ."
    UPLOAD_MSG = "⬆️ ʏᴏᴜʀ ꜰɪʟᴇ ɪs ʙᴇᴇɴ ᴜᴘʟᴏᴀᴅɪɴɢ..."
    UPLOAD_MSG2 = "🌹 ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ / ᴛᴇxᴛ  / ᴀɴɪᴍᴀᴛɪᴏɴ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ . . ."
    HOLD_MSG = "⏳• ʜᴏʟᴅ ᴏɴ ɪ'ᴍ ᴜᴘʟᴏᴀᴅɪɴɢ . . ."
    ERROR_MSG = "🌹 ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜰɪʟᴇ ꜰᴏʀᴍᴀᴛ ᴏʀ ꜰɪʟᴇ sɪᴢᴇ, ɪᴛ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5 ᴍʙ . . ."
    FILE_ERROR = "😢 sᴏʀʀʏ, ᴛʜᴇ ꜰɪʟᴇ ɪs ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ !"
    H_BUTTON = [
         [
              InlineKeyboardButton(text="๏ ᴀʙᴏᴜᴛ ๏", callback_data="ABOUT_CMD"),
         ],
         [
              InlineKeyboardButton(text="๏ ᴄᴍᴅs ๏", callback_data="CMDS_CMD"),
              InlineKeyboardButton(text="๏ ᴛᴇᴀᴍ ᴀʟᴇxᴀ ๏", callback_data="TEAM_CMD"),
         ],
    ]

    HELP_BACK = [
            [     
                  InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data="HELP_BACK"),
            ],
    ]

    HELP_STRING = f"""
**ɪᴛ ɪs ᴀ ©️ ᴛᴇᴀᴍ ᴀʟᴇxᴀ ᴘʀᴏᴊᴇᴄᴛ ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ʜᴇʟᴘ ᴀʟʟ ᴄᴍᴅ ᴀɴᴅ ᴅᴇᴛᴀɪʟs ᴀʀᴇ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ!**
**──────────────**
<b> ©️ @Alexa_BotUpdatest </b>
"""

    ABOUT_STRING = f"""
➛ ɪɴᴛʀᴏᴅᴜᴄɪɴɢ ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴘʀᴏᴊᴇᴄᴛ ꜰʀᴏᴍ ᴛᴇᴀᴍ ᴀʟᴇxᴀ - ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ! ᴛʜɪs ɪɴᴄʀᴇᴅɪʙʟᴇ ʙᴏᴛ ᴄᴀɴ ᴇꜰꜰᴏʀᴛʟᴇssʟʏ ᴜᴘʟᴏᴀᴅ ᴘɪᴄᴛᴜʀᴇs, ᴠɪᴅᴇᴏs, ᴀɴɪᴍᴀᴛɪᴏɴs, ᴀɴᴅ ᴛᴇxᴛs ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ ᴀɴᴅ ɪɴsᴛᴀɴᴛʟʏ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴛᴏ ᴛʜᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ꜰɪʟᴇ. ᴊᴜsᴛ ʀᴇᴍᴇᴍʙᴇʀ, ꜰᴏʀ ᴛʜᴇ ʙᴇsᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ, ᴇɴsᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ꜰɪʟᴇ ɪs ᴜɴᴅᴇʀ 5ᴍʙ ɪɴ sɪᴢᴇ.
**───────────────**
<b>©️ @Alexa_BotUpdatest & @Alexa_Help </b>
"""

    CMDS_STRING = f"""
<u>**ʜᴇʀᴇ ɪs sᴏᴍᴇ ʙᴀsɪᴄ ᴄᴍᴅs**</u>
**➛ `/stats` ᴄᴏʟʟᴇᴄᴛ ᴄʜᴀᴛs ᴀɴᴅ ᴜsᴇʀ ᴡʜᴇʀᴇ ʙᴏᴛ ɪs ᴡᴏʀᴋɪɴɢ.**
**➛ `/help` ᴛᴏ ᴋɴᴏᴡ ᴀʟʟ ᴀʙᴏᴜᴛ ᴄᴍᴅ ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʙᴏᴛ.**
**➛ `/start` ᴜsᴇᴅ ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.**
**➛ `/upload` ʀᴇᴘʟᴏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴘɪᴄs, ᴠᴅᴏ, ᴀɴɪᴍᴀᴛᴏɴ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ.**
**➛ `/uploadtxt` ʀᴇᴘʟᴀʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟᴀʏ ᴡɪᴛʜ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛᴇxᴛ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ.**
**➛ `/broadcast ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜsᴇʀs ᴀɴᴅ ᴄʜᴀᴛᴇs.**
**───────────────**
<b> ©️ @Alexa_BotUpdatest & @Alexa_Help </b>
"""

    TEAM_STRING = f"""
<u>**ᴛᴇᴀᴍ ᴀʟᴇxᴀ:**</u>
ᴛᴇᴀᴍ ᴀʟᴇxᴀ, ꜰɪʀsᴛʟʏ, ɪᴛ ᴡᴀs ᴍᴀɴᴀɢᴇᴅ ʙʏ ᴀsᴀᴅ ᴀʟɪ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ, ʙᴜᴛ ᴛʜᴇʏ ʜᴀᴠᴇ ᴀʟʟ ʟᴇꜰᴛ. ɴᴏᴡ, ɪᴛ ɪs ʙᴇɪɴɢ ʀᴜɴ ʙʏ ᴀsᴀᴅ ᴀʟɪ ᴀɴᴅ ᴠᴇɴᴏᴍ., ʜᴀs ᴛʀᴜʟʏ ʙᴇᴇɴ ᴀ ꜰᴏʀᴄᴇ ᴛᴏ ʙᴇ ʀᴇᴄᴋᴏɴᴇᴅ ᴡɪᴛʜ. ᴡɪᴛʜ ᴛʜᴇɪʀ ᴅᴇᴅɪᴄᴀᴛɪᴏɴ ᴀɴᴅ ʜᴀʀᴅ ᴡᴏʀᴋ, ᴛʜᴇʏ ʜᴀᴠᴇ ᴍᴀɴᴀɢᴇᴅ ᴛᴏ ᴄʀᴇᴀᴛᴇ ɴᴜᴍᴇʀᴏᴜs ʙᴏᴛs ꜰᴏʀ ᴠᴀʀɪᴏᴜs ᴘᴜʀᴘᴏsᴇs sᴜᴄʜ ᴀs ᴍᴜsɪᴄ, ᴍᴀɴᴀɢᴇᴍᴇɴᴛ, ᴍᴇɴᴛɪᴏɴ, sᴇssɪᴏɴ, ᴄʜᴀᴛʙᴏᴛ, ᴀɴᴅ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ, ᴀᴍᴏɴɢ ᴏᴛʜᴇʀs. ᴛʜᴇɪʀ ᴇꜰꜰᴏʀᴛs ʜᴀᴠᴇ ɴᴏᴛ ɢᴏɴᴇ ᴜɴɴᴏᴛɪᴄᴇᴅ, ᴀs ᴄᴏᴜɴᴛʟᴇss ᴜsᴇʀs ʜᴀᴠᴇ ʙᴇɴᴇꜰɪᴛᴇᴅ ꜰʀᴏᴍ ᴛʜᴇɪʀ ᴄʀᴇᴀᴛɪᴏɴs. ɪɴ ᴀᴅᴅɪᴛɪᴏɴ, ᴛᴇᴀᴍ ᴀʟᴇxᴀ ɪs ᴀʟsᴏ ʀᴇsᴘᴏɴsɪʙʟᴇ ꜰᴏʀ ʀᴜɴɴɪɴɢ ᴛʜᴇ ʜɪɢʜʟʏ sᴜᴄᴄᴇssꜰᴜʟ ᴊᴀɴᴋᴀʀɪ ᴋɪ ᴅᴜɴɪʏᴀ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ, ᴡʜɪᴄʜ ʜᴀs ᴘʀᴏᴠɪᴅᴇᴅ ᴠᴀʟᴜᴀʙʟᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴛᴏ ᴠɪᴇᴡᴇʀs ᴡᴏʀʟᴅᴡɪᴅᴇ. 

<a href="https://www.youtube.com/jankarikiduniya" target="_blank">Click Here To Visit Our Channel</a>

ᴛᴏ ᴀʟʟ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴜᴘᴘᴏʀᴛᴇᴅ ᴛᴇᴀᴍ ᴀʟᴇxᴀ ᴀɴᴅ ᴜᴛɪʟɪᴢᴇᴅ ᴛʜᴇɪʀ ʙᴏᴛs, ᴡᴇ ᴇxᴛᴇɴᴅ ᴏᴜʀ ʜᴇᴀʀᴛꜰᴇʟᴛ ᴛʜᴀɴᴋs. ʏᴏᴜʀ ᴄᴏɴᴛɪɴᴜᴇᴅ sᴜᴘᴘᴏʀᴛ ʜᴀs ʙᴇᴇɴ ɪɴsᴛʀᴜᴍᴇɴᴛᴀʟ ɪɴ ᴅʀɪᴠɪɴɢ ᴛᴇᴀᴍ ᴀʟᴇxᴀ ᴛᴏ ɢʀᴇᴀᴛᴇʀ ʜᴇɪɢʜᴛs, ᴀɴᴅ ᴡᴇ ʟᴏᴏᴋ ꜰᴏʀᴡᴀʀᴅ ᴛᴏ ᴘʀᴏᴠɪᴅɪɴɢ ʏᴏᴜ ᴡɪᴛʜ ᴇᴠᴇɴ ᴍᴏʀᴇ ɪɴɴᴏᴠᴀᴛɪᴠᴇ sᴏʟᴜᴛɪᴏɴs ɪɴ ᴛʜᴇ ꜰᴜᴛᴜʀᴇ.
**──────────────**
<b>©️ @Alexa_BotUpdatest & @Alexa_Help @TheTeamAlexa </b>
"""    