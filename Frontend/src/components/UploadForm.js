// Import necessary libraries and hooks
import React, { useRef, useContext } from 'react';
// Import the uploadPDF function from the API service
import { uploadPDF } from '../services/api';
// Import the Context for state management
import { Context } from '../context/Context';
// Import CSS for the UploadForm component
import '../styles/UploadForm.css';

// Define the UploadForm component
function UploadForm() {
    // Create a reference to the file input element
    const fileInputRef = useRef(null);
    // Extract context functions for state management
    const { setError, setLoading, setDocumentName, setDocumentId } = useContext(Context);
    // Define the supported file types
    const supportedTypes = ['application/pdf'];

    // Handle the button click to trigger the file input click
    const handleButtonClick = () => {
        fileInputRef.current.click();
    };

    // Handle file change event
    const handleFileChange = async (event) => {
        const file = event.target.files[0];
        if (!file) return;

        // Validate file type
        if (file) {
            if (!supportedTypes.includes(file.type)) {
                setError('Unsupported file type. Please upload a PDF file.');
                return;
            }
            setDocumentName(file.name);
            setError(null);
            setLoading(true);
        }

        // Prepare form data for file upload
        const formData = new FormData();
        formData.append('file', file);


        try {
            // Upload the file using the uploadPDF function
            const response = await uploadPDF(formData);

            // Check if the response contains a document ID
            if (!response.data.document_id) {
                setDocumentName('');
                throw new Error('Failed to upload document');
            }

            // Set the document ID in the context
            setDocumentId(response.data.document_id);

        } catch (error) {
            // Handle errors during file upload
            setError('Failed to upload document. Please try again.');
            console.error('Error uploading document', error);
        } finally {
            // Set loading state to false
            setLoading(false);
        }
    };

    return (
        <div>
            {/* Hidden file input element */}
            <input
                type="file"
                accept="application/pdf"
                ref={fileInputRef}
                style={{ display: 'none' }}
                onChange={handleFileChange}
            />
            {/* Upload button */}
            <button type="button" className="upload-button" onClick={handleButtonClick}>
                <span className="plus-icon">
                    <i className="fas fa-plus-circle"></i>
                </span>
                <span className="upload-text">Upload PDF</span>
            </button>
        </div>
    );
}

// Export the UploadForm component as the default export
export default UploadForm;
