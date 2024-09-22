from models.booking import Booking
from models.room import Room
from datetime import datetime

def create_booking(session, user_id, room_id, start_date, end_date):
    """
    Creates a booking for a given user and room.
    
    :param session: SQLAlchemy session
    :param user_id: ID of the user making the booking
    :param room_id: ID of the room being booked
    :param start_date: Start date of the booking
    :param end_date: End date of the booking
    :return: The created booking object
    """
    # Check if the room is available for the given dates
    existing_booking = session.query(Booking).filter(
        Booking.room_id == room_id,
        Booking.start_date <= end_date,
        Booking.end_date >= start_date
    ).first()
    
    if existing_booking:
        raise ValueError("Room is already booked for the selected dates.")
    
    # Create a new booking
    booking = Booking(
        user_id=user_id,
        room_id=room_id,
        start_date=start_date,
        end_date=end_date,
        status="confirmed"
    )
    
    session.add(booking)
    session.commit()
    
    return booking

def cancel_booking(session, booking_id):
    """
    Cancels an existing booking by setting its status to 'canceled'.
    
    :param session: SQLAlchemy session
    :param booking_id: ID of the booking to cancel
    :return: None
    """
    booking = session.get(Booking, booking_id)
    
    if not booking:
        raise ValueError(f"Booking with ID {booking_id} not found.")
    
    booking.status = "canceled"
    session.commit()
    return booking

def get_booking_by_id(session, booking_id):
    """
    Retrieves a booking by its ID.
    
    :param session: SQLAlchemy session
    :param booking_id: ID of the booking
    :return: Booking object if found, None otherwise
    """
    return session.query(Booking).get(booking_id)
