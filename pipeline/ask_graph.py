import json
import subprocess
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

question = input("Ask a question: ")

prompt = f"""
You are an assistant.

Choose ONE graph query from this list.

product features
product personas
product icps
product competitors
product customers
competitor features
customer industries

Return ONLY the query name.

Question:
{question}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

query_name = response.choices[0].message.content.strip().lower()

print("Selected Query:", query_name)

# -----------------------------
# Step 3
# -----------------------------

with open("pipeline/graph_queries.json", "r") as f:
    mapping = json.load(f)

if query_name not in mapping:
    print("Query not supported.")
    exit()
graph_query = mapping[query_name]

print("Omnigraph Query:", graph_query)

print("\nRunning Omnigraph...\n")

result = subprocess.run(
    [
        "omnigraph",
        "query",
        graph_query,
        "--query",
        f"schema/{graph_query}.gq",
        "--branch",
        "ingest-stockly",
        "--store",
        "graph.omni"
    ],
    capture_output=True,
    text=True
)

graph_output = result.stdout

print("\n===== GRAPH RESULT =====")
print(graph_output)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": """
You are an AI assistant.

The user asked a question.

You are also given the graph query results.

Answer naturally in plain English.

Do NOT mention Omnigraph or the graph query.
"""
        },
        {
            "role": "user",
            "content": f"""
Question:
{question}

Graph Results:
{graph_output}
"""
        }
    ],
    temperature=0
)

answer = response.choices[0].message.content

print("\n===== AI ANSWER =====")
print(answer)

if result.stderr:
    print(result.stderr)