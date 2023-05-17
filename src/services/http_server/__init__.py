import fastapi
import config
from src.routers import notification_router

bot_host = config.BOT_API_URL.split("//")[1]
bot_host = bot_host.split(":")[0] if bot_host.find(":") else bot_host
trusted_hosts = [
    bot_host,
    "127.0.0.1"
]

app = fastapi.FastAPI(docs_url="/docs")
app.include_router(notification_router)

@app.middleware("http")
async def set_trusted_addresses(request: fastapi.Request, call_next):
    print(trusted_hosts)
    if request.client.host not in trusted_hosts:
        return fastapi.responses.PlainTextResponse("Forbidden", status_code=403)
    return await call_next(request)