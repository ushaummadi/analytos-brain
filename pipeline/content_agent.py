from pipeline.hybrid_search import ask
from pipeline.answer_generator import generate_answer


def generate_blog(topic):

    question = f"Write a blog about {topic}"

    answer, context = ask(question)

    prompt = f"""
Using ONLY the approved knowledge below,
write a professional blog.

Requirements:
- Mention at least 3 proof points
- Mention product features
- Mention competitors only if relevant
- Do NOT invent information.
- Do NOT use external knowledge.

Knowledge:

{context}
"""

    blog = generate_answer(prompt, context)

    return blog