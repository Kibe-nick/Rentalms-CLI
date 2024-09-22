# rentalms.py

import click
from cli.commands import create_user_cli, book_room_cli, cancel_booking_cli

@click.group()
def cli():
    """
    Rental Management System CLI
    """
    pass

# Register CLI commands
cli.add_command(create_user_cli)
cli.add_command(book_room_cli)
cli.add_command(cancel_booking_cli)

if __name__ == '__main__':
    cli()
