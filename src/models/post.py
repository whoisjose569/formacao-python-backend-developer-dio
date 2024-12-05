from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import db
import sqlalchemy as sa

class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)
    created: Mapped[datetime] = mapped_column(sa.DateTime, server_default=sa.func.now())
    author_id: Mapped[int] = mapped_column(sa.ForeignKey('user.id'))

    def __repr__(self):
        return f"Users(id={self.id!r}, title={self.title!r}, author_id={self.author_id!r})"