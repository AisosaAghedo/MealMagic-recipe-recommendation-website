#!/usr/bin/python3
"""
    This module contains The defination of AllrecipeScraper class
    This class is responsible to scrape all necessary data from
    allrecipe website

    Author: Yaekob Demisse
"""

import requests
from bs4 import BeautifulSoup
from time import sleep


class AllrecipeScraper:
    """ 
        This class will scrape all necessary data or recipe for allrecipe recipes
        DATA:
            - recipe name
            - recipe image
            - recipe ingridients
            - instructions

        Attr:
            recipe_url: str - the url of the  recipe
    """

    def __init__(self, url) -> None:
        """Initialize the class"""
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}

    def get_html(self) -> str:
        """Get the html of specified url"""
        html = requests.get(self.url)
        text = html.text
        return text

    def get_data(self) -> dict:
        """Scrape necessary data from the html text"""
        html = self.get_html()
        soup = BeautifulSoup(html, 'html.parser')
        data = {}
        data['recipe_name'] = soup.find('h1').text.strip()
        img = soup.find('img')
        data['recipe_image_url'] = img.get('src')
        ingredients = soup.find_all(
            'li', {"class": "mntl-structured-ingredients__list-item"})
        data['ingredients'] = [ingredient.text.strip()
                               for ingredient in ingredients]
        instructions = soup.find_all('p', {"class": "mntl-sc-block-html"})
        data['instructions'] = [instruction.text.strip()
                                for instruction in instructions]

        return data
