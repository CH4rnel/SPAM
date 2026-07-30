# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)


DATABASE_URL = (
    "postgresql+asyncpg://"
    "spam:"
    "spam_password@"
    "localhost:5432/"
    "spam_network"
)


engine = create_async_engine(
    DATABASE_URL,
    echo=True
)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session():

    async with AsyncSessionLocal() as session:
        yield session
