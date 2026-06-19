# Main FastAPI application
from fastapi import FastAPI
from pydantic import BaseModel
from app.config import PDF_FILE_PATH
from app.ingest import ingest_pdf
from app.rag_pipeline import ask_questions

# Create FastAPI app instance
app = FastAPI()

class QuestionRequest(BaseModel):
    text: str

@app.on_event("startup")
def startup_event():
    print("Starting document ingestion...")

    ingest_pdf(PDF_FILE_PATH)
	
    print("Document ingestion completed.")
	
@app.get("/")
def home():
    return {"message": "RAG AI assistant is running"}

@app.post("/ask")
def ask(request: QuestionRequest):
	"""
	API endpoint for asking questions.
	"""
	answer = ask_questions(request.text)
	final_answer = answer.replace("\\n", " ").replace("\n", " ").strip()
	return {"question": request.text, "answer": final_answer}
