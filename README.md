# Document Chatbot App

## Introduction

The Document Chatbot App is a web application that allows users to upload PDF documents, ask questions about the content of the documents, and receive answers from a pre-trained model. The app consists of a frontend built with Angular and a backend powered by FastAPI.

## Prerequisites

Before you start, make sure you have the following installed:

- Node.js and npm (for running the Angular app)
- Python 3.7 or higher (for running the FastAPI backend)

## Getting Started

### Frontend (Angular)

1. Navigate to the `pdf-chat-frontend` directory:

```
cd pdf-chat-frontend
```

2. Install dependencies:

```
npm install
```

3. Start the Angular app:

```
ng serve
```

The app will be accessible at `http://localhost:4200`.

### Backend (FastAPI)

1. Navigate to the `pdf-chat` directory:

```
cd pdf-chat
```

2. Create a virtual environment (optional but recommended):

```
python3 -m venv venv
```

3. Activate the virtual environment (if created):

- Windows:

```
venv\Scripts\activate
```

- macOS and Linux:

```
source venv/bin/activate
```

4. Install the required Python packages:

```
pip install -r requirements.txt
```

### Running the FastAPI Backend

1. Start the FastAPI server:

```
uvicorn main:app --reload
```

The backend will be accessible at `http://localhost:8000`.

## Using the App

1. **Sign Up**: Register for an account if you're a new user.

2. **Sign In**: Log in with your credentials.

3. **Chat**: In the chat component, you can:

   - Upload a PDF document.
   - Ask questions about the content of the uploaded document.

4. **Uploading PDFs**: When you upload a PDF, it will be processed by the backend and added to the database.

5. **Asking Questions**: When you ask a question, it will be sent to the backend for processing. The backend will search the database for relevant information and provide an answer.

6. **View Answers**: The answers to your questions will be displayed in the chat component.

## Backend Approach

The backend of the Document Chatbot App is built using FastAPI, a modern, high-performance web framework for building APIs with Python.

### Components and Libraries

1. **Document Processing**:
   - The backend uses `langchain` library for document processing. This includes loading and splitting PDF documents.

2. **Text Embeddings**:
   - `HuggingFaceEmbeddings` is used for generating embeddings of text for further processing.

3. **Vector Stores**:
   - `Chroma` is used as a vector store to efficiently search for similar documents based on their embeddings.

4. **Question Answering**:
   - The app employs a pre-trained model from the Hugging Face Hub (`google/flan-t5-small`) for question-answering.

### API Endpoints

#### 1. Upload PDF

- **URL:** `/upload`
- **Method:** `POST`
- **Request Body:** `multipart/form-data` with the PDF file.
- **Response:**
  - `message`: Indicates whether the upload was successful.
  - `file_name`: The name of the uploaded file.

#### 2. Ask Question

- **URL:** `/answer`
- **Method:** `POST`
- **Request Body:** JSON object with the question.
  - `question`: The question you want to ask.
- **Response:**
  - `answer`: The answer to the question.

## Project Structure

```
document_chatbot
|- pdf-chat
|   |- main.py
|   |- ...
|   |- requirements.txt
|- pdf-chat-frontend
|   |- ...
|   |- package.json
|   |- ...
```

- `pdf-chat`: Contains the FastAPI backend code and requirements.
- `pdf-chat-frontend`: Contains the Angular frontend code.

## Additional Notes

- Make sure the environment variables (e.g., `HUGGINGFACEHUB_API_TOKEN`) are properly set in your environment.

## Support and Issues

If you encounter any issues or have questions about the app, please feel free to open an issue on the [GitHub repository](https://github.com/rt13853/quantivesubmission).

Happy chatting!
