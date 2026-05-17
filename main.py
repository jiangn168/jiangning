from telethon import TelegramClient
from telethon.tl.functions.contacts import SearchRequest
from telethon.tl.functions.messages import SearchGlobalRequest
from telethon.tl.types import InputMessagesFilterEmpty

api_id = 33308378
api_hash = 'cd1f27e05accf4d4dc93f3189eeb9a9a'

client = TelegramClient('session', api_id, api_hash)

async def main():
    keywords = ['越南', '猪肉', '越南猪肉']
    
    for keyword in keywords:
        # 搜索频道和群组
        result = await client(SearchRequest(
            q=keyword,
            limit=50
        ))
        print(f'=== 频道/群组: {keyword} ===')
        for chat in result.chats:
            print(f'名称: {chat.title}')
            try:
                print(f'用户名: @{chat.username}')
            except:
                print('用户名: 无')
            print('---')
        
        # 搜索聊天记录
        messages = await client(SearchGlobalRequest(
            q=keyword,
            filter=InputMessagesFilterEmpty(),
            min_date=None,
            max_date=None,
            offset_rate=0,
            offset_peer='username',
            offset_id=0,
            limit=50
        ))
        print(f'=== 消息记录: {keyword} ===')
        for msg in messages.messages:
            print(f'内容: {msg.message}')
            print('---')

with client:
    client.loop.run_until_complete(main())
