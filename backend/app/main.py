# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging

from app.api.routes import router


setup_logging()


app = FastAPI(

    title=settings.app_name,

    version=settings.app_version

)


app.include_router(router)
