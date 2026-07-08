from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)


question = input("Question: ")


docs = db.similarity_search(
    question,
    k=5
)


print("\nRetrieved Context:\n")


for doc in docs:
    print(doc.page_content)
    print("-"*60)