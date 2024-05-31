// Import necessary libraries and hooks
import React, { useContext } from 'react';
// Import the Context for state management
import { Context } from '../context/Context';
// Import CSS for the DocumentNameDisplay component
import '../styles/DocumentNameDisplay.css';

// Define the DocumentNameDisplay component
const DocumentNameDisplay = () => {
    // Use useContext to access documentName from Context
    const { documentName } = useContext(Context);

    // Return null if documentName is not present
    if (!documentName) return null;

    return (
        <div className="doc-display">
            {/* Display document information if documentName is present */}
            <div className="document-info">
                <i className="fas fa-file-pdf"></i>
                <span className="document-name">{documentName}</span>
            </div>
        </div>
    );
}

// Export the DocumentNameDisplay component as the default export
export default DocumentNameDisplay;
