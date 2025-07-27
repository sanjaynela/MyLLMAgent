# 🤖 Local LLM Agent - Zero Cloud Costs

A fully offline AI agent that runs entirely on your local machine with zero cloud dependency and zero cost.

## 🚀 Quick Start (5 minutes)

### 1. Install Ollama
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows: Download from https://ollama.ai/download
```

### 2. Start Ollama & Download Models
```bash
ollama serve                    # Start Ollama's HTTP server (localhost:11434)
ollama pull mistral            # Main model
ollama pull nomic-embed-text   # For PDF analysis
```

### 3. Set Up Python
```bash
python3 -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Start Using!
```bash
python simple_chat.py          # Simple direct chat (recommended for testing)
python main.py                 # Basic chat with LangChain
chainlit run main_chainlit.py  # Web interface
python pdf_analyzer.py         # PDF analysis
```

## 📋 What This Project Does

This smart local assistant can:
- 💬 Respond to natural language prompts
- 🧠 Use lightweight open-source LLMs
- 🏠 Run entirely on your local machine
- 📄 Read and analyze PDF documents
- 🌐 Provide a web-based chat interface
- 🔧 Offer both simple HTTP and advanced LangChain interfaces

## 🛠️ Usage Examples

### Basic Chat Interface
```bash
python main.py
```
**Example conversation:**
```
👤 You: What is machine learning?
🤖 Assistant: Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed...

👤 You: Write a Python function to calculate fibonacci numbers
🤖 Assistant: Here's a Python function to calculate Fibonacci numbers:
def fibonacci(n):
    if n <= 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)
```

### Simple Direct Chat (No LangChain)
```bash
python simple_chat.py
```
**Features:**
- Direct HTTP communication with Ollama's built-in API
- Lightweight and fast
- No additional dependencies beyond requests
- Perfect for quick testing

**How it works:**
When you run `ollama serve`, Ollama starts a web server on `localhost:11434` that exposes a REST API. The script connects to `http://localhost:11434/api/generate` to send prompts directly to your local LLM.

**Example session:**
```
🤖 Simple Local LLM Chat
========================================
Loading LLM...
✅ LLM loaded successfully!
🤖 Assistant: Hello! I'm here and ready to assist you. How may I help you today?

💬 Chat started! Type 'exit' or 'quit' to end the conversation.
----------------------------------------

👤 You: what is 2+2=
🤖 Assistant: The answer is 4. In basic arithmetic, 2 + 2 equals 4.
```

### LangChain Chat Interface
```bash
python main.py
```
**Features:**
- Uses LangChain framework for advanced LLM interactions
- Prompt templates and system messages
- Better error handling and chain management
- Foundation for more complex AI applications

**How it works:**
LangChain provides a higher-level abstraction over Ollama. Instead of direct HTTP calls, it uses:
- `ChatOllama` class to manage the LLM connection
- `ChatPromptTemplate` for structured prompts
- Chain composition for complex workflows

**Key differences from simple_chat.py:**
- **Simple chat**: Direct HTTP → Ollama API → Response
- **LangChain**: LangChain → ChatOllama → Ollama API → Response

**When to use which:**
- **Use `simple_chat.py`** for quick testing and simple interactions
- **Use `main.py`** for development and when you need LangChain features

### Web Interface
```bash
chainlit run main_chainlit.py
```
Opens a modern web chat interface at `http://localhost:8000`

### PDF Analysis
```bash
python pdf_analyzer.py research_paper.pdf
```
**Example session:**
```
👤 Your question: What is the main research question?
🤔 Question: What is the main research question?
🔍 Searching for answer...
💡 Answer: The main research question investigates the effectiveness of transformer-based models in natural language processing tasks...

👤 Your question: What were the key findings?
💡 Answer: The key findings include: 1) Transformer models show 15% improvement in accuracy...
```

## 📁 Project Structure
```
MyLLMAgent/
├── main.py              # Basic chat interface (LangChain)
├── simple_chat.py       # Simple direct chat (HTTP requests)
├── main_chainlit.py     # Web UI version
├── pdf_analyzer.py      # PDF analysis functionality
├── setup.py            # Automated setup script
├── test_setup.py       # Test suite
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## ⚙️ Advanced Usage

### Using Different Models
```python
# In any of the main files
llm = ChatOllama(model="llama3")  # Instead of "mistral"
```

Available models:
- `mistral` (default, balanced)
- `llama3` (larger, higher quality)
- `phi3` (smaller, faster)
- `codellama` (code-specialized)

### Customizing Prompts
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful coding assistant. Always provide code examples."),
    ("human", "{input}")
])
```

### Batch PDF Processing
```python
import os
from pdf_analyzer import setup_llm, load_pdf, create_vectorstore, create_qa_chain

def process_multiple_pdfs(pdf_directory):
    llm = setup_llm()
    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith('.pdf'):
            # Process each PDF...
```

## 🔧 Troubleshooting

### Common Issues
**"Error loading LLM"**
```bash
ollama serve  # Start Ollama service
```
*This starts Ollama's HTTP server on localhost:11434*

**"Model not found"**
```bash
ollama pull mistral  # Download the model
```

**"Embedding model not found"**
```bash
ollama pull nomic-embed-text  # Download embeddings
```

**"Connection refused" or "Cannot connect to Ollama"**
```bash
# Check if Ollama is running
ps aux | grep ollama

# Restart Ollama service
pkill ollama
ollama serve
```

### Test Your Setup
```bash
python test_setup.py  # Run comprehensive tests
```

## 🎯 Why This Matters

This project demonstrates that powerful AI capabilities are accessible locally without any cloud dependencies:

- ✅ **Zero Cloud Costs** - Everything runs on your machine
- ✅ **Complete Privacy** - No data leaves your computer
- ✅ **No Rate Limits** - Use as much as you want
- ✅ **Always Available** - Works offline
- ✅ **Production Ready** - Can be integrated into real applications

## 🚀 Next Steps

- Try different models with Ollama
- Add more document types (Word, Excel, etc.)
- Implement conversation memory
- Add custom tools and functions
- Integrate into your existing projects

## 📄 License

This project is open source and available under the MIT License.

---

*Built with ❤️ using Ollama, LangChain, and Python* 