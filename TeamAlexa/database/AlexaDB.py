# Copyright ©️ 2023 Team Alexa : All Rights Reserved Modified, Enhanced And Database Added By ©️ Team Alexa
""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2022 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

from typing import Dict, List, Union
from TeamAlexa.database import db as alexa

chatsdb = alexa.chats
usersdb = alexa.tgusersdb

async def is_telegraph_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def get_telegraph_chats() -> list:
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list


async def add_telegraph_chat(chat_id: int):
    is_served = await is_telegraph_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})


async def remove_telegraph_chat(chat_id: int):
    is_served = await is_telegraph_chat(chat_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"chat_id": chat_id})


async def is_telegraph_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_telegraph_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_telegraph_user(user_id: int):
    is_served = await is_telegraph_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})