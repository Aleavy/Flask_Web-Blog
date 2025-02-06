from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from app import db



class Blog_User(UserMixin, db.Model):
    __tablename__ = "blog_user"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(db.String(80), nullable=False)
    username: Mapped[str] = mapped_column(db.String(80), nullable=False)
    password: Mapped[str] = mapped_column(db.String(120), nullable=False)

    post: Mapped[list["Blog_Post"]] = relationship("Blog_Post", back_populates="user", cascade="all, delete-orphan")

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"<User: {self.id} {self.email}>"