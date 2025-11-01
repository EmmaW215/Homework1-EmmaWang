import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def use_filesystem_via_claude(task_description):
    """
    Ask Claude to use Filesystem MCP
    
    Args:
        task_description: Description of the filesystem task
    """
    
    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": task_description
                }
            ]
        )
        
        response_text = ""
        for block in message.content:
            if hasattr(block, 'text'):
                response_text += block.text
        
        return response_text
    
    except Exception as e:
        return f"Error: {e}"

# Main execution
if __name__ == "__main__":
    prompt = """
    Use Filesystem to create a folder named mcp_test on my Desktop and add a file 
    hello.txt inside with the text 'Hello MCP!'.
    """
    
    print("Asking Claude to create folder and file...\n")
    print("="*80)
    
    result = use_filesystem_via_claude(prompt)
    print(result)