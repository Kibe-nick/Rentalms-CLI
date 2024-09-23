# models/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Replace with your actual database URL
DATABASE_URL = 'sqlite:///database.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
def create_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_database()