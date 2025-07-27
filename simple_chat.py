#!/usr/bin/env python3
"""
Simple Local LLM Chat
A basic chat interface using Ollama directly via HTTP requests.
"""

import requests
import json
import sys

def chat_with_ollama(prompt, model="mistral"):
    """Send a prompt to Ollama and get a response."""
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "No response received")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to Ollama: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing response: {e}")
        return None

def main():
    """Main chat loop."""
    print("🤖 Simple Local LLM Chat")
    print("=" * 40)
    print("Loading LLM...")
    
    # Test connection
    test_response = chat_with_ollama("Say 'Hello, I am working!'")
    if test_response is None:
        print("❌ Could not connect to Ollama. Make sure it's running:")
        print("   ollama serve")
        sys.exit(1)
    
    print("✅ LLM loaded successfully!")
    print(f"🤖 Assistant: {test_response}")
    print("\n💬 Chat started! Type 'exit' or 'quit' to end the conversation.")
    print("-" * 40)
    
    # Chat loop
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n👋 Goodbye! Thanks for chatting!")
                break
            
            print("\n🤖 Assistant: ", end="", flush=True)
            response = chat_with_ollama(user_input)
            
            if response:
                print(response)
            else:
                print("Sorry, I encountered an error.")
            
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main() 