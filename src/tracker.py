from telethon import TelegramClient, events, types 
import config 
import logging_config as lc 
from client import client
from utils import kword_finder

chats = []  # plug 

@client.on(events.NewMessage(chats=chats))
async def message_tracker(event: events.NewMessage.Event) -> None: 
    msg = event.message 
    if (text:= msg.message):  # если вообще нет текста - скип 
        source = msg.peer_id 
        if isinstance(source, types.PeerUser):
            source_user = await client.get_entity(source.user_id)
        elif isinstance(source, types.PeerChannel):
            source_user = await client.get_entity(source.channel_id)
        source_username = source_user.username if source_user.username else 'Unknown sourse'
        dt = msg.date.strftime('%d.%m.%Y %I:%M:%S %p')
        
        if (kwords:= kword_finder(config.KEYWORDS, text)):  # если найдены кворды 
            try: 
                user_id = msg.from_id.user_id 
                user = await client.get_entity(user_id)
                username = user.username if user.username else 'Unknown'
            except AttributeError:
                username = 'Unknown'
            data = f'=== NEW MESSAGE WITH KEYWORDS FROM @{source_username} ===\nDATE: {dt}\nusername: @{username}\ntext: {text}\nkeywords found: {', '.join(kwords)}\n'
            lc.target_messages_logger.info(data)
            
            await client.send_message(config.NOTIFICATION_CHAT, data)
            
        else:  # если кворды не найдены 
            data = f'New message from @{source_username}: {text} ({dt})'
            lc.all_messages_logger.info(data)