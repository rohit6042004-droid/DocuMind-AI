from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List

from chatbot import ask_question
from utils import format_sources
from services.upload_service import index_uploaded_files
from services.document_service import get_uploaded_documents


app = FastAPI(
    title="DocuMind AI API",
    description="FastAPI backend for DocuMind AI RAG system",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    question: str
    history: str = ""
    selected_document: str = "All Documents"


@app.get("/")
def home():
    return {
        "message": "DocuMind AI API is running"
    }


@app.get("/documents")
def documents():
    return {
        "documents": get_uploaded_documents()
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer, docs = ask_question(
        request.question,
        request.history,
        request.selected_document
    )

    return {
        "answer": answer,
        "sources": format_sources(docs)
    }


@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    chunks_count = index_uploaded_files(files)

    return {
        "message": "Files indexed successfully",
        "chunks_created": chunks_count
    }