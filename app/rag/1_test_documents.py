from pathlib import Path

from langchain_community.document_loaders import TextLoader


file_path = Path("data/documents/company_policies.txt")

loader = TextLoader(
    str(file_path),
    encoding="utf-8"
)

documents = loader.load()

print("Number of documents:", len(documents))

print("\nDocument content:")
print(documents[0].page_content)

print("\nMetadata:")
print(documents[0].metadata)