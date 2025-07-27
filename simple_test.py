#!/usr/bin/env python3
"""
Simple test script for Local LLM Agent
Tests basic functionality without complex dependencies.
"""

import sys

def test_basic_imports():
    """Test basic imports."""
    print("🧪 Testing basic imports...")
    
    try:
        from langchain_community.chat_models import ChatOllama
        print("✅ ChatOllama imported successfully")
    except Exception as e:
        print(f"❌ Failed to import ChatOllama: {e}")
        return False
    
    try:
        from langchain_core.prompts import ChatPromptTemplate
        print("✅ ChatPromptTemplate imported successfully")
    except Exception as e:
        print(f"❌ Failed to import ChatPromptTemplate: {e}")
        return False
    
    return True

def test_ollama_connection():
    """Test Ollama connection."""
    print("\n🔗 Testing Ollama connection...")
    
    try:
        from langchain_community.chat_models import ChatOllama
        llm = ChatOllama(model="mistral")
        print("✅ Ollama connection successful")
        return llm
    except Exception as e:
        print(f"❌ Ollama connection failed: {e}")
        return None

def test_basic_chat(llm):
    """Test basic chat functionality."""
    print("\n💬 Testing basic chat...")
    
    try:
        from langchain_core.prompts import ChatPromptTemplate
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Respond with 'Hello from local LLM!'"),
            ("human", "Say hello")
        ])
        
        chain = prompt | llm
        response = chain.invoke({"input": "Say hello"})
        
        print(f"✅ Response received: {response.content[:50]}...")
        return True
        
    except Exception as e:
        print(f"❌ Chat test failed: {e}")
        return False

def main():
    """Run simple tests."""
    print("🧪 Simple Local LLM Agent Test")
    print("=" * 40)
    
    # Test imports
    if not test_basic_imports():
        print("\n❌ Import test failed. Exiting.")
        sys.exit(1)
    
    # Test Ollama connection
    llm = test_ollama_connection()
    if llm is None:
        print("\n❌ Ollama connection failed. Exiting.")
        sys.exit(1)
    
    # Test basic chat
    if not test_basic_chat(llm):
        print("\n❌ Chat test failed. Exiting.")
        sys.exit(1)
    
    print("\n🎉 All tests passed! Your Local LLM Agent is working!")
    print("\nYou can now run:")
    print("  python main.py")
    print("  chainlit run main_chainlit.py")

if __name__ == "__main__":
    main() 