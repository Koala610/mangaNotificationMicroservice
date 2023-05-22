import asyncio
import config

from ..notification import notification_service
from src.logger import logger

def get_current_update_frequency():
    return config.UPDATE_FREQUENCY

def set_frequency(get_freq_func):
    logger.info("In decorator")
    def decorator(func):
        async def wrapper(*args, **kwargs):
            while True:
                frequency = get_freq_func()
                await asyncio.sleep(frequency)
                await func(*args, **kwargs)
        return wrapper
    return decorator

@set_frequency(get_current_update_frequency)
async def notification_task():
    if config.IS_NOTIFICATION_WORKING:
        logger.info("Sending updates...")
        await notification_service.send_updates()
    await asyncio.sleep(1)