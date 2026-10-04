from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# --------------------------------------------------
# 1. Load embedding model
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 2. Load existing vector store
# --------------------------------------------------

vector_store = FAISS.load_local(
    "data/vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)


# --------------------------------------------------
# 3. Ask a question
# --------------------------------------------------

question = "How many paid leaves do employees get?"


# --------------------------------------------------
# 4. Search for relevant chunks
# --------------------------------------------------

results = vector_store.similarity_search(
    question,
    k=3
)


# --------------------------------------------------
# 5. Display results
# --------------------------------------------------

print("Question:")
print(question)

print("\nRelevant chunks:")

for i, document in enumerate(results):
    print("\n" + "=" * 60)
    print(f"RESULT {i + 1}")
    print("=" * 60)

    print(document.page_content)

    print("\nMetadata:")
    print(document.metadata)