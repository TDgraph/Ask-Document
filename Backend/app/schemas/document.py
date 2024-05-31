# Import necessary modules from Pydantic and datetime
from pydantic import BaseModel
from datetime import datetime

# Define the base schema for a document
class DocumentBase(BaseModel):
    filename: str  # Filename of the document

# Define the schema for creating a new document, extending the base schema
class DocumentCreate(DocumentBase):
    text: str  # Extracted text content of the document

# Define the schema for a document stored in the database, extending the base schema
class Document(DocumentBase):
    id: int  # ID of the document
    upload_date: datetime  # Date and time when the document was uploaded
    text: str  # Extracted text content of the document

    # Enable ORM mode to allow compatibility with SQLAlchemy models
    class Config:
        orm_mode = True
