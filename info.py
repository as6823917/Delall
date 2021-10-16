import os
from os import environ

API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = set(int(x) for x in os.environ.get("ADMINS", "1914868167").split())
TIME = os.environ.get("TIME", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
