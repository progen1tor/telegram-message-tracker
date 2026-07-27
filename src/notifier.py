import asyncio
from telethon import TelegramClient, errors
from .logging_config import exp_logger 


async def message_sender(
    client: TelegramClient, 
    notification_chat: str, 
    data: str
    ) -> None:
    for _ in range(5):  
        try: 
            await client.send_message(notification_chat, data)
            return  
        
        except errors.FloodWaitError as exp:
            exp_logger.error(f'limit exceeded - wait for {exp.seconds} seconds ({exp}).')
            await asyncio.sleep(exp.seconds)
            
        except errors.RPCError as exp:
            exp_logger.error(f'telegram error while sending notification ({exp}).')
            return 
        
        except (
            ConnectionError, ConnectionResetError,
            TimeoutError, OSError, asyncio.TimeoutError
        ) as exp:
            exp_logger.error(f'network problem ({type(exp).__name__}: {exp}).')
            return 
        
        except Exception as exp:
            exp_logger.error(f'unexpected error ({type(exp).__name__}: {exp}).')
            return 
        
    exp_logger.error(f'Failed to send message to {notification_chat} after 5 attempts.')