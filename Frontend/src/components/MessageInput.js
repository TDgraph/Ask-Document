// Import necessary libraries and hooks
import React, { useState, useContext } from 'react';
// Import the askQuestion function from the API service
import { askQuestion } from '../services/api';
// Import the Context for state management
import { Context } from '../context/Context';
// Import CSS for the MessageInput component
import '../styles/MessageInput.css';

// Define the MessageInput component
function MessageInput() {
    // State for managing the message input and button state
    const [message, setMessage] = useState('');
    const [isButtonDisabled, setIsButtonDisabled] = useState(true);

    // Extract context values and functions
    const { documentId, setLoading, setError, addMessage, cache, setCache } = useContext(Context);

    // Handle input change event
    const handleChange = (event) => {
        const value = event.target.value;
        setMessage(value);
        setIsButtonDisabled(value.trim() === '');
    };

    // Handle form submit event
    const handleSubmit = async (event) => {
        event.preventDefault();
        if (message.trim()) {
            // Add user's message
            addMessage({ text: message, sender: 'user' });
            setMessage('');
            setLoading(true);
            setError(null);

            // Check cache for existing answer
            if (cache[documentId]?.[message]) {
                addMessage({ sender: 'bot', text: cache[documentId][message] });
                setLoading(false);
                return;
            }

            try {
                // Ask question via API
                const response = await askQuestion({ document_id: documentId, question: message });

                if (!response.data.answer) {
                    throw new Error('Failed to get an answer');
                }

                const answer = response.data.answer;

                // Add bot's answer
                addMessage({ text: answer, sender: 'bot' });
                // Update cache with new answer
                setCache((prevCache) => ({
                    ...prevCache,
                    [documentId]: { ...prevCache[documentId], [message]: answer }
                }));
            } catch (error) {
                setError('Sorry, cannot get an answer for now. Please try again later.');
                console.error('Error asking question', error);
            } finally {
                setLoading(false);
            }
        }
        setIsButtonDisabled(true);
    };

    return (
        <form className="message-form" onSubmit={handleSubmit}>
            <input
                type="text"
                value={message}
                onChange={handleChange}
                placeholder="Send a message..."
                className="message-input"
                disabled={!documentId}
            />
            <button type="submit" className="send-button" disabled={!documentId || isButtonDisabled}>➤</button>
        </form>
    );
}

// Export the MessageInput component as the default export
export default MessageInput;
