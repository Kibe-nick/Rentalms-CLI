from modelss.user import User
from services.user_service import create_user, authenticate_user
import pytest

def test_create_user(session):
    """
    Test creating a user and ensuring their details are correctly stored.
    """
    # Create a user
    user = create_user(session, name="Alice Doe", email="alice@example.com", password="password123")
    
    # Check the user was created correctly
    assert user.name == "Alice Doe"
    assert user.email == "alice@example.com"
    assert user.password != "password123"  # Ensure password is hashed
    assert user.is_admin == False  # Default non-admin

def test_authenticate_user(session):
    """
    Test authenticating a user with correct and incorrect credentials.
    """
    # Create a test user
    create_user(session, name="Bob Smith", email="bob@example.com", password="mypassword")

    # Correct credentials should authenticate successfully
    user = authenticate_user(session, email="bob@example.com", password="mypassword")
    assert user.email == "bob@example.com"

    # Incorrect password should raise an error
    with pytest.raises(ValueError, match="Invalid email or password"):
        authenticate_user(session, email="bob@example.com", password="wrongpassword")
    
    # Non-existent email should raise an error
    with pytest.raises(ValueError, match="Invalid email or password"):
        authenticate_user(session, email="nonexistent@example.com", password="mypassword")
