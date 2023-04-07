#!/usr/bin/python3
"""
    This module data_collector function that is responsible
    recipe data and saving it on csv file
"""

import csv
from jamieoliver_recipe_scraper import JamieOliverScraper
import time


RECIPE_LINKS = 'jamie_oliver_recipe_links.csv'
RECIPE = 'jamieoliver_recipes.csv'


def data_collector():
    """
        Collects and save all recipe information of allrecipe
    """
    headers = ["Recipe_link", "Recipe_name", "Recipe_img",
               "Recipe_ingredients", "Recipe_directions"]
    with open(RECIPE_LINKS, 'r', newline='') as file:
        reader = csv.reader(file)
        list_of_links = list(reader)

    with open(RECIPE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        count = 1

        for link in list_of_links:
            obj = JamieOliverScraper(link[0])
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


data_collector()
