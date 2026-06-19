# This file reads PDF documents and stores embeddings.

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.vector_store import get_vector_store

def ingest_pdf(file_path):
	"""
	Reads PDF, splits into chunks, and stores embeddings into ChromaDB.
	"""
	print("Loading PDF...")
	
	# Load PDF document
	loader = PyPDFLoader(file_path)
	documents = loader.load()
	print(f"Loaded {len(documents)} pages")

	for doc in documents[:2]:
		print(doc.metadata)
	print("+"*40)
	
	# Split documents into small chunks
	splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
	chunks = splitter.split_documents(documents)
	print(f"Created {len(chunks)} chunks")

	# Verify chunk content
	print("\nFirst chunk preview:\n")
	print(chunks[0].page_content[:300])
	
	# Store chunks in vector database
	vector_db = get_vector_store()          # Load Vector DB
	vector_db.add_documents(chunks)         # Add chunks to Vector DB
	# vector_db.persist()   			        # Save database
	
	print("Documents successfully ingested")
	return {
		"message": f"Ingested {len(chunks)} chunks"
	}
	