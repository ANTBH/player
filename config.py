import os
from os import getenv
from dotenv import load_dotenv
from OWNER import BOT_TOKEN, OWNER, OWNER_NAME, DATABASE, CHANNEL, GROUP, LOGS, VIDEO , PHOTO

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
user = {}
call = {}
dev = {}
logger = {}
logger_mode = {}
botname = {}
appp = {}
helper = {}



API_ID = int(getenv("API_ID", "12847352"))
API_HASH = getenv("API_HASH", "19b76e60ee49e2356497d361cabcf7a8")
BOT_TOKEN = BOT_TOKEN
MONGO_DB_URL = DATABASE
OWNER = OWNER
OWNER_NAME = OWNER_NAME
CHANNEL = CHANNEL
GROUP = GROUP
LOGS = LOGS
VIDEO = VIDEO
PHOTO = PHOTO
