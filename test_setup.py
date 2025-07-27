#!/usr/bin/env python3
"""
Test script for Local LLM Agent
Verifies that the basic components are working correctly.
"""

import sys
import os

def test_imports():
    """Test if all required packages can be imported."""
    print("🧪 Testing imports...")
    
    try:
        from langchain_community.chat_models import ChatOllama
        print("✅ langchain_community.chat_models imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import langchain_community.chat_models: {e}")
        return False
    
    try:
        from langchain_core.prompts import ChatPromptTemplate
        print("✅ langchain_core.prompts imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import langchain_core.prompts: {e}")
        return False
    
    try:
        from langchain_community.document_loaders import PyPDFLoader
        print("✅ langchain_community.document_loaders imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import langchain_community.document_loaders: {e}")
        return False
    
    try:
        from langchain_text_splitters import CharacterTextSplitter
        print("✅ langchain_text_splitters imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import langchain_text_splitters: {e}")
        return False
    
    try:
        from langchain_community.vectorstores import FAISS
        print("✅ langchain_community.vectorstores imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import langchain_community.vectorstores: {e}")
        return False
    
    try:
        from langchain_community.embeddings import OllamaEmbeddings
        print("✅ langchain_community.embeddings imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import langchain_community.embeddings: {e}")
        return False
    
    try:
        from langchain.chains import RetrievalQA
        print("✅ langchain.chains imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import langchain.chains: {e}")
        return False
    
    try:
        import chainlit as cl
        print("✅ chainlit imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import chainlit: {e}")
        return False
    
    return True

def test_ollama_connection():
    """Test if Ollama is running and accessible."""
    print("\n🔗 Testing Ollama connection...")
    
    try:
        from langchain_community.chat_models import ChatOllama
        llm = ChatOllama(model="mistral")
        print("✅ Ollama connection successful")
        return True
    except Exception as e:
        print(f"❌ Ollama connection failed: {e}")
        print("💡 Make sure Ollama is running: ollama serve")
        print("💡 Make sure you have the mistral model: ollama pull mistral")
        return False

def test_basic_functionality():
    """Test basic LLM functionality."""
    print("\n🤖 Testing basic LLM functionality...")
    
    try:
        from langchain_community.chat_models import ChatOllama
        from langchain_core.prompts import ChatPromptTemplate
        
        llm = ChatOllama(model="mistral")
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Respond with 'Hello from local LLM!'"),
            ("human", "Say hello")
        ])
        
        chain = prompt | llm
        response = chain.invoke({"input": "Say hello"})
        
        if "hello" in response.content.lower():
            print("✅ Basic LLM functionality working")
            return True
        else:
            print(f"❌ Unexpected response: {response.content}")
            return False
            
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def test_file_structure():
    """Test if all required files exist."""
    print("\n📁 Testing file structure...")
    
    required_files = [
        "main.py",
        "main_chainlit.py", 
        "pdf_analyzer.py",
        "requirements.txt",
        "README.md",
        "setup.py"
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing files: {', '.join(missing_files)}")
        return False
    
    return True

def main():
    """Run all tests."""
    print("🧪 Local LLM Agent - Test Suite")
    print("=" * 50)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Package Imports", test_imports),
        ("Ollama Connection", test_ollama_connection),
        ("Basic Functionality", test_basic_functionality)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print(f"\n{'='*50}")
    print("📊 Test Results Summary")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your Local LLM Agent is ready to use.")
        print("\nNext steps:")
        print("1. Run: python main.py")
        print("2. Or run: chainlit run main_chainlit.py")
        print("3. Or run: python pdf_analyzer.py [your_pdf_file]")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        print("\nCommon solutions:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Start Ollama: ollama serve")
        print("3. Download models: ollama pull mistral")
        print("4. Download embeddings: ollama pull nomic-embed-text")

if __name__ == "__main__":
    main() 