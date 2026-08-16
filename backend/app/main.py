from fastapi import FastAPI

from app.api.health import router as health_router
from app.config.settings import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description=(
        "ServerWatch infrastructure monitoring "
        "and incident management API."
    ),
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "service": "serverwatch-api",
        "version": "0.1.0",
        "status": "running",
    }