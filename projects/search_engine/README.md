**Vector Space Search Engine in Python**
========================================

**Overview**
------------

This project is a simple implementation of a **Vector Space Search Engine** using Python. It allows you to compare text documents and search for the most relevant documents given a query. The engine uses **cosine similarity** to measure how similar a query is to each document in the dataset.

**How It Works**
----------------

The engine converts text documents into vectors and compares these vectors using mathematical operations. Here's the step-by-step breakdown:

1.  **Concordance Generation**:
    
    *   A **concordance** is a dictionary that counts how many times each word appears in a document.
        
    *   Example:For the document "cat dog cat", the concordance is: {'cat': 2, 'dog': 1}
        
2.  **Vector Representation**:
    
    *   Each document and query is represented as a vector, where each dimension corresponds to a word.
        
    *   Example:If the words are \["cat", "dog", "bird"\], the document "cat dog cat" becomes the vector:\[2,1,0\]\[2, 1, 0\]\[2,1,0\]
        
3.  **Cosine Similarity**:
    
    *   This measures how similar two vectors are by calculating the cosine of the angle between them.
        
    *   Formula: Cosine Similarity = Dot Product of Vectors / (Magnitude of Vector 1 × Magnitude of Vector 2)
        
4.  **Ranking**:
    
    1.  Each document is scored based on its cosine similarity to the query. Higher scores mean greater relevance.
        
    2.  The results are sorted in descending order of similarity.
        



### **Key Intuitions for Cosine Similarity**

1.  **Cosine = 1**: The vectors point in the **same direction** (perfectly similar documents).
    
2.  **Cosine = 0**: The vectors are **perpendicular** (no similarity or overlap).
    
3.  **Cosine = -1**: The vectors point in **opposite directions** (completely dissimilar).
    

In practical applications, cosine similarity values are typically between **0** and **1** because word counts (frequencies) are non-negative, meaning vectors rarely point in opposite directions.