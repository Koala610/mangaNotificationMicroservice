import asyncio

from src import logger
from src.config import UPDATE_FREQUENCY
from src.models.user import User
from typing import List
from datetime import datetime, timedelta
from src.repositories import user_repository
from src.services.bot_api import BotApiService, ApiService

class NotificationService:

    def __init__(self) -> None:
        self.api_service: ApiService = BotApiService()

    async def send_updates(self):
        while True:
            users: List[User] = user_repository.find_by_subscription(is_subscribed=True)
            logger.info("Checking updates...")
            for user in users:
                last_updated = user.last_updated
                if last_updated is None or datetime.now() - last_updated > timedelta(minutes=UPDATE_FREQUENCY):
                    user_repository.update(user.id, last_updated = datetime.now())
                response: dict = await self.api_service.get_bookmarks_hash(user.id)
                h = response.get("hash")
                if h != user.bookmarks_hash:
                    user_repository.update(user.id, bookmarks_hash=h)
                    request_data: dict = {"message" : "Что-то изменилось у вас в закладках..."}
                    await self.api_service.send_message(user.id, request_data)
            await asyncio.sleep(1)