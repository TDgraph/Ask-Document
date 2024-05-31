// Import React library
import React from 'react';
// Import ReactDOM for rendering the app
import ReactDOM from 'react-dom/client';
// Import the main App component
import App from './App';
// Import the Provider component from the context
import { Provider } from './context/Context';

// Get the root element from the DOM
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render the App component wrapped with Provider inside React.StrictMode
root.render(
  <React.StrictMode>
    <Provider>
      <App />
    </Provider>
  </React.StrictMode>
);
