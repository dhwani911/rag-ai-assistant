# This file performs:
# 1. Search relevant chunks
# 2. Send chunks to LLM
# 3. Generate final answer
from click import prompt

from app.vector_store import get_vector_store
from app.llm import load_llm

def ask_questions(question):
	""" Ask question to RAG pipeline """
	
	# Load Vector database
	vector_db = get_vector_store()

	# Retrive most 3 similar chunks
	docs = vector_db.similarity_search(question, k=3)

	# Combine retrieved chunks into a single context string
	context = "\n\n".join([doc.page_content for doc in docs])
	
	# Create prompt for llm
	prompt = f"Use the context below to answer the question. \n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
	
	# Load llm
	llm = load_llm()
	
	# generate response
	response = llm.invoke(prompt)
	
	return response
	
	
