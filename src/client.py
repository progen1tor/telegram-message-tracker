from telethon import TelegramClient
import config 

client = TelegramClient(
    session=config.SESSION_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH
)