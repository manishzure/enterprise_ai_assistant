from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# --------------------------------------------------
# 1. Load document
# --------------------------------------------------

file_path = Path("data/documents/company_policies.txt")

loader = TextLoader(
    str(file_path),
    encoding="utf-8"
)

documents = loader.load()


# --------------------------------------------------
# 2. Split document into chunks
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print("Number of chunks:", len(chunks))


# --------------------------------------------------
# 3. Create embedding model
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 4. Create FAISS vector store
# --------------------------------------------------

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)


# --------------------------------------------------
# 5. Save vector store
# --------------------------------------------------

vector_store.save_local(
    "data/vector_store"
)

print("Vector store created successfully!")