from telethon import TelegramClient
from telethon.tl.functions.contacts import SearchRequest

api_id = 33308378
api_hash = 'cd1f27e05accf4d4dc93f3189eeb9a9a'

client = TelegramClient('session', api_id, api_hash)

async def main():
    for keyword in ['越南', '猪肉', '越南猪肉']:
        result = await client(SearchRequest(
            q=keyword,
            limit=50
        ))
        print(f'=== 关键词: {keyword} ===')
        for chat in result.chats:
            print(f'名称: {chat.title}')
            try:
                print(f'用户名: @{chat.username}')
            except:
                print('用户名: 无')
            print('---')

with client:
    client.loop.run_until_complete(main())
