# models/room.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from modelss import Base

class Room(Base):
    """
    Represents a room within an apartment complex.
    """
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)  # Unique room ID
    number = Column(String, nullable=False)  # Room number
    apartment_id = Column(Integer, ForeignKey('apartments.id'), nullable=False)  # Linked apartment
    capacity = Column(Integer, nullable=False)  # Max occupants

    apartment = relationship("Apartment", back_populates="rooms")  # Relationship to apartment
    bookings = relationship("Booking", back_populates="room")  # Relationship to bookings
