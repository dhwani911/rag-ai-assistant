# This file creates and loads ChromaDB vector database.

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

from app.config import CHROMA_DB_PATH

# Create embedding model
# This model is high in speed and low in memory: https://sbert.net/docs/sentence_transformer/pretrained_models.html#original-models
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")     

def get_vector_store():
	# Returns ChromaDB vector store instance
	vector_db = Chroma(collection_name="rag_collection",embedding_function=embeddings, persist_directory=CHROMA_DB_PATH)
	return vector_db