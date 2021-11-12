from config_telethon import *
import telethon, pandas, time, datetime
from telethon import TelegramClient

client = TelegramClient(name, api_id, api_hash)


async def main(chats):
    posts, i = list(), 0

    while i < len(chats):
        channel = chats[i]
        channel_entity = await client.get_entity(channel)
        async for message in client.iter_messages(channel_entity, offset_date=datetime.datetime.today()):
                posts.append({'channel': channel_entity, 'text': str(message.message), 'date': message.date})
        i += 1
        time.sleep(300)
        print('Next iteration, groups left:', len(chats)-i)

    df = pandas.DataFrame(posts)
    df.to_csv('tg_news.csv', encoding='utf-8')

    return df

    
with client:
    print(client.loop.run_until_complete(main(chats)))

    


