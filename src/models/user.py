import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import db

class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True)
    password: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)
    role_id: Mapped[int] = mapped_column(sa.ForeignKey("role.id", name="fk_user_role_id"))
    role: Mapped["Role"] = relationship("Role", back_populates="users")
    
    def __repr__(self):
        return f"Users(id={self.id!r}, username={self.username!r}, active={self.active!r})"