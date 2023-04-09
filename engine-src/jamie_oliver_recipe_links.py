#!/usr/bin/python3
"""
This script defines a function that scrapes all the recipe links from the Jamie Oliver website
and saves them in a CSV file.
"""

import requests
from bs4 import BeautifulSoup
import re
import csv


def get_jamie_oliver_recipe_links():
    """
    Scrapes all the recipe links from the Jamie Oliver website and saves them in a CSV file.
    """

    url = "https://www.jamieoliver.com/recipes/category/course/mains/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    pattern = re.compile(r"/recipes/([a-z]+-)*recipes/[-a-z]+/")
    all_recipes = [link['href'] for link in soup.find_all('a', href=pattern)]

    all_recipes = [
        f"https://www.jamieoliver.com{recipe}" for recipe in all_recipes
    ]

    with open('recipe_links.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([[recipe] for recipe in all_recipes])


if __name__ == '__main__':
    get_jamie_oliver_recipe_links()
