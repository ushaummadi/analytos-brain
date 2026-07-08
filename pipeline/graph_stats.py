import subprocess


def get_count(query_name):
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

        lines = result.stdout.splitlines()

        for line in lines:
            if "rows from branch" in line:
                return int(line.split()[0])

        return 0

    except Exception:
        return 0


def get_graph_stats():
    return {
        "Products": get_count("get_products"),
        "Features": get_count("get_product_features"),
        "Competitors": get_count("get_product_competitors"),
        "Customers": get_count("get_product_customers"),
        "Industries": get_count("get_customer_industries"),
    }