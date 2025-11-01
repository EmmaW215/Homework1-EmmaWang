import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY 未设置，请检查 .env")

client = OpenAI(api_key=api_key)

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

text = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. It has applications in various fields, including healthcare, finance, and transportation.
"""

prompt = f"Summarize the following text:\n{text}"
response = get_completion(prompt)
print(response)