import asyncio

from typing import Protocol
from src.services.http_client import HTTPClientImpl, HTTPClient
from config import BOT_API_URL

class ApiService(Protocol):

    async def get_bookmarks_hash(self) -> dict: ...

    async def send_message(self, data: dict) -> dict: ...

class BotApiService:

    BOT_API_URL = BOT_API_URL

    def __init__(self) -> None:
        self.http_client: HTTPClient = HTTPClientImpl

    async def get_bookmarks_hash(self, id: int) -> dict:
        return await self.http_client.get(f"{BOT_API_URL}/{id}/bookmarks/with_hash")

    async def send_message(self, data: dict) -> dict:
        pass


async def main():
    pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
