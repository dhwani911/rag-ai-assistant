# This file performs:
# 1. Search relevant chunks
# 2. Send chunks to LLM
# 3. Generate final answer
import os

from app.vector_store import get_vector_store
from app.llm import load_llm

def ask_questions(question):
	""" Ask question to RAG pipeline """

	# Load Vector database
	vector_db = get_vector_store()

	# Retrive most 3 similar chunks
	docs = vector_db.similarity_search(question, k=3)
	print("\nRetrieved Docs:")

	# Combine retrieved chunks into a single context string
	context = "\n\n".join([doc.page_content for doc in docs])
	
	# Create prompt for llm
	prompt = f"Use the context below to answer the question. \n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
	
	# Load llm
	llm = load_llm()
	
	# generate response
	response = llm.invoke(prompt)

	# Extract sources
	sources = extract_sources(docs)

	return {
		"answer": response,
		"sources": sources
	}

def extract_sources(docs):
	""" Extract sources from retrieved documents from it's metadata """
	seen = set()
	sources = []
	
	for doc in docs:
		meta = doc.metadata
		file_path = meta.get("source", "Unknown")
		file_path = os.path.basename(file_path)
		page = meta.get("page", 0)
		
		# We donot want repeatation of sources and page number in response
		key = (file_path, page)
		if key in seen:
			continue
		seen.add(key)
					
		source_info = {
			"source": file_path,
			"page": page + 1
		}
		sources.append(source_info)
	return sources
	
	
	
