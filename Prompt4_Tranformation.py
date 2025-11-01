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

text = "The weather is nice today."

prompt = f"Translate the following text to French:\n{text}"
response = get_completion(prompt)
print(response)


prompt = """
Translate the following English phrases to French:

English: Hello
French: Bonjour

English: Thank you
French: Merci

English: Good night
French:

English: Good morning
French:

English: Good afternoon
French:

English: Good evening
French:

English: Goodbye
French:

English: See you later
French:

English: See you tomorrow
French:

English: See you next week
French:

English: See you next month
French:
"""
response = get_completion(prompt)
print(response)