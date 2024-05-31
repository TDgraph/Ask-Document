# Import necessary modules and classes from FastAPI and SQLAlchemy
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Dict

# Import necessary schemas, CRUD operations, and dependencies
from ...schemas.document import DocumentCreate, Document
from ...crud.document import create_document
from app.dependencies import get_db
from ...pdf_operations.storage import save_pdf_file
from ...pdf_operations.extractor import extract_text_from_pdf

# Create an instance of APIRouter
router = APIRouter()

@router.post("/", response_model=Document)
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)) -> Dict[str, any]:
    """
    Endpoint to upload a PDF file, extract text from it, and save the document details to the database.

    Args:
        file (UploadFile): The uploaded PDF file.
        db (Session): The database session.

    Returns:
        JSONResponse: A response containing the filename and document ID.
    """
    

    # Check if the uploaded file is a PDF
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File type not supported.")
    try:
        # Save the uploaded PDF file to the server
        file_path = save_pdf_file(file)
        
        # Extract text from the saved PDF file
        extracted_text = extract_text_from_pdf(file_path)
        
        # Create a document creation schema with the extracted text
        document_create = DocumentCreate(filename=file.filename, text=extracted_text)
        
        # Save the document details to the database
        document = create_document(db, document_create)
        
        # Return a JSON response with the filename and document ID
        return JSONResponse(status_code=200, content={"filename": document.filename, "document_id": document.id})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
