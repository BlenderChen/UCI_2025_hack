import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

class textToAddress:
    def __init__(self, model_name='all-MiniLM-L6-v2', dataset_path='houses.csv'):
        # Load dataset
        self.df = pd.read_csv(dataset_path, encoding='ISO-8859-1')
        
        # Initialize SentenceTransformer model
        self.model = SentenceTransformer(model_name)
        
        # Encode all house details into vectors
        self.vectors = self.model.encode(self.df['Details'])
    
    def text_to_address(self, input_text):
        """
        Encode the input text to a vector using the SentenceTransformer model.
        """
        input_vector = self.model.encode([input_text])  # Keep input as 2D array
        return input_vector

    def kth_nearest_neighbors(self, input_vector, k=1):
        """
        Find the k nearest neighbors of an input vector from a database of vectors.
        """
        # Compute Euclidean distances
        distances = np.linalg.norm(self.vectors - input_vector, axis=1)
        
        # Get the indices of the k smallest distances
        nearest_indices = np.argsort(distances)[:k]
        
        # Return the indices and distances of the nearest neighbors
        return [(index, distances[index]) for index in nearest_indices]

    def find_nearest_houses(self, input_text, k=3):
        """
        Find the k nearest houses based on user input.
        """
        input_vector = self.text_to_address(input_text)
        nearest_neighbors = self.kth_nearest_neighbors(input_vector, k)
        
        results = []
        for index, distance in nearest_neighbors:
            details = self.df['Details'][index]
            results.append({"Details": details, "Distance": distance})
        
        return results
if __name__ == "__main__":
    # Example usage
    house_search = textToAddress(dataset_path='Houses.csv')
    
    # Get user input
    input_string = input("Enter the details of a house: ")
    
    # Find nearest houses
    k = 3  # Number of nearest neighbors to find
    results = house_search.find_nearest_houses(input_string, k)
    
    print(f"\nTop {k} Nearest Neighbors:\n")
    for result in results:
        print(f"Details: {result['Details']}, Distance: {result['Distance']:.2f}")
