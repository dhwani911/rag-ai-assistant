# This file stores environment variables and project settings.

from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

# Chroma database path
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")

# File path to the PDF document to be ingested
PDF_FILE_PATH = os.getenv("PDF_FILE_PATH")
