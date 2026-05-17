from telethon import TelegramClient
from telethon.tl.functions.contacts import SearchRequest
from telethon.tl.functions.messages import SearchGlobalRequest
from telethon.tl.types import InputMessagesFilterEmpty
import asyncio

api_id = '33308378'
api_hash = 'cd1f27e05accf4d4dc93f3189eeb9a9a'

client = TelegramClient('session', api_id, api_hash)

async def main():
    # 搜索包含"烟"关键词的频道和群组
    result = await client(SearchRequest(
        q='烟',
        limit=50
    ))
    
    print('=== 找到的频道/群组 ===')
    for chat in result.chats:
        print(f'名称: {chat.title}')
        try:
            print(f'用户名: @{chat.username}')
        except:
            print('用户名: 无')
        print('---')

with client:
    client.loop.run_until_complete(main())
