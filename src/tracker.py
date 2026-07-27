from telethon import events, types, errors
import asyncio 
from . import config 
from . import logging_config as lc 
from .client import client
from .utils import kword_finder, target_message_formatter
from .notifier import message_sender


def handlers_register(chats: list[int]):
    @client.on(events.NewMessage(chats=chats))
    async def message_tracker(event: events.NewMessage.Event) -> None: 
        try: 
            
            msg = event.message 
            if (text:= msg.message):  
                source = msg.peer_id 
                
                source_user = None 
                source_username = None 
                
                try: 
                    if isinstance(source, types.PeerUser):
                        source_user = await client.get_entity(source.user_id)
                    elif isinstance(source, types.PeerChannel):
                        source_user = await client.get_entity(source.channel_id)
                    elif isinstance(source, types.PeerChat):
                        source_user = await client.get_entity(source.chat_id)
                except (TypeError, ValueError) as exp:
                    lc.exp_logger.error(f'({type(exp).__name__}) {exp}.')
                
                if source_user:
                    source_username = source_user.username 
                    
                dt = msg.date.strftime('%d.%m.%Y %I:%M:%S %p')
                
                if (kwords:= kword_finder(config.KEYWORDS, text)): 
                    try: 
                        user_id = msg.from_id.user_id 
                        user = await client.get_entity(user_id)
                        username = user.username 
                    except (AttributeError, ValueError):
                        username = None
                    data = target_message_formatter(source_username, dt, username, text, kwords)
                    lc.target_messages_logger.info(data)
                    
                    await message_sender(client, config.NOTIFICATION_CHAT, data)
                                        
                else:   
                    source_username = f'@{source_user.username}' if source_user and source_user.username else 'Unknown'
                    data = f'New message from {source_username}: {text} ({dt})'
                    lc.all_messages_logger.info(data)
        
        except Exception as exp:
            lc.exp_logger.error(f'unexpected error ({type(exp).__name__}: {exp})')
