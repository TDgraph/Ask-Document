# Import necessary modules and packages
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from .api.router import api_router
from fastapi.middleware.cors import CORSMiddleware
import os
from .models import document
from .database.connection import engine

# Initialize the FastAPI application with a title
app = FastAPI(title="Ask Doc")

# Create all database tables defined in the document model
document.Base.metadata.create_all(bind=engine)

# Define CORS origins
origins = ["*"]

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include the API router
app.include_router(api_router)

# Define the root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Ask Doc!"}

# Custom exception handler for HTTPExceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Custom exception handler for general exceptions
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again later."},
    )
