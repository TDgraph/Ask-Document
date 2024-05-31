# Import the APIRouter class from FastAPI
from fastapi import APIRouter
# Import the endpoint modules
from .endpoints import upload, query

# Create an instance of APIRouter
api_router = APIRouter()

# Include the upload router with a prefix and tags
api_router.include_router(upload.router, prefix="/upload", tags=["upload"])

# Include the query router with a prefix and tags
api_router.include_router(query.router, prefix="/query", tags=["query"])
