from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Note(Base):
    __tablename__ = "note"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    text: Mapped[str] = mapped_column(String(512), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
