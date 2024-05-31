# Import necessary modules and classes
import os
import re
from typing import Any, Dict
from langchain.chains import LLMChain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
from langchain.embeddings import HuggingFaceEmbeddings
#from getpass import getpass
from app.config import settings



# Set the HuggingFace API token as an environment variable
os.environ["HUGGINGFACEHUB_API_TOKEN"] = settings.HUGGINGFACEHUB_API_TOKEN

# Define the repository ID for the HuggingFace model
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
# Define the folder where PDFs are stored
PDF_STORAGE_FOLDER = "uploaded_pdfs"

class NLPProcessor:
    def __init__(self):
        # Initialize the language model with the HuggingFace endpoint
        self.llm = HuggingFaceEndpoint(
            repo_id=repo_id, 
            max_length=128, 
            temperature=0.5, 
            token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
        )
        # Define the prompt template for the language model
        self.prompt_template = (
            "Given the following context: {context}\n"
            "Answer the question: {question}.\n"
            "Then, suggest a follow-up question I can ask based on the document."
        )
        self.prompt = ChatPromptTemplate.from_template(self.prompt_template)
    
    def answer_question(self, pdf_filename: str, question: str) -> str:
        """
        Process a question and return an answer based on the document content.
        
        Args:
            pdf_filename (str): The filename of the PDF document.
            question (str): The question to ask.

        Returns:
            str: The answer to the question.
        """
        try:
            # Construct the file path
            file_path = os.path.join(PDF_STORAGE_FOLDER, pdf_filename)
            # Process the PDF to create a vector store
            vectorstore = self.process_pdf(file_path)
            
            # Retrieve relevant documents from the vector store
            retriever = vectorstore.as_retriever()
            retrieved_docs = retriever.get_relevant_documents(question)
            context = " ".join([doc.page_content for doc in retrieved_docs])

            # Create an LLMChain with the prompt and language model
            llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)
            # Invoke the chain with the context and question
            response = llm_chain.invoke({'context': context, 'question': question})
            print(f'The response: {response}')
            res = response['text']

            # Process the response to remove unnecessary text
            processed_response = self.process_response(res)
            return processed_response

        except Exception as e:
            raise Exception(f"Error answering question: {str(e)}")


    def process_response(self, response: str) -> str:
        """
        Process the response from the language model to remove unnecessary text.
        
        Args:
            response (str): The raw response from the language model.

        Returns:
            str: The processed response.
        """
        try:
            # Remove specific substrings from the response
            response = re.sub(r'Answer:', '', response)
            response = re.sub(r'Follow-up question:', '', response)
            response = response.strip()
            return response
        except Exception as e:
            raise Exception(f"Error processing response: {str(e)}")

    def process_pdf(self, file_path: str) -> FAISS:
        """
        Process a PDF document to create a vector store.
        
        Args:
            file_path (str): The path to the PDF document.

        Returns:
            FAISS: The vector store created from the document.
        """
        try:
            # Load the PDF document
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            
            # Split the document into chunks
            text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=300, chunk_overlap=50)
            splits = text_splitter.split_documents(documents)

            # Create embeddings for the document chunks
            embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
            
            return vectorstore
        except Exception as e:
            raise Exception(f"Error processing PDF: {str(e)}")
