from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


# --------------------------------------------------
# 1. Embedding model
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 2. Load FAISS vector store
# --------------------------------------------------

vector_store = FAISS.load_local(
    "data/vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)


# --------------------------------------------------
# 3. Create retriever
# --------------------------------------------------

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


# --------------------------------------------------
# 4. Create Ollama LLM
# --------------------------------------------------

llm = ChatOllama(
    model="qwen3:4b",
    temperature=0
)


# --------------------------------------------------
# 5. Create prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are an enterprise company policy assistant.

Answer the user's question using ONLY the context provided below.

If the answer cannot be found in the context, say:
"I don't have enough information in the company documents."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""
)


# --------------------------------------------------
# 6. Helper function
# --------------------------------------------------

def ask_question(question: str):

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    formatted_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(formatted_prompt)

    return response.content
