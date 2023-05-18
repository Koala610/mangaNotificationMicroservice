import fastapi
import config
import os
from src.logger import logger
from typing import Optional

router = fastapi.APIRouter()

def change_env_variable(variable_name: str, new_value: str):
    dot_env_path = ".env"
    with open(dot_env_path, "r", encoding="utf-8") as file:
        file_contents = file.readlines()

        for i, line in enumerate(file_contents):
            if line.startswith(f"{variable_name}"):
                file_contents[i] = f"{variable_name}={new_value}\n"

    with open(dot_env_path, "w") as file:
        file.writelines(file_contents)

@router.get("/notification/service/working_state")
async def turn_on_off_notifications(change: Optional[bool] = True):
    if change:
        config.IS_NOTIFICATION_WORKING = not config.IS_NOTIFICATION_WORKING
        change_env_variable("IS_NOTIFICATION_WORKING", config.IS_NOTIFICATION_WORKING)
    return config.IS_NOTIFICATION_WORKING

@router.get("/notification/service")
async def change_update_frequency(update_frequency: Optional[int] = None, change: Optional[bool] = True):
    if change and update_frequency is not None:
        config.UPDATE_FREQUENCY = update_frequency
        change_env_variable("UPDATE_FREQUENCY", config.UPDATE_FREQUENCY)
    return config.UPDATE_FREQUENCY