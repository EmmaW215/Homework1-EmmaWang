**MCP Automation Test**
MCP Automation Test Results
Completed on: 2025-10-31 20:26:30

Tasks Completed
✓ Brave Search: Searched for 'latest AI paper publication platforms' and retrieved top 3 results
✓ GitHub: Listed 5 latest commits from repository EmmaW215/n8n
✓ Puppeteer: Captured full-page screenshot of https://www.inference.ai/ saved as example.png
✓ Filesystem: Created mcp_test folder on Desktop with hello.txt file containing 'Hello MCP!'
✓ Notion: Created this page to log all automation test results

________________________________________________________________________________________________________

# **Ollama + LangChain + Gradio Integration**

Running on local URL: [http://0.0.0.0:7860](http://0.0.0.0:7860/)

### **📖 How to Use**

**Basic Chat:**

1. Type your message in the text box
2. Press Enter or click "Send 📤"
3. The AI will respond with context from previous messages

**Advanced Features:**

- **System Prompt**: Set a role for the AI (e.g., "You are a Python expert")
- **Clear Chat**: Reset the conversation and start fresh
- **Statistics**: View message count and session info
- **Export**: Save your conversation as JSON

### **💡 Example Queries**

- "Explain machine learning in simple terms"
- "Write a Python function to calculate fibonacci numbers"
- "What's the difference between lists and tuples?"
- "Help me debug this code: [paste code]"

### **🔧 Requirements**

- ✅ Ollama must be running: `ollama serve`
- ✅ Model must be downloaded: `ollama pull llama2`
- ✅ Check available models: `ollama list`

### **🚨 Troubleshooting**

If you see errors:

1. Check Ollama is running: `ps aux | grep ollama`
2. Test Ollama directly: `ollama run llama2 "hello"`
3. Check Ollama status: `curl http://localhost:11434`


<img width="1925" height="882" alt="image" src="https://github.com/user-attachments/assets/8e012dff-f8b8-4da3-bbc3-7dbf02e8fa23" />
