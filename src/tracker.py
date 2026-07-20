import pyrogram
from pyrogram import filters 
from pyrogram.types import Message 
import config 
from logging_config import all_messages_logger, target_messages_logger, exp_logger

async def message_tracker(app: pyrogram.Client, message: Message) -> None: 
    new_message = f'New message from {message.chat.title}:\n{message.text}'  
    all_messages_logger.info(new_message)
    
    for word in config.KEYWORDS: 
        if not message.text: 
            break 
        if word in message.text.lower():
            chat_link = f'https://t.me/{message.chat.username}' if message.chat.username else 'Private chat'
            dt = message.date.strftime('%d.%m.%Y %I:%M:%S %p')
            author = f'@{message.from_user.username}' if message.from_user.username else 'Unknown message author'
            
            data = f'Chat: {chat_link}\nDate: {dt}\nWord found: {word}\nAuthor: {author}\nMessage text: {message.text}'
            target_messages_logger.info(data)
            
            await app.send_message(config.NOTIFICATION_CHAT, data)  # ! notifier.py 
            
            
@app.on_message(filters=filters.chat(config.TARGET_CHATS) & filters.text)
async def message_handler(app: pyrogram.Client, message: Message) -> None: 
    await message_tracker(app, message)
    
app.run()