from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pypdf
from pathlib import Path


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Replace with the list of allowed origins if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FileUploadResponse(BaseModel):
    message: str
class Question(BaseModel):
    question: str

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

UPLOAD_DIR = Path("uploads")
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Ensure the uploads directory exists
        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        # Save the file locally
        file_path = UPLOAD_DIR / "uploaded_file.pdf"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        return {"message": "File uploaded successfully", "file_name": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

loader = PyPDFLoader("uploads/uploaded_file.pdf")
documents = loader.load_and_split()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
texts = text_splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(texts, embeddings, persist_directory="db")
llm = HuggingFaceHub(
    repo_id="google/flan-t5-small", 
    model_kwargs={"temperature":0.2, "max_length":256}
)

chain = load_qa_chain(llm, chain_type="stuff")
@app.post("/answer/")
async def get_answer(question_data: Question):
    try:
        question = question_data.question        
        docs = db.similarity_search(question)
        answer = chain.run(input_documents=docs, question=question)
        print(answer)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
