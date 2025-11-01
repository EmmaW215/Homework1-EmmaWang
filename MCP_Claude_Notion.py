import os
from notion_client import Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_API_KEY"))

def create_notion_page(parent_page_id, title, tasks_content):
    """
    Create a new Notion page with task summary
    
    Args:
        parent_page_id: ID of the parent page (database or page)
        title: Title of the new page
        tasks_content: List of tasks to log
    
    Returns:
        Created page object
    """
    
    try:
        # Create the page - FIX: Remove 'properties' for a child page
        new_page = notion.pages.create(
            parent={"page_id": parent_page_id},
            properties={
                "title": {  # This is for the page title
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            },
            children=[
                # Add heading
                {
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": "MCP Automation Test Results"}
                            }
                        ]
                    }
                },
                # Add timestamp
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": f"Completed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                                },
                                "annotations": {"italic": True}
                            }
                        ]
                    }
                },
                # Add divider
                {
                    "object": "block",
                    "type": "divider",
                    "divider": {}
                },
                # Add tasks heading
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": "Tasks Completed"}
                            }
                        ]
                    }
                }
            ]
        )
        
        # Add each task as a bullet point
        for task in tasks_content:
            notion.blocks.children.append(
                block_id=new_page["id"],
                children=[
                    {
                        "object": "block",
                        "type": "bulleted_list_item",
                        "bulleted_list_item": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {"content": task}
                                }
                            ]
                        }
                    }
                ]
            )
        
        print(f"✓ Notion page created successfully!")
        print(f"✓ Page ID: {new_page['id']}")
        print(f"✓ URL: {new_page['url']}")
        
        return new_page
    
    except Exception as e:
        print(f"✗ Error creating Notion page: {e}")
        return None

def get_parent_page_id_from_url(url):
    """
    Extract page ID from Notion URL
    
    Args:
        url: Notion page URL
    
    Returns:
        Cleaned page ID
    """
    # Extract the ID part from URL
    # Format: https://www.notion.so/Page-Name-1234567890abcdef1234567890abcdef
    if '-' in url:
        page_id = url.split('-')[-1]
        # Remove any query parameters
        page_id = page_id.split('?')[0]
        
        # Format as UUID with hyphens if needed
        if len(page_id) == 32:
            page_id = f"{page_id[:8]}-{page_id[8:12]}-{page_id[12:16]}-{page_id[16:20]}-{page_id[20:]}"
        
        return page_id
    
    return url

# Main execution
if __name__ == "__main__":
    # OPTION 1: Use the full Notion URL
    PARENT_PAGE_URL = "https://www.notion.so/AI-295fc62149ca80aba30ef7e7e75dba5a?source=copy_link"  # Paste your Notion page URL
    
    # Extract page ID from URL
    PARENT_PAGE_ID = get_parent_page_id_from_url(PARENT_PAGE_URL)
    
    # OPTION 2: Or directly use the page ID if you have it
    # PARENT_PAGE_ID = "12345678-1234-1234-1234-123456789abc"  # Replace with actual UUID
    
    print(f"Using parent page ID: {PARENT_PAGE_ID}\n")
    
    # Define tasks
    tasks = [
        "✓ Brave Search: Searched for 'latest AI paper publication platforms' and retrieved top 3 results",
        "✓ GitHub: Listed 5 latest commits from repository EmmaW215/n8n",
        "✓ Puppeteer: Captured full-page screenshot of https://www.inference.ai/ saved as example.png",
        "✓ Filesystem: Created mcp_test folder on Desktop with hello.txt file containing 'Hello MCP!'",
        "✓ Notion: Created this page to log all automation test results"
    ]
    
    print("="*80)
    print("Creating Notion page with MCP test results...")
    print("="*80 + "\n")
    
    page = create_notion_page(
        parent_page_id=PARENT_PAGE_ID,
        title="MCP Automation Test",
        tasks_content=tasks
    )