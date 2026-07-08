import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, context):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Answer only using provided context."
            },
            {
                "role": "user",
                "content": f"""
Question:
{question}

Context:
{context}
"""
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content 