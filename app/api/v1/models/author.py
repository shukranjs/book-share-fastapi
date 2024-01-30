# models.py

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    biography = Column(String)

    # Define relationship with User
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="author")

    # Define relationship with Book
    books = relationship("Book", back_populates="author")
