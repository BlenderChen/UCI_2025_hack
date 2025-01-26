import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv('houses.csv')

# Initialize SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode all house details into vectors
vectors = model.encode(df['Details'])

def textToAddress(inputText):
    """
    Encode the input text to a vector using the SentenceTransformer model.
    """
    input_vector = model.encode([inputText])  # Keep input as 2D array
    return input_vector

def get_user_input(prompt="Enter a string: "):
    """
    Requests the user to input a string.
    """
    user_input = input(prompt)
    return user_input

def kth_nearest_neighbors(input_vector, database_vectors, k=1):
    """
    Find the k nearest neighbors of an input vector from a database of vectors.
    """
    # Compute Euclidean distances
    distances = np.linalg.norm(database_vectors - input_vector, axis=1)
    
    # Get the indices of the k smallest distances
    nearest_indices = np.argsort(distances)[:k]
    
    # Return the indices and distances of the nearest neighbors
    return [(index, distances[index]) for index in nearest_indices]

def main():
    # Get user input
    input_string = get_user_input("Enter the details of a house: ")

    # Convert input string to vector
    input_vector = textToAddress(input_string)

    # Find nearest neighbors
    k = 3  # Number of nearest neighbors to find
    nearest_neighbors = kth_nearest_neighbors(input_vector, vectors, k)

    # Print nearest neighbors with details
    print(f"\nTop {k} Nearest Neighbors:\n")
    for index, distance in nearest_neighbors:
        print(f"Details: {df['Details'][index]}, Distance: {distance:.2f}")

if __name__ == "__main__":
    main()
