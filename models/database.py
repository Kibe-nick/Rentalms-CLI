# models/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your actual database URL
DATABASE_URL = 'sqlite:///database.db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
