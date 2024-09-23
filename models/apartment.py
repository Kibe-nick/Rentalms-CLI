from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base  # Import the Base from your models/__init__.py

class Apartment(Base):
    """
    Represents an apartment complex in the Rental Management System.
    """
    __tablename__ = 'apartments'

    id = Column(Integer, primary_key=True, index=True)  # Unique apartment ID
    name = Column(String, index=True)   # Name of the apartment complex
    location = Column(String)  # Physical address
    num_rooms = Column(Integer)
    # Relationship to rooms
    rooms = relationship("Room", back_populates="apartment")
