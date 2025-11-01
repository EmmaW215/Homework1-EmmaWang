import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY 未设置，请检查 .env")

client = OpenAI(api_key=api_key)

def get_completion(prompt, model="gpt-4o-mini"):
    response = client.responses.create(
        model=model,
        input=prompt,
        temperature=0,
    )
    return response.output[0].content[0].text

prompt = "What is the capital of France?"
response = get_completion(prompt)
print(response)