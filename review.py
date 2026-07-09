import shutil
import subprocess
def get_branch_diff(branch):

    if shutil.which("omnigraph") is None:
        return """
Omnigraph is unavailable on Streamlit Cloud.

Demo Branch:
---------------------

+ Product: Stockly
+ Feature: Demand Forecasting
+ Feature: Inventory Planning
+ Customer: Walmart
+ Customer: Target
+ Proof Point: Reduced stockouts by 35%
"""

    result = subprocess.run(
        [
            "omnigraph",
            "diff",
            "--store",
            "graph.omni",
            "--from",
            "main",
            "--to",
            branch,
        ],
        capture_output=True,
        text=True,
    )

    return result.stdout
def merge_branch(branch):

    if shutil.which("omnigraph") is None:
        return "Branch merged successfully (Demo Mode)."

    result = subprocess.run(
        [
            "omnigraph",
            "branch",
            "merge",
            branch,
            "--store",
            "graph.omni",
        ],
        capture_output=True,
        text=True,
    )

    return result.stdout
def delete_branch(branch):

    if shutil.which("omnigraph") is None:
        return "Branch rejected (Demo Mode)."

    result = subprocess.run(
        [
            "omnigraph",
            "branch",
            "delete",
            branch,
            "--store",
            "graph.omni",
        ],
        capture_output=True,
        text=True,
    )

    return result.stdout
