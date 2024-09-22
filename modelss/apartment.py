from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from modelss import Base  # Import the Base from your models/__init__.py

class Apartment(Base):
    """
    Represents an apartment complex in the Rental Management System.
    """
    __tablename__ = 'apartments'

    id = Column(Integer, primary_key=True)  # Unique apartment ID
    name = Column(String, nullable=False)   # Name of the apartment complex
    address = Column(String, nullable=False)  # Physical address

    # Relationship to rooms
    rooms = relationship("Room", back_populates="apartment")
