import os
from os import environ

API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = set(int(x) for x in os.environ.get("ADMINS", "1914868167").split())
GROUPS = [int(admin) for admin in environ.get("GROUPS", "").split()]
