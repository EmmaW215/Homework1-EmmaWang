import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def use_puppeteer_via_claude(url, screenshot_name):
    """
    Ask Claude to use Puppeteer MCP to take a screenshot
    
    Args:
        url: Website URL to visit
        screenshot_name: Name for the screenshot file
    """
    
    prompt = f"""
    Use Puppeteer to go to {url} and capture a full-page screenshot saved as {screenshot_name}.
    
    Please confirm when the screenshot has been taken and saved.
    """
    
    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        # Extract response
        response_text = ""
        for block in message.content:
            if hasattr(block, 'text'):
                response_text += block.text
        
        return response_text
    
    except Exception as e:
        return f"Error: {e}"

# Main execution
if __name__ == "__main__":
    url = "https://www.inference.ai/"
    screenshot_name = "example.png"
    
    print(f"Asking Claude to screenshot {url}...\n")
    print("="*80)
    
    result = use_puppeteer_via_claude(url, screenshot_name)
    print(result)