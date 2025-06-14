# Author: Atishay Jain

# app/utils/settings.py
import tempfile
import os
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama

# Model configuration
OLLAMA_MODEL = "llama3.2"

# LLM and Embedding model initialization
embeddings = OllamaEmbeddings(model=OLLAMA_MODEL)
llm = ChatOllama(model=OLLAMA_MODEL)

# Directory setup
UPLOAD_DIR = tempfile.mkdtemp()
DOCUMENTS_DIR = "documents"
os.makedirs(DOCUMENTS_DIR, exist_ok=True)

# Text splitter configuration
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Author: Atishay Jain
