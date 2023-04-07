"""
    This module contains The defination of JamieOliverScraper class
    It is responsile to scrape all recipe information for given recipe url
"""

import requests
from bs4 import BeautifulSoup
import csv


class JamieOliverScraper:
    """ This class is responsible to scrape all necessary data of
        of recipe from given recipe link

        Attributes:
            recipe_url -  link to recipe page

    """

    def __init__(self, url) -> None:
        """Inistiate the class"""
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}

    @staticmethod
    def parse_ingredients(ingredients: list) -> list:
        """Will parse ingredient ul and return list of ingredients"""
        ingredient_list = []
        for ingredient in ingredients:
            text = ingredient.text.strip()
            text_list = text.split()
            ingredient_list.append(' '.join(text_list))
        return ingredient_list

    def get_html(self) -> str:
        """This will get the raw html from given url"""

        html = requests.get(self.url, headers=self.headers)
        return html.text

    def get_data(self) -> dict:
        """This will extract Neccessary data"""

        text = self.get_html()
        soup = BeautifulSoup(text, 'html.parser')
        data = {}
        data['recipe_name'] = soup.find(
            'h3', {'class': 'single-recipe-title'}).text.strip()
        data['recipe_image_url'] = soup.find('img').get('src')
        ingredients = soup.select('ul.ingred-list li')
        data['ingredients'] = self.parse_ingredients(ingredients)
        direction = soup.select('ol.recipeSteps li')
        data['instructions'] = [dire.text.strip() for dire in direction]

        return data
