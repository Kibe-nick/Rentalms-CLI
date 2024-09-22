from models.apartment import Apartment
from models.room import Room
import pytest

def test_create_apartment(session):
    """
    Test creating an apartment and ensuring its details are stored correctly.
    """
    # Create an apartment
    apartment = Apartment(name="Sunset Apartments", address="789 Pine Street")
    session.add(apartment)
    session.commit()

    # Verify the apartment's details
    assert apartment.name == "Sunset Apartments"
    assert apartment.address == "789 Pine Street"

def test_apartment_with_multiple_rooms(session):
    """
    Test that an apartment can have multiple rooms.
    """
    # Create an apartment
    apartment = Apartment(name="Evergreen Apartments", address="101 Forest Lane")
    session.add(apartment)
    session.commit()

    # Create multiple rooms
    room1 = Room(number="301", apartment_id=apartment.id, capacity=2)
    room2 = Room(number="302", apartment_id=apartment.id, capacity=1)
    session.add_all([room1, room2])
    session.commit()

    # Verify the apartment has the correct number of rooms
    assert len(apartment.rooms) == 2
    assert apartment.rooms[0].number == "301"
    assert apartment.rooms[1].number == "302"
