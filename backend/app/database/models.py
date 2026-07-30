# ♃ ☿ 𓂀  OCCULT CONFIG LAYER 𓂀  ☿ ♃

from datetime import datetime

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from sqlalchemy import (
    String,
    Integer,
    DateTime,
)


class Base(DeclarativeBase):
    pass



class User(Base):

    __tablename__ = "users"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    spam_hash: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        index=True
    )


    rank: Mapped[str] = mapped_column(
        String(50),
        default="Wanderer"
    )


    karma: Mapped[int] = mapped_column(
        Integer,
        default=0
    )


    language: Mapped[str] = mapped_column(
        String(10),
        default="en"
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
