// Import necessary libraries and hooks
import React, { useContext, useRef, useEffect } from 'react';
// Import CSS for the Message component
import '../styles/Message.css';
// Import the Context for state management
import { Context } from '../context/Context';

// Define the Message component
function Message() {
    // Extract context values for messages, loading, and error
    const { messages, loading, error } = useContext(Context);
    // Create a reference to the end of the messages
    const messagesEndRef = useRef(null);

    // Scroll to the bottom whenever messages, loading, or error change
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages, loading, error]);

    // Return null if there are no messages
    if (messages.length === 0) return null;

    // Format message text with line breaks
    const formatMessage = (text) => {
        return text.split('\n').map((item, index) => (
            <React.Fragment key={index}>
                {item}
                <br />
            </React.Fragment>
        ));
    };

    return (
        <div className="messages">
            {/* Render each message */}
            {messages.map((msg, index) => (
                <div key={index} className={`message ${msg.sender}`}>
                    <div className="message-content">
                        {/* Display icon based on sender */}
                        {msg.sender === 'bot' && <span className="icon">🤖</span>}
                        <span>{formatMessage(msg.text)}</span>
                        {msg.sender === 'user' && <span className="icon">👤</span>}
                    </div>
                </div>
            ))}
            {/* Render loading indicator */}
            {loading && (
                <div className='message bot'>
                    <div className='message-content'>
                        <span className="icon">🤖</span>
                        <span>Typing.....</span>
                    </div>
                </div>
            )}
            {/* Render error message */}
            {error && (
                <div className='message error'>
                    <div className='message-content'>
                        <span className="icon">🤖</span>
                        <span>{formatMessage(error)}</span>
                    </div>
                </div>
            )}
            {/* Placeholder to ensure scrolling to the bottom */}
            <div ref={messagesEndRef} />
        </div>
    );
}

// Export the Message component as the default export
export default Message;
