# Building a Chatbot with FastAPI and OpenAI

This project demonstrates how to build an interactive chatbot using FastAPI (Python web framework) and OpenAI's API. The chatbot can engage in conversations and provide responses using OpenAI's powerful language models.

## Features

- Interactive web-based chat interface
- Integration with OpenAI's API
- Real-time response generation
- FastAPI backend server
- Simple and clean user interface

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CodeSignal-Learn/course_building-a-chatbot-with-fastapi-and-openai
cd course_building-a-chatbot-with-fastapi-and-openai
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, you need to set up your OpenAI API key. You can do this by exporting it as an environment variable:

For macOS/Linux:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

For Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=your-api-key-here
```

For Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY='your-api-key-here'
```

## Running the Application

1. Start the FastAPI development server:
```bash
cd app
python main.py
```

2. Open your web browser and navigate to:
```
http://localhost:3000
```

## Usage

1. Once the application is running, you'll see a chat interface in your browser
2. Type your message in the input field
3. Press Enter or click the Send button to submit your message
4. The chatbot will process your input and provide a response

## Project Structure

```
.
├── README.md
├── requirements.txt
└── app/
    ├── main.py           # Main FastAPI application
    ├── static/           # Static files (CSS, JS)
    ├── templates/        # HTML templates
    ├── services/         # Business logic services
    ├── controllers/      # Route controllers
    ├── models/          # Data models
    └── data/            # Data storage
```

The project follows an MVC (Model-View-Controller) architecture pattern:
- Controllers: Handle HTTP requests and responses
- Models: Define data structures
- Services: Contain business logic
- Templates: Store HTML views
- Static: Contains CSS, JavaScript, and other static assets