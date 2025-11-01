import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY 未设置，请检查 .env")

client = OpenAI(api_key=api_key)

def get_completion(prompt, model="gpt-4o-mini"):
       messages = [
           {"role": "system", "content": "You are a helpful assistant knowledgeable in history."},
           {"role": "user", "content": "Who was the first president of the United States?"},
           {"role": "assistant", "content": "George Washington was the first president of the United States."},
           {"role": "user", "content": "When did he take office?"}
       ]
       response = client.chat.completions.create(
           model=model,
           messages=messages,
           temperature=0.7,
       )
       return response.choices[0].message.content

response = get_completion(prompt=None)
print(response)

