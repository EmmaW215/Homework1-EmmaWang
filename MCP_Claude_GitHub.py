import anthropic
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def use_github_mcp_through_claude(owner, repo, num_commits=5):
    """
    Use Claude API to call GitHub MCP functions
    """
    
    prompt = f"""
    Please use the GitHub MCP integration to:
    1. Access the repository {owner}/{repo}
    2. List the {num_commits} most recent commits
    3. For each commit, provide:
       - Commit SHA (short form)
       - Commit message
       - Author name
       - Date
       - Commit URL
    
    Format the output clearly with numbered items.
    """
    
    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract text response
        response_text = ""
        for block in message.content:
            if hasattr(block, 'text'):
                response_text += block.text
        
        return response_text
    
    except Exception as e:
        return f"Error communicating with Claude: {e}"

if __name__ == "__main__":
    owner = "EmmaW215"
    repo = "n8n"
    
    print(f"Fetching commits from {owner}/{repo} via Claude + GitHub MCP...\n")
    print("="*80)
    
    result = use_github_mcp_through_claude(owner, repo, num_commits=5)
    print(result)