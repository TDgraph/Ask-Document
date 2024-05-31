# Import necessary modules from SQLAlchemy and your application
from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.document import DocumentCreate

def create_document(db: Session, document_create: DocumentCreate) -> Document:
    """
    Create a new document in the database.

    Args:
        db (Session): The database session.
        document_create (DocumentCreate): The document creation schema containing the filename and text.

    Returns:
        Document: The created document object.
    """
    try:
        # Create a new Document instance with the provided data
        db_document = Document(filename=document_create.filename, text=document_create.text)
        
        # Add the document to the database session
        db.add(db_document)
        
        # Commit the transaction to save the document to the database
        db.commit()
        
        # Refresh the session to reflect the new state of the document
        db.refresh(db_document)
        
        # Return the created document
        return db_document
    except Exception as e:
        db.rollback()
        raise Exception(f"Error creating document: {str(e)}")
    

def get_document(db: Session, document_id: int) -> Document:
    """
    Retrieve a document by its ID from the database.

    Args:
        db (Session): The database session.
        document_id (int): The ID of the document to retrieve.

    Returns:
        Document: The retrieved document object or None if not found.
    """
    try:
        # Query the database for the document with the specified ID
        return db.query(Document).filter(Document.id == document_id).first()
    except Exception as e:
        raise Exception(f"Error retrieving document: {str(e)}")

