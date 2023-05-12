from src.logger import logger
from src.models.user import User
from typing import List
from src.repositories import user_repository
from src.services.bot_api import ApiService

class NotificationService:

    def __init__(self, api_service: ApiService) -> None:
        self.api_service: ApiService = api_service

    async def send_updates(self):
        users: List[User] = user_repository.find_by_subscription(is_subscribed=True)
        for user in users:
            response: dict = await self.api_service.get_bookmarks_hash(user.id)
            h = response.get("hash")
            if h is None:
                logger.error(f"Hash wasn'y accepted for user {user.id}")
                return
            logger.info(f"{h} hash for user {user.id} bookmarks")
            if h != user.bookmarks_hash:
                user_repository.update(user.id, bookmarks_hash=h)
                request_data: dict = {"message" : "Что-то изменилось у вас в закладках..."}
                await self.api_service.send_message(user.id, request_data)
