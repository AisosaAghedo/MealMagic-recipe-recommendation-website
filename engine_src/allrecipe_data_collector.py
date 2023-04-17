#!/usr/bin/python3
"""
This module contains the data_collector function that is responsible
for collecting recipe data and saving it to a CSV file.
"""

import csv
import time
import os
from allrecipe_scraper import AllrecipeScraper

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          os.pardir))
RECIPE_LINKS = os.path.join(parent_dir, 'input', 'allrecipe_recipe_links.csv')
RECIPE = os.path.join(parent_dir, 'input', 'allrecipe_recipes.csv')


def data_collector():
    """
    Collects and saves all recipe information from Allrecipes.
    """
    headers = [
        "Recipe_link", "Recipe_name", "Recipe_img", "Recipe_ingredients",
        "Recipe_directions"
    ]

    with open(RECIPE_LINKS, 'r', newline='') as file:
        reader = csv.reader(file)
        list_of_links = list(reader)

    with open(RECIPE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        count = 1

        for link in list_of_links:
            obj = AllrecipeScraper(link[0])
            data = obj.get_data()
            count += 1
            if count == 10:
                count = 0
                time.sleep(5)

            recipe_link = link[0]
            name = data.get('recipe_name')
            img = data.get('recipe_image_url')
            ingredients = data.get('ingredients')
            directions = data.get('instructions')
            row = [recipe_link, name, img, ingredients, directions]

            writer.writerow(row)


if __name__ == '__main__':
    data_collector()
