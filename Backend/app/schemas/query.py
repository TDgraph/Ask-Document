# Import necessary modules from Pydantic
from pydantic import BaseModel

# Define the QuerySchema model
class QuerySchema(BaseModel):
    document_id: int  # ID of the document to query
    question: str  # The question to ask about the document

# Define the AnswerSchema model
class AnswerSchema(BaseModel):
    answer: str  # The answer to the question
