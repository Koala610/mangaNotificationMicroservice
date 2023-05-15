import fastapi
import config
import os
from src.logger import logger

router = fastapi.APIRouter()

def change_env_variable(variable_name: str, new_value: str):
    dot_env_path = ".env"
    with open(dot_env_path, "r") as file:
        file_contents = file.readlines()

        for i, line in enumerate(file_contents):
            if line.startswith(f"{variable_name}"):
                file_contents[i] = f"{variable_name}={new_value}\n"

    with open(dot_env_path, "w") as file:
        file.writelines(file_contents)

@router.get("/notification/service/working_state")
async def turn_on_off_notifications():
    config.IS_NOTIFICATION_WORKING = not config.IS_NOTIFICATION_WORKING
    change_env_variable("IS_NOTIFICATION_WORKING", config.IS_NOTIFICATION_WORKING)
    return {"message": f"Notification {'not' if not config.IS_NOTIFICATION_WORKING else ''} working"}

@router.get("/notification/service")
async def change_update_frequency(update_frequency: int):
    config.UPDATE_FREQUENCY = update_frequency
    change_env_variable("UPDATE_FREQUENCY", config.UPDATE_FREQUENCY)
    return {"message": f"Update frequency now: {config.UPDATE_FREQUENCY}"}