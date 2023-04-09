#!/usr/bin/python3
"""
This script recommends recipes based on input ingredients.
"""

import os
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def recommend_recipes(ingredients):
    """
    Recommends recipes based on the input ingredients.

    Args:
        ingredients (str): A comma-separated string of ingredient names.

    Returns:
        list: A list of the top 10 recommended recipe names.
    """

    # Define the file paths
    parent_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir))
    parsed_recipe_file = os.path.join(parent_dir, 'input', 'parsed_recipe.csv')
    model_file = os.path.join(parent_dir, 'input', 'tdidf_model')
    encoding_file = os.path.join(parent_dir, 'input', 'tdidf_encoding')

    # Load the TfidfVectorizer model and encoding
    with open(model_file, 'rb') as file:
        tfidf = pickle.load(file)
    with open(encoding_file, 'rb') as file:
        tfidf_recipe = pickle.load(file)

    # Parse input ingredients and transform into Tfidf vector
    #parsed_ingredients = ingredient_parser("'[" + ingredients + "]'")
    parsed_ingredients = " ".join(ingredients.split(",")).encode('utf-8')
    input_vector = tfidf.transform([parsed_ingredients])

    # Calculate cosine similarity between input vector and all recipe vectors
    cosine_similarities = cosine_similarity(input_vector, tfidf_recipe)

    # Select top 10 recipes with highest cosine similarity and output their names
    recipe_df = pd.read_csv(parsed_recipe_file)
    similar_recipe_indices = np.argsort(cosine_similarities)
    recommended_recipes = recipe_df.iloc[similar_recipe_indices.ravel()]
    recommended_recipes_list = recommended_recipes[['Recipe_name'
                                                    ]].values.tolist()
    return recommended_recipes_list[::-1][:9]
