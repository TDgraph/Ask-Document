# Frontend Ask Doc Project

This is the frontend project for Ask Doc. It is built using React and provides an interface for interacting with the backend services.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Folder Structure](#folder-structure)
- [Available Scripts](#available-scripts)


## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/).

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/TDgraph/Ask-doc
   cd Ask-doc
   ```

2. Install dependencies:

   ```bash
   npm install
   ```
3. Environment Variables:

   To configure environment variables, create a `.env` file in the root directory and add your variables following the format below:

   ```
   REACT_APP_API_BASE_URL=your-backend-api-url
   ```
## Running the Application

To start the development server, run:

```bash
npm start
```

This will run the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits. You will also see any lint errors in the console.

## Folder Structure

Here is a brief overview of the project's folder structure:

```
├── public
│   ├── index.html
│   └── ...
├── src
│   ├── assets
│   │   └── logo.png
│   ├── components
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   ├── MainContent.js
│   │   ├── Message.js
│   │   ├── MessageInput.js
│   │   ├── UploadForm.js
│   │   └── DocumentNameDisplay.js
│   ├── context
│   │   ├── Context.js
│   ├── services
│   │   ├── api.js
│   ├── styles 
│   │   ├── Header.css
│   │   ├── Footer.css
│   │   ├── MainContent.css
│   │   ├── Message.css
│   │   ├── MessageInput.css
│   │   ├── UploadForm.css
│   │   └── DocumentNameDisplay.css
    ├── App.css
│   ├── App.js
│   ├── index.js
│   └── ...
├── .gitignore
├── package.json
└── README.md
```

## Available Scripts

In the project directory, you can run the following scripts:

- `npm start`: Runs the app in the development mode.



Make sure to replace the values with your actual environment variables.

