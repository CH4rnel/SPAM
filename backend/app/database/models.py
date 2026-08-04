# ♃ ☿ 𓂀  SPAM CONFIG LAYER 𓂀  ☿ ♃

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Base database model.
    """

    pass


class User(Base):
    """
    Anonymous SPAM user model.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    anonymous_hash: Mapped[str] = mapped_column(
        String(128),
        unique=True,
        nullable=False,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
    )
