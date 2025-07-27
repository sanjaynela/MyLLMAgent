#!/usr/bin/env python3
"""
Local LLM Agent - PDF Analyzer
Load PDF documents and answer questions about them using vector search.
"""

from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
import os
import sys

def setup_llm():
    """Initialize the LLM with Ollama."""
    try:
        llm = ChatOllama(model="mistral")
        print("✅ LLM loaded successfully!")
        return llm
    except Exception as e:
        print(f"❌ Error loading LLM: {e}")
        print("Make sure Ollama is running and you have a model installed.")
        print("Try: ollama run mistral")
        sys.exit(1)

def load_pdf(pdf_path):
    """Load and split PDF document."""
    try:
        print(f"📄 Loading PDF: {pdf_path}")
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()
        print(f"✅ Loaded {len(pages)} pages from PDF")
        return pages
    except Exception as e:
        print(f"❌ Error loading PDF: {e}")
        sys.exit(1)

def create_vectorstore(documents):
    """Create vector store from documents."""
    try:
        print("🔧 Creating vector store...")
        
        # Split documents into chunks
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.split_documents(documents)
        print(f"✅ Split into {len(docs)} chunks")
        
        # Create embeddings
        print("🧠 Creating embeddings...")
        embedding = OllamaEmbeddings(model="nomic-embed-text")
        
        # Create vector store
        vectorstore = FAISS.from_documents(docs, embedding)
        print("✅ Vector store created successfully!")
        
        return vectorstore
    except Exception as e:
        print(f"❌ Error creating vector store: {e}")
        print("Note: You may need to install the nomic-embed-text model:")
        print("ollama pull nomic-embed-text")
        sys.exit(1)

def create_qa_chain(llm, vectorstore):
    """Create a retrieval-based QA chain."""
    try:
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm, 
            retriever=retriever,
            return_source_documents=True
        )
        return qa_chain
    except Exception as e:
        print(f"❌ Error creating QA chain: {e}")
        sys.exit(1)

def ask_question(qa_chain, question):
    """Ask a question and get an answer."""
    try:
        print(f"\n🤔 Question: {question}")
        print("🔍 Searching for answer...")
        
        result = qa_chain({"query": question})
        
        print(f"\n💡 Answer: {result['result']}")
        
        # Show source documents if available
        if 'source_documents' in result and result['source_documents']:
            print("\n📚 Sources:")
            for i, doc in enumerate(result['source_documents'][:2], 1):
                page_num = doc.metadata.get('page', 'Unknown')
                print(f"   {i}. Page {page_num}: {doc.page_content[:100]}...")
        
        return result['result']
    except Exception as e:
        print(f"❌ Error getting answer: {e}")
        return None

def interactive_mode(qa_chain):
    """Run interactive question-answering mode."""
    print("\n💬 Interactive PDF Analysis Mode")
    print("=" * 50)
    print("Ask questions about your PDF document.")
    print("Type 'exit' or 'quit' to end the session.")
    print("-" * 50)
    
    while True:
        try:
            question = input("\n👤 Your question: ").strip()
            
            if not question:
                continue
                
            if question.lower() in ["exit", "quit", "bye"]:
                print("\n👋 Goodbye! Thanks for using the PDF analyzer!")
                break
            
            ask_question(qa_chain, question)
            
        except KeyboardInterrupt:
            print("\n\n👋 Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")

def main():
    """Main function."""
    print("📚 Local LLM Agent - PDF Analyzer")
    print("=" * 50)
    
    # Check if PDF file is provided
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        # Look for PDF files in current directory
        pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
        
        if not pdf_files:
            print("❌ No PDF file found!")
            print("Usage: python pdf_analyzer.py [path_to_pdf]")
            print("Or place a PDF file in the current directory.")
            sys.exit(1)
        
        if len(pdf_files) == 1:
            pdf_path = pdf_files[0]
            print(f"📄 Using PDF: {pdf_path}")
        else:
            print("📄 Multiple PDF files found:")
            for i, pdf in enumerate(pdf_files, 1):
                print(f"   {i}. {pdf}")
            choice = input("Select a PDF (number): ").strip()
            try:
                pdf_path = pdf_files[int(choice) - 1]
            except (ValueError, IndexError):
                print("❌ Invalid selection!")
                sys.exit(1)
    
    # Setup
    print("Loading LLM...")
    llm = setup_llm()
    
    # Load PDF
    documents = load_pdf(pdf_path)
    
    # Create vector store
    vectorstore = create_vectorstore(documents)
    
    # Create QA chain
    qa_chain = create_qa_chain(llm, vectorstore)
    
    # Run interactive mode
    interactive_mode(qa_chain)

if __name__ == "__main__":
    main() 