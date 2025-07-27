#!/usr/bin/env python3
"""
Setup script for Local LLM Agent
Helps users get started quickly with the project.
"""

import subprocess
import sys
import os
import platform

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def check_ollama():
    """Check if Ollama is installed and running."""
    try:
        result = subprocess.run(["ollama", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Ollama is installed: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass
    
    print("❌ Ollama is not installed!")
    print("Please install Ollama first:")
    
    system = platform.system().lower()
    if system == "darwin":  # macOS
        print("   brew install ollama")
    elif system == "linux":
        print("   curl -fsSL https://ollama.ai/install.sh | sh")
    elif system == "windows":
        print("   Download from: https://ollama.ai/download")
    else:
        print("   Visit: https://ollama.ai/download")
    
    return False

def create_virtual_environment():
    """Create a virtual environment."""
    if os.path.exists("venv"):
        print("✅ Virtual environment already exists")
        return True
    
    return run_command("python3 -m venv venv", "Creating virtual environment")

def install_dependencies():
    """Install Python dependencies."""
    # Determine the correct pip command
    if os.name == 'nt':  # Windows
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/macOS
        pip_cmd = "venv/bin/pip"
    
    return run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies")

def download_ollama_models():
    """Download required Ollama models."""
    models = ["mistral", "nomic-embed-text"]
    
    for model in models:
        print(f"🔄 Downloading Ollama model: {model}")
        if not run_command(f"ollama pull {model}", f"Downloading {model}"):
            print(f"⚠️  Warning: Failed to download {model}")
            print(f"   You can download it manually with: ollama pull {model}")

def main():
    """Main setup function."""
    print("🚀 Local LLM Agent Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check Ollama
    if not check_ollama():
        print("\n📋 Please install Ollama first, then run this setup script again.")
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Download Ollama models
    print("\n📥 Downloading Ollama models...")
    download_ollama_models()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    
    print("\n2. Start Ollama service:")
    print("   ollama serve")
    
    print("\n3. Run the basic chat interface:")
    print("   python main.py")
    
    print("\n4. Or run the web interface:")
    print("   chainlit run main_chainlit.py")
    
    print("\n5. To analyze PDFs:")
    print("   python pdf_analyzer.py [path_to_pdf]")
    
    print("\n💡 For more information, see README.md")

if __name__ == "__main__":
    main() 