from pipeline.hybrid_search import ask
from pipeline.answer_generator import generate_answer


def generate_gtm(product):

    question = f"Who should we prospect for {product}?"

    answer, context = ask(question)

    prompt = f"""
You are a GTM Strategy Agent.

Using ONLY the approved company knowledge below,
generate a GTM Prospecting Brief.

Include:

# Product

# ICP Segments

# Buyer Personas

# Competitor Displacement Angles

# Proof Points

# Target Company Profile

# Example Companies (3)

# Recommended Outreach Message

Do NOT use external knowledge.

Knowledge:

{context}
"""

    return generate_answer(prompt, context)