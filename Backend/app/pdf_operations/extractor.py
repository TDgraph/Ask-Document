# Import the PyMuPDF library
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    try:
        # Initialize an empty string to store the extracted text
        text = ""
        
        # Open the PDF file
        with fitz.open(file_path) as doc:
            # Iterate over each page in the PDF
            for page in doc:
                # Extract text from the page and append it to the text string
                text += page.get_text()
        
        # Return the extracted text
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")
