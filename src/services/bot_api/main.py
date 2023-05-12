import asyncio
import json

from typing import Protocol
from src.services.http_client import HTTPClientImpl, HTTPClient
from config import BOT_API_URL, ADMIN_USERNAME, ADMIN_PASSWORD

class ApiService(Protocol):

    async def get_bookmarks_hash(self) -> dict: ...

    async def send_message(self, data: dict) -> dict: ...

class BotApiService:

    def __init__(self, http_client: HTTPClient) -> None:
        self.http_client: HTTPClient = http_client
        self.access_token: str = "123"

    async def get_bookmarks_hash(self, id: int) -> dict:
        is_access_token_valid = await self.verify_access_token()
        is_access_token_valid = bool(json.loads(is_access_token_valid.get("text")).get("result"))
        if not is_access_token_valid:
            tmp = await self.auth(ADMIN_USERNAME, ADMIN_PASSWORD)
            self.access_token = json.loads(tmp.get("text")).get("access_token")
        return await self.http_client.get(f"{BOT_API_URL}/{id}/bookmarks/hash", headers={"Authorization": f"Bearer {self.access_token}"})

    async def send_message(self, data: dict) -> dict:
        pass

    async def verify_access_token(self):
        return await self.http_client.post(f"{BOT_API_URL}/verify-jwt", data = {"access_token": self.access_token})

    async def auth(self, username: str, password: str):
        return await self.http_client.post(f"{BOT_API_URL}/login", data = {"username": username, "password": password})

async def main():
    pass

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()