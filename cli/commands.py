# cli/commands.py

import click
import sys
import os
from services.apartment_service import create_apartment  
from services.user_service import create_user, authenticate_user
from services.booking_service import create_booking, cancel_booking
from models import SessionLocal, User
from datetime import datetime
# Add the root directory (Rentalms-CLI) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@click.group()
def cli():
    """Rental Management CLI."""
    pass

# Create a new user
@click.command('create-user')
@click.argument('name')
@click.argument('email')
@click.argument('password')
@click.option('--admin', is_flag=True, help='Flag to create an admin user.')
def create_user_cli(name, email, password, admin):
    print("Executing create-user command")
    """
    CLI command to create a new user.
    """
    click.echo("Creating user...")
    session = SessionLocal()
    try:
        user = create_user(session, name, email, password, is_admin=admin)
        click.echo(f"User '{user.name}' created with ID {user.id}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()

#Book a room 
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

# cancel a Booking
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

# Create an Apartment
@click.command('create-apartment')
@click.argument('name')
@click.argument('location')
@click.argument('num_rooms', type=int)

def create_apartment_cli(name, location, num_rooms):
    """CLI command to create a new apartment."""
    click.echo("Creating apartment...")
    session = SessionLocal()
    try:
        apartment = create_apartment(session, name, location, num_rooms)
        click.echo(f"Apartment '{apartment.name}' created with ID {apartment.id}")
    except Exception as e:
        click.echo(f"Error: {e}")
    finally:
        session.close()


# Register the commands
cli.add_command(create_user_cli)
cli.add_command(book_room_cli)
cli.add_command(cancel_booking_cli)
cli.add_command(create_apartment_cli)

if __name__ == '__main__':
    cli()