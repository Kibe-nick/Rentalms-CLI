from datetime import date
from models import Booking, User, Room
from services.booking_service import create_booking, cancel_booking
import pytest

def test_create_booking(session):
    # Create dummy user and room
    user = User(name="John Doe", email="john@example.com", password="hashedpass")
    room = Room(number="101", apartment_id=1, capacity=2)
    session.add(user)
    session.add(room)
    session.commit()

    # Define booking dates
    start_date = date(2024, 9, 20)
    end_date = date(2024, 9, 25)
    
    # Test creating a booking
    booking = create_booking(session, user_id=user.id, room_id=room.id, start_date=start_date, end_date=end_date)
    assert booking.user_id == user.id
    assert booking.room_id == room.id
    assert booking.start_date == start_date
    assert booking.end_date == end_date

def test_cancel_booking(session):
    # Create dummy user, room, and booking
    user = User(name="Jane Doe", email="jane@example.com", password="hashedpass")
    room = Room(number="102", apartment_id=1, capacity=2)
    session.add(user)
    session.add(room)
    session.commit()

    start_date = date(2024, 9, 21)
    end_date = date(2024, 9, 26)
    booking = create_booking(session, user_id=user.id, room_id=room.id, start_date=start_date, end_date=end_date)

    # Test canceling a booking
    canceled_booking = cancel_booking(session, booking_id=booking.id)
    assert canceled_booking.status == 'canceled'
