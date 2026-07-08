import subprocess

queries = [
    "get_product_features",
    "get_product_personas",
    "get_product_icps",
    "get_product_competitors",
    "get_product_customers",
]

for q in queries:
    print(f"\n===== {q} =====")
    subprocess.run([
        "omnigraph",
        "query",
        q,
        "--query", f"schema/{q}.gq",
        "--branch", "ingest-stockly",
        "--store", "graph.omni"
    ])