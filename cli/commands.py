# cli/commands.py

import click
from services.user_service import create_user, authenticate_user
from services.booking_service import create_booking, cancel_booking
from models import SessionLocal, User
from datetime import datetime

@click.command('create-user')
@click.argument('name')
@click.argument('email')
@click.argument('password')
@click.option('--admin', is_flag=True, help='Flag to create an admin user.')
def create_user_cli(name, email, password, admin):
    """
    CLI command to create a new user.
    """
    session = SessionLocal()
    try:
        user = create_user(session, name, email, password, is_admin=admin)
        click.echo(f"User '{user.name}' created with ID {user.id}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

@click.command('book-room')
@click.argument('user_email')
@click.argument('room_id', type=int)
@click.argument('start_date')
@click.argument('end_date')
def book_room_cli(user_email, room_id, start_date, end_date):
    """
    CLI command to book a room.
    """
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.email == user_email).first()
        if not user:
            click.echo("User not found")
            return
        start = datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.strptime(end_date, '%Y-%m-%d').date()
        booking = create_booking(session, user.id, room_id, start, end)
        click.echo(f"Booking created with ID {booking.id} for Room {room_id}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

@click.command('cancel-booking')
@click.argument('booking_id', type=int)
def cancel_booking_cli(booking_id):
    """
    CLI command to cancel a booking.
    """
    session = SessionLocal()
    try:
        booking = cancel_booking(session, booking_id)
        click.echo(f"Booking ID {booking.id} has been canceled.")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()
