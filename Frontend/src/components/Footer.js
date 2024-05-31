// Import React library
import React from 'react';
// Import custom MessageInput component
import MessageInput from './MessageInput';
// Import CSS for the Footer component
import '../styles/Footer.css';

// Define the Footer component
function Footer() {
    return (
        <footer className="footer">
            {/* Render the MessageInput component */}
            <MessageInput />
        </footer>
    );
}

// Export the Footer component as the default export
export default Footer;
