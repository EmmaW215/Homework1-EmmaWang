import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY 未设置，请检查 .env")
client = anthropic.Anthropic(api_key=api_key)


def get_completion(prompt, model="claude-sonnet-4-20250514", temperature=0):
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        temperature=temperature,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

prompt = "What is the capital of France?"
response = get_completion(prompt)
print(response)