# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):

    app_name: str = "SPAM Network"

    app_version: str = "0.1.0"

    environment: str = "development"


    host: str = "0.0.0.0"

    port: int = 8000


    database_async_url: str

    database_sync_url: str


    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )


settings = Settings()
