# This file loads the llm model

from langchain_community.llms import Ollama
from app.config import MODEL_NAME

def load_llm():  
	""" Load local Ollama model """
	llm = Ollama(model=MODEL_NAME)
	return llm