import sys
import os

from datetime import datetime
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
parent_directory = os.path.dirname(parent_directory)
  
sys.path.append(parent_directory)

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SERVICE_PORT = int(os.getenv("SERVICE_PORT"))
SERVICE_HOST = os.getenv("SERVICE_HOST")

USERNAME = os.getenv("MYSQL_USERNAME")
PASSWORD = os.getenv("MYSQL_PASSWORD")
HOST = os.getenv("MYSQL_HOST")
DATABASE = os.getenv("MYSQL_DATABASE")
PORT = os.getenv("MYSQL_PORT")

DSN = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"

REQUEST_WAITING_TIME = int(os.getenv("REQUEST_WAITING_TIME"))
UPDATE_FREQUENCY = int(os.getenv("UPDATE_FREQUENCY"))
LAST_UPDATED = datetime.now()

BOT_API_URL = os.getenv("BOT_API_URL")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")