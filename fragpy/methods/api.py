import aiohttp
from aiocache import Cache

async def send(method: str, url: str, params=None, json=None, headers=None, cookies=None, data=None):
    async with aiohttp.ClientSession() as session:

        async with session.request(method, url, params=params, json=json, headers=headers, cookies=cookies, data=data) as response:
            try:
                data = await response.json() 
            except aiohttp.ContentTypeError:
                data = await response.text() 
            return data, response
