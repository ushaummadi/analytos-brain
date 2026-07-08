from mcp.server.fastmcp import FastMCP
from pipeline.hybrid_search import ask
from pipeline.query_router import select_query
from policy import check_access
mcp = FastMCP("Analytos Brain")


@mcp.tool()
def ask_question(question: str):
    """
    Ask a question using Hybrid RAG.
    """
    answer, context = ask(question)

    return {
        "question": question,
        "answer": answer,
        "context": context
    }


@mcp.tool()
def graph_query(question: str):
    """
    Return which Omnigraph query will be executed.
    """
    return {
        "query": select_query(question)
    }


@mcp.tool()
def health():
    """
    Health check.
    """
    return {
        "status": "running",
        "server": "Analytos Brain MCP"
    }
@mcp.tool()
def read_product(role: str, question: str):

    if not check_access(role, "Product"):

        return {
            "error": "Access Denied"
        }

    answer, context = ask(question)

    return {
        "answer": answer
    }
@mcp.tool()
def read_email(role: str):

    if not check_access(role, "EmailThread"):

        return {
            "error": "Access Denied"
        }

    return {
        "email": "Internal Email"
    }

if __name__ == "__main__":
    print("=" * 50)
    print("Analytos Brain MCP Server")
    print("=" * 50)
    print("Starting MCP Server...")
    print("Available tools:")
    print(" • ask_question")
    print(" • graph_query")
    print(" • health")
    print("=" * 50)

    mcp.run()