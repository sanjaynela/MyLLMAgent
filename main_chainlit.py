#!/usr/bin/env python3
"""
Local LLM Agent - Web UI with Chainlit
A modern web-based chat interface using Chainlit, Ollama, and LangChain.
"""

import chainlit as cl
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import asyncio

# Global variables to store the chain
chain = None

@cl.on_chat_start
async def start():
    """Initialize the chat session."""
    global chain
    
    # Show loading message
    await cl.Message(
        content="🤖 Loading your local LLM agent...",
        author="System"
    ).send()
    
    try:
        # Initialize LLM
        llm = ChatOllama(model="mistral")
        
        # Create prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful, friendly, and knowledgeable assistant. You provide clear, accurate, and helpful responses. Always be concise but thorough."),
            ("human", "{input}")
        ])
        
        # Create the chain
        chain = prompt | llm
        
        # Welcome message
        await cl.Message(
            content="✅ Local LLM Agent loaded successfully!\n\n💬 You can now start chatting with your local AI assistant. No cloud costs, no API keys, just pure local processing!",
            author="System"
        ).send()
        
    except Exception as e:
        await cl.Message(
            content=f"❌ Error loading LLM: {e}\n\nMake sure Ollama is running and you have a model installed.\nTry: ollama run mistral",
            author="System"
        ).send()
        return

@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages."""
    global chain
    
    if chain is None:
        await cl.Message(
            content="❌ LLM not initialized. Please restart the chat.",
            author="System"
        ).send()
        return
    
    try:
        # Show typing indicator
        await cl.Message(
            content="🤔 Thinking...",
            author="Assistant"
        ).send()
        
        # Get response from the chain
        response = chain.invoke({"input": message.content})
        
        # Send the response
        await cl.Message(
            content=response.content,
            author="Assistant"
        ).send()
        
    except Exception as e:
        await cl.Message(
            content=f"❌ Sorry, I encountered an error: {e}",
            author="System"
        ).send()

@cl.on_chat_end
async def end():
    """Handle chat end."""
    await cl.Message(
        content="👋 Thanks for using your local LLM agent!",
        author="System"
    ).send() 