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
        

##Key Components

#Concordance Function

Generates a word frequency count for a given document.

def concordance(document):

con = {}

for word in document.split():

if word in con:

con\[word\] += 1

else:

con\[word\] = 1

return con

##VectorCompare Class

Implements the mathematical operations for vector comparison:

Dot Product: Measures alignment of two vectors.

Magnitude: Calculates the length of a vector.

Cosine Similarity: Combines dot product and magnitudes to compute similarity.

class VectorCompare:

def magnitude(self, concordance):

return math.sqrt(sum(count \*\* 2 for count in concordance.values()))

def relation(self, concordance1, concordance2):

dot\_product = sum(concordance1\[word\] \* concordance2.get(word, 0) for word in concordance1)

mag1 = self.magnitude(concordance1)

mag2 = self.magnitude(concordance2)

return dot\_product / (mag1 \* mag2) if mag1 and mag2 else 0

Example Usage

Create Documents:

documents = {

0: "cat dog cat",

1: "dog bird",

2: "bird cat"

}

##Build an Index:

v = VectorCompare()

index = {doc\_id: v.concordance(doc.lower()) for doc\_id, doc in documents.items()}

Search for a Query:

searchterm = "cat"

search\_con = v.concordance(searchterm.lower())

matches = \[\]

for doc\_id, doc\_con in index.items():

score = v.relation(search\_con, doc\_con)

if score > 0:

matches.append((score, documents\[doc\_id\]))

matches.sort(reverse=True) # Sort by relevance

print(matches)

Output Example: For the query "cat", the output might look like this:

\[(0.894, "cat dog cat"), (0.707, "bird cat")\]

##Key Intuitions for Cosine Similarity

Cosine = 1: The vectors point in the same direction (perfectly similar documents).

Cosine = 0: The vectors are perpendicular (no similarity or overlap).

Cosine = -1: The vectors point in opposite directions (completely dissimilar).

In practical applications, cosine similarity values are typically between 0 and 1 because word counts (frequencies) are non-negative, meaning vectors rarely point in opposite directions.