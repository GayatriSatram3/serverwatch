from fastapi import APIRouter
from sqlalchemy import text

from app.database.connection import engine


router = APIRouter(
    prefix="/api/v1",
    tags=["Health"],
)


@router.get("/health")
def health_check():
    database_status = "healthy"

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception:
        database_status = "unhealthy"

    overall_status = (
        "healthy"
        if database_status == "healthy"
        else "unhealthy"
    )

    return {
        "status": overall_status,
        "service": "serverwatch-api",
        "database": database_status,
    }