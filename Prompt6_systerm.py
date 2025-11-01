import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY 未设置，请检查 .env")

client = OpenAI(api_key=api_key)

def get_completion_with_system_prompt(system_prompt, user_prompt, model="gpt-4o-mini"):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

# Define the system and user prompts
system_prompt = "You are a helpful assistant that provides concise and accurate information."
user_prompt = "Can you explain the importance of data privacy?"

response = get_completion_with_system_prompt(system_prompt, user_prompt)
print(response)