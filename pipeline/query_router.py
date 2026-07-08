def select_query(question):

    q = question.lower()

    if "competitor" in q:

        return "get_product_competitors"

    elif "customer" in q:

        return "get_product_customers"

    elif "industry" in q:

        return "get_customer_industries"

    elif "persona" in q:

        return "get_product_personas"

    elif "feature" in q:

        if "blue yonder" in q or "netstock" in q:
            return "get_competitor_features"

        return "get_product_features"

    elif "proof" in q or "stockout" in q:

        return "get_product_proof_points"

    elif "icp" in q:

        return "get_product_icps"

    else:

        return "get_products"