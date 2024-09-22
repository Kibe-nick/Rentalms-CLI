# services/user_service.py
import click
from models.user import User
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(session: Session, name: str, email: str, password: str, is_admin: bool=False) -> User:
    """
    Creates a new user with the provided details.

    :param session: SQLAlchemy session object.
    :param name: Full name of the user.
    :param email: Email address of the user.
    :param password: Plain text password (will be hashed).
    :param is_admin: Boolean flag for admin privileges.
    :return: The created User object.
    """
    if session.query(User).filter(User.email == email).first():
        raise ValueError("A user with this email already exists.")
    
    hashed_password = generate_password_hash(password)  # Hash the password for security
    user = User(name=name, email=email, password=hashed_password, is_admin=is_admin)
    session.add(user)  # Add user to the session
    session.commit()    # Commit the transaction
    session.refresh(user)  # Refresh to get the updated user with ID
    
    click.echo(f"User '{user.name}' created with ID {user.id}") 
    return user

def authenticate_user(session: Session, email: str, password: str) -> User:
    """
    Authenticates a user based on email and password.

    :param session: SQLAlchemy session object.
    :param email: Email address of the user.
    :param password: Plain text password.
    :return: The authenticated User object if credentials are valid.
    :raises: ValueError if authentication fails.
    """
    user = session.query(User).filter(User.email == email).first()
    if user and check_password_hash(user.password, password):
        return user
    else:
        raise ValueError("Invalid email or password")
