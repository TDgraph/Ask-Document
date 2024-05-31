// Import React library
import React from 'react';
// Import custom components
import UploadForm from './UploadForm';
import DocumentNameDisplay from './DocumentNameDisplay';
// Import CSS for the Header component
import '../styles/Header.css';
// Import the logo image
import logo from '../assets/logo.png';  // Adjust the path if necessary

// Define the Header component
function Header() {
    return (
        <header className="header">
            {/* Logo Container */}
            <div className="logo-container">
                {/* Display the logo */}
                <img src={logo} alt="AI Planet Logo" className="logo" />
            </div>
            {/* Upload Container */}
            <div className="upload-container">
                {/* Display the document name */}
                <DocumentNameDisplay />
                {/* Display the upload form */}
                <UploadForm />
            </div>
        </header>
    );
}

// Export the Header component as the default export
export default Header;
