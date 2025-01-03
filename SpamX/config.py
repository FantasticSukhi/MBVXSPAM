import os
from os import getenv as env
from SpamX.functions.logger import LOGS
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(env("API_ID", 27251761))
if API_ID is None:
    LOGS.error("Please set your API_ID!")
    quit(1)

API_HASH = str(env("API_HASH", "22561f023ab0dccfe3b609845014ff0b"))
if API_HASH is None:
    LOGS.error("Please set your API_HASH!")
    quit(1)

ASSISTANT_TOKEN = str(env("ASSISTANT_TOKEN", "6873452469:AAG4mhD3lDpOBickoDdRznjTLM0FnF3w9jg"))
if ASSISTANT_TOKEN is None:
    LOGS.error("Please set your ASSISTANT_TOKEN!")
    quit(1)

OWNER_ID = int(env("OWNER_ID", 6713994904))
if OWNER_ID is None:
    LOGS.error("Please set your OWNER_ID!")
    quit(1)

DATABASE_URL = str(env("DATABASE_URL"))
if DATABASE_URL is None:
    LOGS.error("Please set your DATABASE_URL!")
    quit(1)

LOGGER_ID = str(env("LOGGER_ID"))
if LOGGER_ID is None:
    LOGS.error("Please set your LOGGER_ID! (make a private group add assistant in that group & promote as Admin!)")
    quit(1)

# --- ETC
HANDLER = env("HANDLER", ".")
PING_MSG = env("PING_MSG", None)
ALIVE_MSG = env("ALIVE_MSG", None)
ALIVE_MEDIA = env("ALIVE_MEDIA", None)
MULTITASK = env("ALIVE_MEDIA", False)
