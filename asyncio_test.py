import asyncio
import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def call_url(url):
    print('Starting {}'.format(url))
    response = await aiohttp.ClientSession().get(url)
    data = await response.text()
    print('{}: {} bytes:'.format(url, len(data)))
    return data

futures = [call_url(url) for url in urls]

asyncio.run(asyncio.wait(futures))