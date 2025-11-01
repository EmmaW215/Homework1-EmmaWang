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
John Doe, a 29-year-old software engineer from San Francisco, recently joined OpenAI as a research scientist.
"""

prompt = f"Extract the name and occupation from the following text:\n{text}"
response = get_completion(prompt)
print(response)