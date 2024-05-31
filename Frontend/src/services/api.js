// Import the axios library for making HTTP requests
import axios from 'axios';

// Create an instance of axios with default settings
const api = axios.create({
    baseURL: process.env.REACT_APP_API_BASE_URL, // Adjust based on your backend URL
    headers: {
        'Content-Type': 'application/json',
    },
});

/**
 * Function to upload a PDF file
 * @param {FormData} formData - The form data containing the PDF file to be uploaded
 * @returns {Promise} - The axios promise for the HTTP request
 */
export const uploadPDF = (formData) => {
    return api.post('/upload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
};

/**
 * Function to ask a question
 * @param {Object} data - The data containing the document ID and the question
 * @returns {Promise} - The axios promise for the HTTP request
 */
export const askQuestion = (data) => {
    return api.post('/query', JSON.stringify(data), {
        headers: {
            'Content-Type': 'application/json',
        },
    });
}

// Export the axios instance as the default export
export default api;
