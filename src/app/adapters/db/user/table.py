from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from src.app.adapters.db.sqlachemy import Base


class User(Base):
    __tablename__ = "User"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    email: Mapped[str]
