from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    fullname: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
