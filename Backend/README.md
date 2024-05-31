# AskDoc

AskDoc is a web application that allows users to upload PDF documents and ask questions about the content of those documents. The application uses FastAPI for the backend, SQLAlchemy for database interactions, and NLP tools for processing and extracting information from the documents.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Application Architecture](#application-architecture)
- [Contributing](#contributing)
- [License](#license)

## Setup Instructions

### Prerequisites

- Python 3.7+
- PostgreSQL
- LangChain/HuggingFace Libraries

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/askdoc.git
   cd askdoc
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install HuggingFace Libraries:

   ```bash
   pip install transformers sentence-transformers
   ```

5. Set up environment variables:

   Create a `.env` file in the root directory and add the following:

   ```env
   DATABASE_HOSTNAME=your_database_hostname
   DATABASE_PORT=your_database_port
   DATABASE_PASSWORD=your_database_password
   DATABASE_USERNAME=your_database_username
   DATABASE_NAME=your_database_name
   HUGGINGFACEHUB_API_TOKEN=your_token
   ```
    Obtain your HUGGINGFACEHUB_API_TOKEN by creating an account on HuggingFace: https://huggingface.co/settings/tokens.


6. Start the application:

   ```bash
   uvicorn app.main:app --reload
   ```

7. Access the application:

   Open your browser and navigate to `http://localhost:8000`.

## API Documentation

### Endpoints

#### Upload PDF

- URL: `/upload`
- Method: `POST`
- Request:
  - `file`: The PDF file to upload.
- Response:
  - `200 OK`: JSON containing `filename` and `document_id`.

#### Ask Question

- URL: `/query`
- Method: `POST`
- Request:
  - `document_id`: The ID of the document.
  - `question`: The question to ask about the document.
- **Response:**
  - `200 OK`: JSON containing `answer`.

## Application Architecture

### Overview

The AskDoc application is structured into several key components:

1. Main Application (`app/main.py`):
   - Initializes the FastAPI app and includes routes.

2. Configuration (`app/config.py`):
   - Uses Pydantic for settings management. Loads environment variables from a `.env` file.

3. Database Models (`app/models`):
   - Defines SQLAlchemy models for the application.

4. CRUD Operations (`app/crud`):
   - Contains functions to perform Create, Read operations on the database.

5. API Endpoints (`app/api/endpoints`):
   - Defines the API routes for uploading PDFs and querying documents.

6. Dependencies (`app/dependencies.py`):
   - Provides dependencies for database sessions.

7. PDF Operations (`app/pdf_operations`):
   - Contains functions for saving PDF files and extracting text from PDFs.

8. NLP Processor (`app/services/nlpprocessor.py`):
   - Uses NLP tools to process and extract information from documents.

### Directory Structure

```
askdoc/
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── query.py
│   │   │   ├── upload.py
│   │   ├── router.py
│   ├── crud/
│   │   ├── document.py
│   ├── models/
│   │   ├── document.py
│   │   ├── base.py
│   ├── pdf_operations/
│   │   ├── extractor.py
│   │   ├── storage.py
│   ├── schemas/
│   │   ├── document.py
│   │   ├── query.py
│   ├── services/
│   │   ├── nlpprocessor.py
│   ├── config.py
│   ├── dependencies.py
│   ├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file further based on your specific project details and requirements.