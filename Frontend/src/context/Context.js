// Import necessary libraries and hooks
import React, { createContext, useState, useMemo } from "react";

// Create a new context
export const Context = createContext();

// Define the Provider component
export const Provider = ({ children }) => {
    // State for managing messages
    const [messages, setMessages] = useState([]);
    // State for managing the document ID
    const [documentId, setDocumentId] = useState(null);
    // State for managing the document name
    const [documentName, setDocumentName] = useState('');
    // State for managing the loading state
    const [loading, setLoading] = useState(false);
    // State for managing error messages
    const [error, setError] = useState(null);
    // State for caching responses
    const [cache, setCache] = useState({});

    // Function to add a message to the messages state
    const addMessage = (message) => {
        setMessages((prevMessages) => [...prevMessages, message]);
    };

    // Memoize the context value to optimize performance
    const contextValue = useMemo(() => ({
        messages,
        addMessage,
        documentId,
        setDocumentId,
        documentName,
        setDocumentName,
        loading,
        setLoading,
        error,
        setError,
        cache,
        setCache
    }), [messages, documentId, documentName, loading, error, cache]);

    // Return the provider component with the context value
    return (
        <Context.Provider value={contextValue}>
            {children}
        </Context.Provider>
    );
};
