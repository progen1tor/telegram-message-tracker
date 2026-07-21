import pyrogram
import config 

app = pyrogram.Client(
    name=config.SESSION_NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH
)