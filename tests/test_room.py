from models.room import Room
from models.apartment import Apartment
import pytest

def test_create_room(session):
    """
    Test creating a room and linking it to an apartment.
    """
    # Create an apartment
    apartment = Apartment(name="Greenwood", address="123 Elm Street")
    session.add(apartment)
    session.commit()

    # Create a room in the apartment
    room = Room(number="101", apartment_id=apartment.id, capacity=2)
    session.add(room)
    session.commit()

    # Verify the room's details
    assert room.number == "101"
    assert room.capacity == 2
    assert room.apartment_id == apartment.id

def test_room_apartment_relationship(session):
    """
    Test that a room correctly belongs to an apartment.
    """
    # Create an apartment and a room
    apartment = Apartment(name="Maple Residence", address="456 Oak Avenue")
    room = Room(number="202", apartment=apartment, capacity=3)

    session.add(apartment)
    session.add(room)
    session.commit()

    # Check the relationship
    assert room.apartment.name == "Maple Residence"
    assert apartment.rooms[0].number == "202"
