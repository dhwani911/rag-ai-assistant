# RAG AI Assistant

A beginner-friendly Retrieval-Augmented Generation (RAG) AI application built using FastAPI, LangChain, ChromaDB, and Ollama.

This project demonstrates how to:

* Ingest PDF documents
* Generate embeddings
* Store embeddings in a vector database
* Perform semantic search
* Query a local Large Language Model (LLM)
* Build AI APIs using FastAPI
* Create a production-ready backend architecture
* Deploy using Docker

---

# Tech Stack

## Backend

* Python 3.11+
* FastAPI
* LangChain
* ChromaDB
* Sentence Transformers
* Ollama

---

# Features

* PDF document ingestion
* Text chunking
* Embedding generation
* Semantic similarity search
* Local LLM integration
* REST API endpoints
* Swagger API documentation
* Docker-ready architecture
* Beginner-friendly project structure

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-ai-assistant.git

cd rag-ai-assistant
```

---

## 2. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Install Ollama from:

* urlOllama Official Website[https://ollama.com](https://ollama.com)

Pull local model:

```bash
ollama run llama3
```

# Running the Project

## Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

### GET /

Response:

```json
{
  "message": "RAG AI Assistant Running"
}
```

---

## Ask Questions

### POST /ask

Request:

```json
{
  "question": "What is this document about?"
}
```

Response:

```json
{
  "question": "What is this document about?",
  "answer": "Generated response from LLM"
}
```

---

# How RAG Works

## Step 1 — PDF Loading

PDF documents are loaded using:

* PyPDFLoader

---

## Step 2 — Text Chunking

Large text is split into smaller chunks using:

* RecursiveCharacterTextSplitter

This improves:

* retrieval quality
* memory efficiency
* LLM context handling

---

## Step 3 — Embedding Generation

Chunks are converted into vector embeddings using:

* all-MiniLM-L6-v2

---

## Step 4 — Vector Storage

Embeddings are stored inside:

* ChromaDB

---

## Step 5 — Semantic Retrieval

When user asks a question:

* similarity search retrieves relevant chunks
* relevant context is sent to the LLM

---

## Step 6 — LLM Response Generation

The retrieved context is passed into:

* Ollama local LLM

which generates the final answer.

---

# Docker Setup

## Build and Run

```bash
docker-compose up --build
```

## Stop

```bash
docker-compose down
```

## Stop the container and remove volumes

```bash
docker-compose down -v
```
This will removes ollama_data volume which is used to store the model data, so use it with caution. Because this will delete all the model data.
Even if that happens, you can pull the model again using `ollama pull llama3` command, but it will take some time to download the model again.

# Learning Outcomes

This project helped in understanding:

* FastAPI backend development
* Retrieval-Augmented Generation (RAG)
* Vector databases
* Embeddings and semantic search
* Local LLM inference
* API development
* AI system debugging
* Docker fundamentals
* Production-ready AI backend architecture

---

# Future Improvements

## Planned Features

* Multi-document ingestion
* Streamlit/React frontend
* Authentication
* PostgreSQL integration
* Redis caching
* Chat history
* CI/CD pipeline
* Monitoring and observability

---

# License

This project is open-source and available for educational purposes.
