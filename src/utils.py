from telethon import TelegramClient


async def chat_id_getter(client: TelegramClient, chat_list: list[str]) -> list[int]:
    ids = []
    
    async with client: 
        for chat in chat_list:
            chat_entity = await client.get_entity(chat)
            ids.append(chat_entity.id)
    
    return ids 


def kword_finder(kwords: list[str], text: str) -> list[str]: 
    return [w for w in kwords if w in text.lower()]