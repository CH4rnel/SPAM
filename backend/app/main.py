# ♃ ☿ 𓂀  SPAM CONFIG LAYER 𓂀  ☿ ♃

from fastapi import FastAPI

from app.api.v1.router import router
from app.core.config import settings


def create_application() -> FastAPI:

    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
    )

    application.include_router(
        router,
        prefix="/api/v1",
    )

    return application


app = create_application()
