// Import React library and useContext hook
import React, { useContext } from 'react';
// Import custom Message component
import Message from './Message';
// Import CSS for the MainContent component
import '../styles/MainContent.css';
// Import Context for state management
import { Context } from '../context/Context';

// Define the MainContent component
function MainContent() {
    // Use useContext to access messages from Context
    const { messages } = useContext(Context);

    return (
        <div className="main-content">
            {/* Render Message component with messages prop */}
            <Message messages={messages} />
        </div>
    );
}

// Export the MainContent component as the default export
export default MainContent;
