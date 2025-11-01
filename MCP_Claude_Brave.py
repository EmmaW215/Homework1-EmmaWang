import requests

import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY 未设置，请检查 .env")
client = anthropic.Anthropic(api_key=api_key)

BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")
if not BRAVE_API_KEY:
    raise RuntimeError("BRAVE_API_KEY 未设置，请检查 .env")

def brave_search(query):
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    params = {"q": query}
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Use it
#results = brave_search("latest AI developments")



message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[{
        "role": "user", 
        "content": "Use Brave Search to look up the latest AI paper publication platforms and return the top 3 results with title and link."
    }]
)

print(message.content[0].text)