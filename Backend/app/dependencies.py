# Import the SessionLocal class from the database connection module
from .database.connection import SessionLocal

def get_db():
    """
    Dependency function that provides a database session.

    Yields:
        db (Session): A SQLAlchemy database session.

    Ensures that the database session is closed after the request is handled.
    """
    db = SessionLocal()
    try:
        yield db  # Yield the database session
    finally:
        db.close()  # Ensure the database session is closed
