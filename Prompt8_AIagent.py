from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY 未设置，请检查 .env")

client = OpenAI(api_key=api_key)

# Define available functions
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

# Function to get the model's response
def get_agent_response(user_prompt, model="gpt-4"):
    messages = [{"role": "user", "content": user_prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        functions=[
            {
                "name": "add_numbers",
                "description": "Add two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "The first number"},
                        "b": {"type": "number", "description": "The second number"}
                    },
                    "required": ["a", "b"]
                }
            },
            {
                "name": "subtract_numbers",
                "description": "Subtract two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number", "description": "The first number"},
                        "b": {"type": "number", "description": "The second number"}
                    },
                    "required": ["a", "b"]
                }
            }
        ],
        temperature=0,
    )

    response_message = response.choices[0].message

    if response_message.function_call:
        function_name = response_message.function_call.name
        arguments = json.loads(response_message.function_call.arguments)
        if function_name == "add_numbers":
            result = add_numbers(**arguments)
        elif function_name == "subtract_numbers":
            result = subtract_numbers(**arguments)
        else:
            result = "Function not recognized."
        return result
    else:
        return response_message.content

# Example usage
user_prompt = "What is 15 minus 7?"
response = get_agent_response(user_prompt)
print(response)

user_prompt = "What is 9 plus 7?"
response = get_agent_response(user_prompt)
print(response)

user_prompt = "What is 5 plus 7 minus 13?"
response = get_agent_response(user_prompt)
print(response)
