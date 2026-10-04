from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Step 1: Load document
file_path = Path("data/documents/company_policies.txt")

loader = TextLoader(
    str(file_path),
    encoding="utf-8"
)

documents = loader.load()


# Step 2: Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)


# Step 3: Split document
chunks = text_splitter.split_documents(documents)


# Step 4: Display results
print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\n" + "=" * 60)
    print(f"CHUNK {i + 1}")
    print("=" * 60)

    print(chunk.page_content)

    print("\nMetadata:")
    print(chunk.metadata)