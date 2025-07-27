#!/usr/bin/env python3
"""
Create a test PDF file for testing the PDF analyzer.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def create_test_pdf():
    """Create a simple test PDF with sample content."""
    
    # Create PDF
    c = canvas.Canvas("test_document.pdf", pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, height-1*inch, "Sample Research Paper")
    
    # Abstract
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, height-1.5*inch, "Abstract")
    
    c.setFont("Helvetica", 10)
    abstract_text = """
    This paper presents a comprehensive analysis of machine learning algorithms 
    and their applications in natural language processing. We examine various 
    approaches including transformer models, recurrent neural networks, and 
    convolutional neural networks. Our research demonstrates that transformer 
    models achieve superior performance on text classification tasks, with 
    accuracy improvements of up to 15% compared to traditional methods.
    
    The study involved analyzing 10,000 text samples across multiple domains 
    including news articles, scientific papers, and social media posts. Our 
    findings suggest that attention mechanisms play a crucial role in 
    improving model performance, particularly for long-form text processing.
    """
    
    y_position = height-2*inch
    for line in abstract_text.strip().split('\n'):
        c.drawString(1*inch, y_position, line.strip())
        y_position -= 0.2*inch
    
    # Introduction
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y_position-0.5*inch, "Introduction")
    
    c.setFont("Helvetica", 10)
    intro_text = """
    Machine learning has revolutionized the field of natural language processing 
    in recent years. The introduction of transformer architectures has led to 
    significant breakthroughs in text understanding and generation tasks.
    
    This research focuses on comparing different neural network architectures 
    for text classification. We evaluate performance across multiple metrics 
    including accuracy, precision, recall, and F1-score.
    """
    
    y_position -= 1*inch
    for line in intro_text.strip().split('\n'):
        c.drawString(1*inch, y_position, line.strip())
        y_position -= 0.2*inch
    
    # Methodology
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y_position-0.5*inch, "Methodology")
    
    c.setFont("Helvetica", 10)
    method_text = """
    Our methodology involves three main components:
    
    1. Data Preprocessing: We clean and tokenize the text data using 
       standard NLP techniques.
    
    2. Model Training: We train multiple models including BERT, GPT, 
       and traditional RNNs on our dataset.
    
    3. Evaluation: We use cross-validation and holdout sets to ensure 
       robust performance assessment.
    
    The dataset consists of 10,000 documents with balanced class 
    distribution across 5 categories: technology, science, politics, 
    sports, and entertainment.
    """
    
    y_position -= 1.5*inch
    for line in method_text.strip().split('\n'):
        c.drawString(1*inch, y_position, line.strip())
        y_position -= 0.2*inch
    
    # Results
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y_position-0.5*inch, "Results")
    
    c.setFont("Helvetica", 10)
    results_text = """
    Our experimental results show that transformer models significantly 
    outperform traditional approaches:
    
    - BERT: 94.2% accuracy, 0.941 F1-score
    - GPT: 92.8% accuracy, 0.925 F1-score  
    - RNN: 87.3% accuracy, 0.869 F1-score
    
    The transformer models show particular strength in handling 
    long-form text and maintaining context across sentences.
    """
    
    y_position -= 1.5*inch
    for line in results_text.strip().split('\n'):
        c.drawString(1*inch, y_position, line.strip())
        y_position -= 0.2*inch
    
    # Conclusion
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y_position-0.5*inch, "Conclusion")
    
    c.setFont("Helvetica", 10)
    conclusion_text = """
    This study demonstrates the superiority of transformer-based models 
    for text classification tasks. The attention mechanisms in these 
    models enable better understanding of context and relationships 
    between words.
    
    Future work will explore the application of these models to 
    multilingual text processing and real-time classification systems.
    """
    
    y_position -= 1.5*inch
    for line in conclusion_text.strip().split('\n'):
        c.drawString(1*inch, y_position, line.strip())
        y_position -= 0.2*inch
    
    c.save()
    print("✅ Created test_document.pdf successfully!")

if __name__ == "__main__":
    create_test_pdf() 