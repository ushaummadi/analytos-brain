from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from pipeline.answer_generator import generate_answer
from pipeline.query_router import select_query
import shutil
import subprocess

# ----------------------------
# Vector DB Setup
# ----------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)


# ----------------------------
# Graph Search
# ----------------------------

def search_graph(question):

    # If Omnigraph isn't installed (Streamlit Cloud)
    if shutil.which("omnigraph") is None:
        return ""

    query_name = select_query(question)

    try:
        result = subprocess.run(
            [
                "omnigraph",
                "query",
                query_name,
                "--query",
                f"schema/{query_name}.gq",
                "--branch",
                "main",
                "--store",
                "graph.omni",
            ],
            capture_output=True,
            text=True,
        )

        return result.stdout

    except Exception as e:
        return f"Graph error: {e}"
# ----------------------------
# Vector Search
# ----------------------------

def search_vector(question):

    docs = vector_db.similarity_search(
        question,
        k=3
    )

    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    return context


# ----------------------------
# Hybrid Retrieval
# ----------------------------

def hybrid_search(question):

    print("\n🔎 Searching Knowledge Graph...")

    graph_context = search_graph(question)

    print("\n📚 Searching Vector Database...")

    vector_context = search_vector(question)

    final_context = f"""
================ GRAPH INFORMATION ================

{graph_context}

================ DOCUMENT INFORMATION ================

{vector_context}
"""

    return final_context


# ----------------------------
# Ask + Answer
# ----------------------------

def ask(question):

    context = hybrid_search(question)

    answer = generate_answer(question, context)

    return answer, context


# ----------------------------
# Run from terminal only
# ----------------------------

if __name__ == "__main__":

    question = input("Question: ")

    answer, context = ask(question)

    print("\n========== FINAL CONTEXT ==========\n")
    print(context)

    print("\n========== AI ANSWER ==========\n")
    print(answer)
