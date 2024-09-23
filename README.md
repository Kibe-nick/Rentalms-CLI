## Rental Management System CLI
The Rental Management System CLI (rentalms-cli) is a command-line interface tool that enables efficient management of rental apartments. Property managers can create users, manage bookings, and cancel reservations. Tenants can book rooms and view their bookings.

## Features
. User creation (including admin users).
. Room booking by tenants.
. Cancel bookings.
. Supports session management using SQLAlchemy for database interactions.

## Prerequisites
Ensure you have the following installed:

. Python: 3.8 or higher
. Pip: Package manager for Python
. PostgreSQL (or any database supported by SQLAlchemy)

## Installation
Follow the steps below to set up the project on your local machine:

1. Clone the repository:

git clone https://github.com/kibe-nick/Rentalms-cli.git

cd Rentalms-cli

2. Create a virtual environment: It's recommended to use a virtual environment to manage dependencies.

``bash
python3 -m venv venv

``bash
source venv/bin/activate  # For Linux/MacOS

``bash
venv\Scripts\activate  # For Windows

3. Install dependencies: Install the necessary Python packages:

``bash
pip install -r requirements.txt

This will install the following key dependencies:

. SQLAlchemy: For ORM and database management.
. Pytest: For running unit tests.
. Click: For building the command-line interface.
. Werkzeug: For password hashing and security.

4. Set up the database: Ensure your database is configured and running. Update the DATABASE_URL in the project’s settings to connect to your PostgreSQL (or preferred) database.

Example .env file:
DATABASE_URL='sqlite:///database.db'

5. Run database migrations: Set up your database schema with the following:

``bash
alembic upgrade head

## Usage
Once installed, you can use the following commands in the CLI:

1. Create a New User: This command creates a new user (optionally as an admin) by providing a name, email, and password.

``bash
python rentalms.py create-user <name> <email> <password> [--admin]

Example:
python rentalms.py create-user "John Doe" "john@example.com" "securepassword" --admin

2. Book a Room: This command allows a user to book a room by specifying their email, the room ID, and the booking duration (start and end dates).

 ``bash
 python rentalms.py  book-room <user_email> <room_id> <start_date> <end_date>

Example:
python rentalms.py  book-room "john@example.com" 101 2024-10-01 2024-10-10

3. Cancel a Booking: Use this command to cancel an existing booking by providing the booking ID.

 ``bash
 python rentalms.py cancel-booking <booking_id>

Example:
python rentalms.py cancel-booking 3

4. Create an Apartment: Use this command to create a new apartment

``bash
python rentalms.py create-apartment <name> <location> <num_rooms>

Example:
python rentalms.py create-apartment "New Apartments" "Nairobi" "12"

## Project Structure
The project is structured as follows:

rentalms-cli/
│
├── cli/
│   └── commands.py   # Click commands for user creation, booking, and canceling bookings.
│
├── services/
│   ├── user_service.py   # Business logic for creating users and authentication.
│   ├── booking_service.py   # Business logic for room bookings and cancellations.
│
├── models
│   ├── __init__.py   
│   ├── user.py
│   ├── apartment.py
│   ├── booking.py
│   └── room.py
├── tests/      # Contains unit tests for the CLI and services.
├── requirements.txt   # Python dependencies.
└── README.md   # Project documentation.

## Dependencies
The following dependencies are required for this project:

. SQLAlchemy: Object-relational mapper for working with relational databases.
. Click: For building CLI commands.
. Pytest: For testing the project and services.
. Werkzeug: For secure password hashing and validation.
. PostgreSQL: (or your preferred SQL database) for data persistence.

To install all dependencies, run:

pip install -r requirements.txt

## Running Tests
The project includes unit tests using Pytest. To run the tests, execute the following command:

pytest

## Contributing
To contribute, fork the repository, create a new branch, and submit a pull request with your changes. Make sure your contributions adhere to the project style guide and are covered by tests.

## Contacts 
Nicholas Korir nickkorir08@gmail.com

