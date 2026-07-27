import json 
from .constants import CONFIG_PATH

with open(CONFIG_PATH, encoding='utf-8') as conf:
    config = json.load(conf)
    
API_ID = config["api_id"]
API_HASH = config["api_hash"]
SESSION_NAME = config["session_name"]
TIMEZONE = config["timezone"]
TARGET_CHATS = config["target_chats"]
KEYWORDS = config["keywords"]
NOTIFICATION_CHAT = config["notification_chat"]