# created from LLM

import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("ratings.csv")

# Create a pivot table of users and items, with ratings as the values
ratings_matrix = df.pivot_table(index='user_id', columns='item_id', values='rating')

# Create a function that calculates the cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

# Create a function that returns the top N similar items to a given item
def get_similar_items(item_id, N=10):
    # Get the item vector
    item_vec = ratings_matrix[item_id]
    
    # Calculate the similarity scores of all other items with the given item
    similarity_scores = ratings_matrix.apply(lambda x: cosine_similarity(item_vec, x), axis=0)
    
    # Sort the similarity scores in descending order
    similarity_scores = similarity_scores.sort_values(ascending=False)
    
    # Return the top N similar items
    return similarity_scores[1:N+1]

# Test the recommendation system
print(get_similar_items(1))




#This recommendation system uses cosine similarity to calculate the similarity between items. It first creates a pivot table of users and items, with ratings as the values. Then, it defines a function that calculates the cosine similarity between two vectors, and another function that returns the top N similar items to a given item.
#To use this recommendation system, you would need to have a dataset of user ratings for different items, in the form of a CSV file. The CSV file should have at least three columns: user_id, item_id, and rating. You would then need to modify the code to read in your own CSV file and use it to create the pivot table.
