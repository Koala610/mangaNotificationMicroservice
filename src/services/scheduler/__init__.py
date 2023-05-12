import asyncio

from .main import notification_task
from ..http_server import app

@app.on_event("startup")
async def schedule():
    asyncio.create_task(notification_task())
