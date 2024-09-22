# models/__init__.py

from sqlalchemy.orm import declarative_base

# Create the base class for your models
Base = declarative_base()

# Import the models to ensure they are registered with SQLAlchemy
from .user import User
from .apartment import Apartment
from .room import Room
from .booking import Booking
