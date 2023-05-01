# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved Modified, Enhanced And Database Added By ©️ Team Alexa
""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2022 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from env import MONGO_DB_URI


MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.wbb
