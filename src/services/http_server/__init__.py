import fastapi
from src.routers import notification_router

app = fastapi.FastAPI(docs_url="/docs")
app.include_router(notification_router)