# This file loads the llm model
import os

from langchain_community.llms import Ollama
from app.config import MODEL_NAME
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")

def load_llm():  
	""" Load local Ollama model """
	llm = Ollama(model=MODEL_NAME, base_url=OLLAMA_BASE_URL)
	return llm