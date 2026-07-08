from pathlib import Path
import json
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
PROMPT = """
Extract the following information from the document.

Return ONLY valid JSON.

{
  "product":"",
  "features":[],
  "proof_points":[],
  "personas":[],
  "icp_segments":[],
  "competitors":[],
  "competitor_features":{},
  "customers":[],
  "customer_case_studies":{
    "Customer Name":{
      "industry":"",
      "use_case":"",
      "outcome":""
    }
  }
}
"""
def extract_entities(filepath):

    text = Path(filepath).read_text(
        encoding="utf-8"
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        response_format={
            "type": "json_object"
        },
        messages=[
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    print("\n========== RAW LLM RESPONSE ==========")
    print(answer)
    print("======================================")

    try:

        data = json.loads(answer)

    except json.JSONDecodeError:

        print("\nInvalid JSON returned by LLM.")
        print("Returning empty structure.\n")

        data = {}

    defaults = {

        "product": "",

        "features": [],

        "proof_points": [],

        "personas": [],

        "icp_segments": [],

        "competitors": [],

        "competitor_features": {}

    }

    for key, value in defaults.items():

        if key not in data:

            data[key] = value

    print("\n========== NORMALIZED JSON ==========")
    print(json.dumps(data, indent=2))
    print("=====================================\n")

    return data


if __name__ == "__main__":

    result = extract_entities(
        "seed-data/stockly-product-overview.md"
    )

    print("\n========== FINAL RESULT ==========")
    print(json.dumps(result, indent=2))