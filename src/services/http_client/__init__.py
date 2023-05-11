import aiohttp

from typing import Union, Protocol

class HTTPClient(Protocol):

    async def get(self, url: str,headers: dict = None, params: dict = None) -> Union[dict, None]: ...

    async def post(self, url: str, headers: dict = None, data: dict = None) -> Union[dict, None]: ... 

class HTTPClientImpl:

    def __init__(self):
        pass

    async def get(self, url: str,headers: dict = None, params: dict = None) -> Union[dict, None]:
        headers = headers or {}
        params = params or {}
        response = {}
        async with aiohttp.ClientSession() as client:
            async with client.get(url, headers=headers, params=params) as resp:
                response["text"] = await resp.text()
                response["status"] = resp.status
        return response

    async def post(self, url: str, headers: dict = None, data: dict = None) -> Union[dict, None]:
        headers = headers or {}
        response = {}
        async with aiohttp.ClientSession() as client:
            async with client.post(url, headers=headers, data=data) as resp:
                response["text"] = await resp.text()
                response["status"] = resp.status
        return response