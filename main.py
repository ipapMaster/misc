"""
asyncio
Asyncio – модуль асинхронного программирования,
который был представлен в Python
https://habr.com/ru/companies/otus/articles/509328/
"""
import signal
import sys
import json
import asyncio
import aiohttp

loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)


async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_reddit_top(subreddit, client):
    url = 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5'
    print(url)
    data1 = await get_json(client, url)
    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + ' (' + link + ')')
    print('Готово:', subreddit + '\n')


def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# asyncio.ensure_future(get_reddit_top('python', client))
asyncio.ensure_future(get_reddit_top('programming', client))
asyncio.ensure_future(get_reddit_top('compsci', client))
loop.run_forever()
