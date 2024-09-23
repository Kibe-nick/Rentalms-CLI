# create_db.py
from models.database import engine
from models import Base

def create_database():
    # Create the database tables
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_database()
