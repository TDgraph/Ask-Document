# Import necessary modules
import os
from fastapi import UploadFile

# Define the folder where PDFs will be stored
PDF_STORAGE_FOLDER = "uploaded_pdfs"

# Create the storage folder if it doesn't exist
os.makedirs(PDF_STORAGE_FOLDER, exist_ok=True)

def save_pdf_file(upload_file: UploadFile) -> str:
    """
    Save an uploaded PDF file to the server.

    Args:
        upload_file (UploadFile): The uploaded file.

    Returns:
        str: The path to the saved file.
    """
    try:
        # Construct the file path
        file_path = os.path.join(PDF_STORAGE_FOLDER, upload_file.filename)
        
        # Save the uploaded file to the constructed file path
        with open(file_path, "wb") as file_out:
            file_out.write(upload_file.file.read())
        
        # Return the path to the saved file
        return file_path
    except Exception as e:
        raise Exception(f"Error saving file: {str(e)}")
