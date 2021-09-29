from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    review_id = Column(Integer, ForeignKey('reviews.id'))
    writer_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String(500), nullable=False, default="")

    # Many to One
    writer = relationship("User", back_populates="comments", join_depth=1, uselist=False)