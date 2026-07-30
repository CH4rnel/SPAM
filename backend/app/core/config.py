# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str = "SPAM Network"
    app_version: str = "0.1.0"

    environment: str = "development"

    host: str = "0.0.0.0"
    port: int = 8000


    class Config:
        env_file = ".env"


settings = Settings()
