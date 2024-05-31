// Import React library
import React from 'react';
// Import custom components
import Header from './components/Header';
import Footer from './components/Footer';
import MainContent from './components/MainContent';
// Import CSS for the App component
import './App.css';

// Define the main App component
function App() {
    return (
        <div className="App">
            {/* Render the Header component */}
            <Header />
            {/* Render the MainContent component */}
            <MainContent />
            {/* Render the Footer component */}
            <Footer />
        </div>
    );
}

// Export the App component as the default export
export default App;
