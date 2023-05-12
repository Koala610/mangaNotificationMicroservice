from .main import NotificationService
from ..bot_api import bot_api_service

notification_service = NotificationService(bot_api_service)