from .main import BotApiService, ApiService
from ..http_client import http_client

bot_api_service: ApiService = BotApiService(http_client=http_client)