# Main FastAPI application

from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_pipeline import ask_questions

# Create FastAPI app instance
app = FastAPI()

class QuestionRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "RAG AI assistant is running"}

@app.post("/ask")
def ask(request: QuestionRequest):
	"""
	API endpoint for asking questions.
	"""
	answer = ask_questions(request.question)
	return {"question": request.question, "answer": answer}

