# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base



class User(Base):

    __tablename__ = "users"


    id: Mapped[int] = mapped_column(
        primary_key=True,
    )


    spam_hash: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        index=True,
        nullable=False,
    )


    rank: Mapped[str] = mapped_column(
        String(32),
        default="wanderer",
    )


    karma: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )


    language: Mapped[str] = mapped_column(
        String(8),
        default="en",
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
