from telethon import TelegramClient, events, types 
import config 
import logging_config as lc 
from client import client
from utils import kword_finder, target_message_formatter


def handlers_register(chats: list[int]):
    @client.on(events.NewMessage(chats=chats))
    async def message_tracker(event: events.NewMessage.Event) -> None: 
        msg = event.message 
        if (text:= msg.message):  
            source = msg.peer_id 
            
            source_user = None 
            
            if isinstance(source, types.PeerUser):
                source_user = await client.get_entity(source.user_id)
            elif isinstance(source, types.PeerChannel):
                source_user = await client.get_entity(source.channel_id)
            
            if source_user:
                source_username = source_user.username or 'Unknown source'
            else: 
                source_username = 'Unknown source'
                
            dt = msg.date.strftime('%d.%m.%Y %I:%M:%S %p')
            
            if (kwords:= kword_finder(config.KEYWORDS, text)): 
                try: 
                    user_id = msg.from_id.user_id 
                    user = await client.get_entity(user_id)
                    username = user.username or 'Unknown'
                except (AttributeError, ValueError):
                    username = 'Unknown'
                data = target_message_formatter(source_username, dt, username, text, kwords)
                lc.target_messages_logger.info(data)
                
                await client.send_message(config.NOTIFICATION_CHAT, data)
                
            else:   
                data = f'New message from @{source_username}: {text} ({dt})'
                lc.all_messages_logger.info(data)
