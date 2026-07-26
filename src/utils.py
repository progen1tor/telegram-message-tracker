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


def target_message_formatter(
    source: str | None, 
    dt: str, 
    username: str | None,
    msg_text: str, 
    kwords: list[str]
    ) -> str: 
    final_source = f'@{source}' if source else 'Unknown source' 
    final_username = f'@{username}' if username else 'Unknown' 
    
    return f'=== NEW MESSAGE WITH KEYWORDS FROM {final_source} ===\nDATE: {dt}\nusername: {final_username}\ntext: {msg_text}\nkeywords found: {', '.join(kwords)}\n'
