# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
# Import the Base class from the base module
from .base import Base

# Define the Document model
class Document(Base):
    __tablename__ = 'documents'  # Specify the table name

    # Define the columns of the table
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    filename = Column(String, nullable=False)  # Column to store the filename
    upload_date = Column(DateTime(timezone=True), server_default=func.now())  # Column to store the upload date with a default value
    text = Column(Text, nullable=False)  # Column to store the document text

    # Optionally, define a __repr__ method for better readability in debugging
    """
    def __repr__(self):
        return f"<Document(id={self.id}, filename={self.filename}, upload_date={self.upload_date}, text={self.text})>"
    """
