from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings



model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)



sentences = [
    "Employees receive 24 paid leaves per year.",
    "Employees can work from home up to 2 days per week.",
    "Employees must submit leave requests in advance."
]


embeddings = model.encode(sentences)


print("Number of sentences:", len(sentences))
print("Embedding shape:", embeddings.shape)

print("\nFirst embedding:")
print(embeddings[0])