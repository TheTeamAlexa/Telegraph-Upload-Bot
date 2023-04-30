""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2023 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import env
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)  # type: ignore

alexa = Client(
    ":memory:",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    plugins=dict(root="TeamAlexa"),
)


if __name__ == "__main__":
    print("Starting the bot")
    try:
        alexa.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = alexa.get_me().username
    print(f"@{uname} is now running!")
    idle()
    alexa.stop()
    print("Bot stopped. Alvida!")
