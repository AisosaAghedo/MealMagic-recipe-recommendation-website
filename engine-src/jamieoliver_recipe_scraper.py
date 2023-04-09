#!/usr/bin/python3
"""
This module contains the definition of the JamieOliverScraper class,
which is responsible for scraping recipe information from a given URL.
"""

import requests
from bs4 import BeautifulSoup


class JamieOliverScraper:
    """
    This class is responsible for scraping all necessary data of
    a recipe from a given recipe URL.

    Attributes:
        url: A string representing the URL of the recipe page.
    """

    def __init__(self, url: str) -> None:
        """Initialize the class."""
        self.url = url
        self.headers = {
            "User-Agent":
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
        }

    @staticmethod
    def parse_ingredients(ingredients: list) -> list:
        """Parse the ingredient list and return a list of ingredients."""
        ingredient_list = []
        for ingredient in ingredients:
            text = ingredient.text.strip()
            text_list = text.split()
            ingredient_list.append(" ".join(text_list))
        return ingredient_list

    def get_html(self) -> str:
        """Get the raw HTML from the given URL."""
        response = requests.get(self.url, headers=self.headers)
        return response.text

    def get_data(self) -> dict:
        """Extract the necessary data from the recipe page."""
        text = self.get_html()
        soup = BeautifulSoup(text, "html.parser")
        data = {
            "recipe_name":
            soup.find("h3", {
                "class": "single-recipe-title"
            }).text.strip(),
            "recipe_image_url":
            soup.find("img").get("src"),
        }
        ingredients = soup.select("ul.ingred-list li")
        data["ingredients"] = self.parse_ingredients(ingredients)
        directions = soup.select("ol.recipeSteps li")
        data["instructions"] = [
            direction.text.strip() for direction in directions
        ]
        return data
