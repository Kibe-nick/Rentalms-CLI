# models/user.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from modelss import Base

class User(Base):
    """
    Represents a user in the Rental Management System.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # Unique user ID
    name = Column(String, nullable=False)   # User's full name
    email = Column(String, nullable=False, unique=True)  # User's email address
    password = Column(String, nullable=False)  # User's hashed password
    is_admin = Column(Boolean, default=False)  # Admin flag

    bookings = relationship("Booking", back_populates="user")  # Relationship to bookings
