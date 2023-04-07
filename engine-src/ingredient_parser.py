#!/usr/bin/python3
""" This module is responsible for cleaning up data to feed for modeling
"""
import pandas as pd
import ast
import re
import unidecode
from nltk.stem import WordNetLemmatizer
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          os.pardir))
RECIPE_LINKS = os.path.join(parent_dir, 'input', 'recipes.csv')
PARSED_RECIPE = os.path.join(parent_dir, 'input', 'parsed_recipe.csv')


def ingredient_parser(ingreds):
    """ This function will be responsible to clean ingredient data
        Ingredient data is most cruical data to train the model and it should be cleaned
        from common words, stop words and it should be uniform
    """

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

    ingred_list = []
    lemmatizer = WordNetLemmatizer()
    most_common_words = [
        lemmatizer.lemmatize(word) for word in most_common_words
    ]
    measures = [lemmatizer.lemmatize(measure) for measure in measures]
    ingreds = ast.literal_eval(ingreds)
    for i in ingreds:
        items = re.split(' |-', i)
        items = [word for word in items if word.isalpha()]
        # Turn every word to lower case
        items = [word.lower() for word in items]
        # remove accents
        items = [unidecode.unidecode(word) for word in items]
        # lemmatize the words
        items = [lemmatizer.lemmatize(word) for word in items]
        # remove most common words
        items = [word for word in items if word not in most_common_words]
        # remove measuring words
        items = [word for word in items if word not in measures]
        if items:
            ingred_list.append(' '.join(items))

    return " ".join(ingred_list)


if __name__ == "__main__":
    df = pd.read_csv(RECIPE_LINKS)
    df['parsed_ingredients'] = df['Recipe_ingredients'].apply(
        lambda x: ingredient_parser(x))
    new_df = df[[
        'Recipe_link', 'Recipe_name', 'Recipe_img', 'Recipe_ingredients',
        'parsed_ingredients', 'Recipe_directions'
    ]]
    new_df.dropna()
    df.to_csv(PARSED_RECIPE, index=False)
