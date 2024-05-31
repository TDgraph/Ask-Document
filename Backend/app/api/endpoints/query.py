# Import necessary modules and classes from FastAPI and SQLAlchemy
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# Import the get_db dependency for database session management
from app.dependencies import get_db
# Import CRUD functions and schemas
from app.crud.document import get_document
from app.schemas.query import QuerySchema, AnswerSchema
# Import the NLPProcessor service for processing questions
from app.services.nlpprocessor import NLPProcessor

# Create an instance of APIRouter
router = APIRouter()

@router.post("/", response_model=AnswerSchema)
async def answer_query(query: QuerySchema, db: Session = Depends(get_db)) -> AnswerSchema:
    """
    Endpoint to process a question and return an answer based on the document content.
    
    Args:
        query (QuerySchema): The question and document ID.
        db (Session): The database session.

    Returns:
        AnswerSchema: The answer to the question.
    """
    try:
        # Retrieve the document from the database using the provided document ID
        document = get_document(db, document_id=query.document_id)
        
        # If the document is not found, raise a 404 HTTP exception
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")
        
        # Initialize the NLP processor
        nlp_processor = NLPProcessor()
        
        # Process the question using the NLP processor
        answer = nlp_processor.answer_question(pdf_filename=document.filename, question=query.question)
        
        # Return the answer wrapped in the AnswerSchema
        return AnswerSchema(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
