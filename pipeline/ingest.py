import json
import subprocess
from extract import extract_entities
import os

ROOT_DIR = r"C:\projects\analytos-brain"
os.chdir(ROOT_DIR)

print("WORKING DIR:", os.getcwd())

GRAPH_PATH = "graph.omni"
BRANCH_NAME = "ingest-stockly"


def run_command(command):

    print("\nRUNNING:")
    print(command)

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=isinstance(command, str)
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return result.stdout


def create_branch():

    cmd = [
        "omnigraph",
        "branch",
        "list",
        "--store",
        GRAPH_PATH
    ]

    branches = run_command(cmd)

    if BRANCH_NAME in branches:
        print(f"Branch {BRANCH_NAME} already exists")
        return

    cmd = [
        "omnigraph",
        "branch",
        "create",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)


def product_exists(product_name):

    cmd = [
        "omnigraph",
        "query",
        "find_product",
        "--query",
        "schema/find_product.gq",
        "--params",
        json.dumps({"name": product_name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    output = run_command(cmd)

    return product_name in output


def feature_exists(feature_name):

    cmd = [
        "omnigraph",
        "query",
        "find_feature",
        "--query",
        "schema/find_feature.gq",
        "--params",
        json.dumps({"name": feature_name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    output = run_command(cmd)

    return feature_name in output


def insert_product(product_name):

    cmd = [
        "omnigraph",
        "mutate",
        "add_product",
        "--query",
        "schema/insert_product.gq",
        "--params",
        json.dumps({"name": product_name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)


def insert_feature(feature_name):

    cmd = [
        "omnigraph",
        "mutate",
        "add_feature",
        "--query",
        "schema/insert_feature.gq",
        "--params",
        json.dumps({"name": feature_name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def proofpoint_exists(metric):

    cmd = [
        "omnigraph",
        "query",
        "find_proofpoint",
        "--query",
        "schema/find_proofpoint.gq",
        "--params",
        json.dumps({"metric": metric}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    output = run_command(cmd)

    return metric in output 
def insert_proofpoint(metric):

    cmd = [
        "omnigraph",
        "mutate",
        "add_proofpoint",
        "--query",
        "schema/insert_proofpoint.gq",
        "--params",
        json.dumps({"metric": metric}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def proof_point_exists(metric):

    cmd = [
        "omnigraph",
        "query",
        "find_proof_point",
        "--query",
        "schema/find_proof_point.gq",
        "--params",
        json.dumps({"metric": metric}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    output = run_command(cmd)

    return metric in output
def insert_proof_point(metric):

    cmd = [
        "omnigraph",
        "mutate",
        "add_proof_point",
        "--query",
        "schema/insert_proof_point.gq",
        "--params",
        json.dumps({"metric": metric}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def link_product_proof_point(product, metric):

    cmd = [
        "omnigraph",
        "mutate",
        "link_product_proof_point",
        "--query",
        "schema/link_product_proof_point.gq",
        "--params",
        json.dumps({
            "product": product,
            "metric": metric
        }),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def persona_exists(name):

    cmd = [
        "omnigraph",
        "query",
        "find_persona",
        "--query",
        "schema/find_persona.gq",
        "--params",
        json.dumps({"name": name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    return name in run_command(cmd)
def insert_persona(name):

    cmd = [
        "omnigraph",
        "mutate",
        "add_persona",
        "--query",
        "schema/insert_persona.gq",
        "--params",
        json.dumps({"name": name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def link_persona(product, persona):

    cmd = [
        "omnigraph",
        "mutate",
        "link_product_persona",
        "--query",
        "schema/link_product_persona.gq",
        "--params",
        json.dumps({
            "product": product,
            "persona": persona
        }),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def icp_exists(name):

    cmd = [
        "omnigraph",
        "query",
        "find_icp_segment",
        "--query",
        "schema/find_icp_segment.gq",
        "--params",
        json.dumps({"name": name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    output = run_command(cmd)

    return name in output
def insert_icp(name):

    cmd = [
        "omnigraph",
        "mutate",
        "add_icp_segment",
        "--query",
        "schema/insert_icp_segment.gq",
        "--params",
        json.dumps({"name": name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def link_icp(product, segment):

    cmd = [
        "omnigraph",
        "mutate",
        "link_product_icp",
        "--query",
        "schema/link_product_icp.gq",
        "--params",
        json.dumps({
            "product": product,
            "segment": segment
        }),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def competitor_exists(name):

    cmd = [
        "omnigraph",
        "query",
        "find_competitor",
        "--query",
        "schema/find_competitor.gq",
        "--params",
        json.dumps({"name": name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    output = run_command(cmd)

    return name in output
def insert_competitor(name):

    cmd = [
        "omnigraph",
        "mutate",
        "add_competitor",
        "--query",
        "schema/insert_competitor.gq",
        "--params",
        json.dumps({"name": name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def link_competitor(product, competitor):

    cmd = [
        "omnigraph",
        "mutate",
        "link_product_competitor",
        "--query",
        "schema/link_product_competitor.gq",
        "--params",
        json.dumps({
            "product": product,
            "competitor": competitor
        }),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)
def link_competitor_feature(competitor, feature):

    cmd = [

        "omnigraph",

        "mutate",

        "link_competitor_feature",

        "--query",

        "schema/link_competitor_feature.gq",

        "--params",

        json.dumps({

            "competitor": competitor,

            "feature": feature

        }),

        "--branch",

        BRANCH_NAME,

        "--store",

        GRAPH_PATH

    ]

    run_command(cmd)
def customer_exists(name):

    cmd = [
        "omnigraph",
        "query",
        "find_customer",
        "--query",
        "schema/find_customer.gq",
        "--params",
        json.dumps({"name": name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    output = run_command(cmd)

    return name in output


def insert_customer(name):

    cmd = [
        "omnigraph",
        "mutate",
        "add_customer",
        "--query",
        "schema/insert_customer.gq",
        "--params",
        json.dumps({"name": name}),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)


def link_customer(product, customer):

    cmd = [
        "omnigraph",
        "mutate",
        "link_product_customer",
        "--query",
        "schema/link_product_customer.gq",
        "--params",
        json.dumps({
            "product": product,
            "customer": customer
        }),
        "--branch",
        BRANCH_NAME,
        "--store",
        GRAPH_PATH
    ]

    run_command(cmd)

if __name__ == "__main__":

    data = extract_entities(
        "seed-data/stockly-product-overview.md"
    )

    print("\nEXTRACTED DATA")
    print(json.dumps(data, indent=2))

    create_branch()

    # Product

    if data["product"]:

        if product_exists(data["product"]):
            print(
                f"{data['product']} already exists. Skipping insert."
            )

        else:
            insert_product(data["product"])

    # Features

    for feature in data["features"]:

        if feature_exists(feature):
            print(
                f"{feature} already exists. Skipping insert."
            )

        else:
            insert_feature(feature)
    for metric in data["proof_points"]:

        if proofpoint_exists(metric):
            print(
                f"{metric} already exists. Skipping insert."
            )

        else:
            insert_proofpoint(metric)
    for proof in data["proof_points"]:

        if not proof_point_exists(proof):
            insert_proof_point(proof)

        link_product_proof_point(
            data["product"],
            proof
        )
    for persona in data["personas"]:

        if not persona_exists(persona):
            insert_persona(persona)

        link_persona(data["product"], persona)
    for segment in data["icp_segments"]:

        if not icp_exists(segment):
            insert_icp(segment)

        link_icp(data["product"], segment)
    for competitor in data["competitors"]:

        if not competitor_exists(competitor):
            insert_competitor(competitor)

            link_competitor(
            data["product"],
            competitor
        )
    for competitor in data["competitors"]:

        if not competitor_exists(competitor):
            insert_competitor(competitor)

        link_competitor(data["product"], competitor)
    competitor_features = data.get("competitor_features", {})
    for competitor, features in competitor_features.items():

        for feature in features:

            if not feature_exists(feature):
                insert_feature(feature)

            link_competitor_feature(
                competitor,
                feature
            )
    for customer in data.get("customers", []):
        if not customer_exists(customer):
            insert_customer(customer)

        link_customer(data["product"], customer)
