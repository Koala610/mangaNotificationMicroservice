import asyncio
import config

from ..notification import notification_service
from src.logger import logger

def set_frequency(frequency: int):
    logger.info("In decorator")
    def decorator(func):
        async def wrapper(*args, **kwargs):
            while True:
                await asyncio.sleep(frequency)
                await func(*args, **kwargs)
        return wrapper
    return decorator

@set_frequency(config.UPDATE_FREQUENCY)
async def notification_task():
    if config.IS_NOTIFICATION_WORKING:
        logger.info("Sending updates...")
        await notification_service.send_updates()
    await asyncio.sleep(1)