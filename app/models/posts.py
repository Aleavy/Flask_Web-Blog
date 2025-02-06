from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone


class Blog_Post(db.Model):
    __tablename__ = "blog_post"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(60), nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)
    image : Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    date_created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now(timezone.utc))
    edited: Mapped[datetime] = mapped_column(nullable=True)

    user_id: Mapped[int] = mapped_column(db.ForeignKey("blog_user.id"), nullable=False)

    user: Mapped["Blog_User"] = relationship("Blog_User", back_populates="post")