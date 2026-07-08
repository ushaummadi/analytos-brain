import subprocess


def get_branch_diff(branch):

    result = subprocess.run(
        [
            "omnigraph",
            "diff",
            "--store",
            "graph.omni",
            "--from",
            "main",
            "--to",
            branch
        ],
        capture_output=True,
        text=True
    )

    return result.stdout
def merge_branch(branch):

    result = subprocess.run(
        [
            "omnigraph",
            "branch",
            "merge",
            branch,
            "--store",
            "graph.omni"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout
def delete_branch(branch):

    result = subprocess.run(
        [
            "omnigraph",
            "branch",
            "delete",
            branch,
            "--store",
            "graph.omni"
        ],
        capture_output=True,
        text=True
    )

    return result.stdout