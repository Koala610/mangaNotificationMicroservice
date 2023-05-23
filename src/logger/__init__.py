from datetime import datetime, timezone
from core_logger import logger

cur_time = datetime.now(timezone.utc).astimezone()
cur_time = datetime.strftime(cur_time, '%z')
logger.basicConfig(
    level=logger.INFO,
    format='[%(asctime)s] [%(levelname)s] - %(message)s | locale: "%(pathname)s", line %(lineno)d, in <module>',
    datefmt=f'%Y-%m-%d %H:%M:%S {cur_time}')