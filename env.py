""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2023 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "")
LOG_ID = int(os.getenv("LOG_ID", ""))

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not MONGO_DB_URI:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
if not LOG_ID:
    print("No Log group defined...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit