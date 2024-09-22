import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Current Python Path:", sys.path)
# Define a fixture for the SQLAlchemy session
@pytest.fixture(scope='function')
def session():
    engine = create_engine('sqlite:///:memory:')  # In-memory SQLite for testing
    Base.metadata.create_all(engine)  # Create all tables
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session  # Provide the session to the test
    
    session.close()  # Cleanup the session
    Base.metadata.drop_all(engine)  # Drop all tables after test
