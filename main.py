import asyncio
from src.client import client
from src.utils import chat_id_getter
from src.config import TARGET_CHATS
from src.tracker import handlers_register

async def main():
    async with client: 
        target_chats = await chat_id_getter(client, TARGET_CHATS)
        handlers_register(target_chats)
        await client.run_until_disconnected()
        
if __name__ == '__main__':
    asyncio.run(main())