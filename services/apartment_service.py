# services/apartment_service.py

from models.apartment import Apartment
from sqlalchemy.orm import Session

def create_apartment(session: Session, name: str, location: str, num_rooms: int) -> Apartment:
    """Creates a new apartment."""
    apartment = Apartment(name=name, location=location, num_rooms=num_rooms)
    session.add(apartment)
    session.commit()
    session.refresh(apartment)
    return apartment
