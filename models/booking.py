# models/booking.py

from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from models import Base

class Booking(Base):
    """
    Represents a booking made by a user for a specific room.
    """
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)  # Unique booking ID
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Linked user
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)  # Linked room
    start_date = Column(Date, nullable=False)  # Booking start date
    end_date = Column(Date, nullable=False)    # Booking end date
    status = Column(String, default='pending')  # Booking status

    user = relationship("User", back_populates="bookings")  # Relationship to user
    room = relationship("Room", back_populates="bookings")  # Relationship to room
