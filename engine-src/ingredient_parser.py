#!/usr/bin/python3
""" This module is responsible for cleaning up data to feed for modeling
"""
import os
import pandas as pd
import ast
import re
import unidecode
from nltk.stem import WordNetLemmatizer

# Define the file paths
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          os.pardir))
RECIPE_LINKS = os.path.join(parent_dir, 'input', 'recipes.csv')
PARSED_RECIPE = os.path.join(parent_dir, 'input', 'parsed_recipe.csv')


def ingredient_parser(ingreds: str) -> str:
    """
    Clean the ingredient data to prepare it for modeling.

    Args:
    ingreds: string, the raw ingredient data

    Returns:
    A cleaned string of parsed ingredients.
    """

    # Define the most common words and measures to remove
    most_common_words = [
        "'1", "'2", 'teaspoon', 'of', 'g', ',', 'cup', 'fresh', "'½",
        'tablespoons', "oil',", 'tablespoon', 'ground', '', 'and', 'or', "'4",
        'red', "'3", "'¼", 'large', 'cups', 'to', 'teaspoons', 'white',
        'cloves', 'bunch', 'olive', "['1", 'black', "chopped',", "salt',",
        'ounce)', "garlic',", 'dried', "pepper',", "sauce',", 'a', "sugar',",
        '½', 'into', "'olive", 'chopped', 'chicken', 'small', 'x', 'cut',
        "taste',", 'green', 'ml', 'finely', "'6", 'vegetable', 'sprigs', "['2",
        "flour',", "vinegar',", 'garlic,', "powder',", "sliced',", 'peeled',
        "tomatoes',", "water',", 'for', 'as', 'virgin', 'pepper', 'from',
        "onions',", "butter',", 'can', 'soy', "seeds',", 'sustainable',
        'pound', 'free-range', "onion',", "cheese',", 'onion,', 'handful',
        'medium', "milk',", 'pinch', 'higher-welfare', "minced',", 'garlic',
        "'extra", "'100", 'heaped', 'minced', "'200", "ginger',", "lemon',",
        "'5", "leaves',", 'all-purpose', 'extra', "'a", 'kg', 'whole'
    ]

    measures = [
        'teaspoon', 't', 'tsp.', 'tablespoon', 'T', 'tbl.', 'tb', 'tbsp.',
        'fluid ounce', 'fl oz', 'gill', 'cup', 'c', 'pint', 'p', 'pt', 'fl pt',
        'quart', 'q', 'qt', 'fl qt', 'gallon', 'g', 'gal', 'ml', 'milliliter',
        'millilitre', 'cc', 'mL', 'l', 'liter', 'litre', 'L', 'dl',
        'deciliter', 'decilitre', 'dL', 'bulb', 'level', 'heaped', 'rounded',
        'whole', 'pinch', 'medium', 'slice', 'pound', 'lb', '#', 'ounce', 'oz',
        'mg', 'milligram', 'milligramme', 'g', 'gram', 'gramme', 'kg',
        'kilogram', 'kilogramme', 'x', 'of', 'mm', 'millimetre', 'millimeter',
        'cm', 'centimeter', 'centimetre', 'm', 'meter', 'metre', 'inch', 'in',
        'milli', 'centi', 'deci', 'hecto', 'kilo'
    ]

    # Lemmatize the most common words and measures
    lemmatizer = WordNetLemmatizer()
    most_common_words = [
        lemmatizer.lemmatize(word) for word in most_common_words
    ]
    measures = [lemmatizer.lemmatize(measure) for measure in measures]

    # Parse the raw ingredient data
    ingreds = ast.literal_eval(ingreds)
    ingred_list = []
    for i in ingreds:
        # Split the ingredient string into individual words
        items = re.split(' |-', i)
        # Remove non-alpha words
        items = [word for word in items if word.isalpha()]
        # Convert all words to lowercase
        items = [word.lower() for word in items]
        # Remove accents
        items = [unidecode.unidecode(word) for word in items]
        # Lemmatize the words
        items = [lemmatizer.lemmatize(word) for word in items]
        # Remove the most common words
        items = [word for word in items if word not in most_common_words]
        # Remove the measures
        items = [word for word in items if word not in measures]
        # Append the cleaned ingredient string to the list
        if items:
            ingred_list.append(' '.join(items))

    # Join the cleaned ingredient strings into a single string
    return " ".join(ingred_list)


if __name__ == "__main__":
    # Read the recipe data into a pandas DataFrame
    df = pd.read_csv(RECIPE_LINKS)
    # Apply the ingredient_parser function to the Recipe_ingredients column
    df['parsed_ingredients'] = df['Recipe_ingredients'].apply(
        ingredient_parser)
    # Select the desired columns
    new_df = df[[
        'Recipe_link', 'Recipe_name', 'Recipe_img', 'Recipe_ingredients',
        'parsed_ingredients', 'Recipe_directions'
    ]]
    # Drop any rows with null values
    new_df = new_df.dropna()
    # Write the cleaned DataFrame to a CSV file
    new_df.to_csv(PARSED_RECIPE, index=False)
