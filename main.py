#!/usr/bin/env python3
"""
Local LLM Agent - Basic Chat Interface
A simple command-line chat interface using Ollama and LangChain.
"""

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import sys

def setup_llm():
    """Initialize the LLM with Ollama."""
    try:
        # Load the LLM - default to mistral, but you can change this
        llm = ChatOllama(model="mistral")
        print("✅ LLM loaded successfully!")
        return llm
    except Exception as e:
        print(f"❌ Error loading LLM: {e}")
        print("Make sure Ollama is running and you have a model installed.")
        print("Try: ollama run mistral")
        sys.exit(1)

def create_chain(llm):
    """Create the chat chain with prompt template."""
    # Create a system and user prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful, friendly, and knowledgeable assistant. You provide clear, accurate, and helpful responses."),
        ("human", "{input}")
    ])
    
    # Bind the prompt to the model
    chain = prompt | llm
    return chain

def ask_agent(chain, question: str):
    """Send a question to the agent and get a response."""
    try:
        response = chain.invoke({"input": question})
        return response.content
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

def main():
    """Main chat loop."""
    print("🤖 Local LLM Agent - Zero Cloud Costs")
    print("=" * 50)
    print("Loading LLM...")
    
    # Setup
    llm = setup_llm()
    chain = create_chain(llm)
    
    print("\n💬 Chat started! Type 'exit' or 'quit' to end the conversation.")
    print("💡 Try asking questions like:")
    print("   - 'What is machine learning?'")
    print("   - 'Write a Python function to calculate fibonacci numbers'")
    print("   - 'Explain quantum computing in simple terms'")
    print("-" * 50)
    
    # Chat loop
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n👋 Goodbye! Thanks for chatting with your local AI agent!")
                break
            
            print("\n🤖 Assistant: ", end="", flush=True)
            response = ask_agent(chain, user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main() 