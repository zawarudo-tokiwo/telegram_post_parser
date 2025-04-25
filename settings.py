import os
from dotenv import load_dotenv, find_dotenv


# TODO: use pydantic_settings
env_file = find_dotenv(".env")
load_dotenv(env_file)

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
