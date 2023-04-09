#!/usr/bin/env python3
"""
This module will scrape allrecipe website recipe links
and saves it in csv file.
"""

from requests import get
from bs4 import BeautifulSoup
from csv import writer, reader
from time import sleep

ALL_RECIPE_FILE = 'allrecipe_recipe_links.csv'
ALL_CUISINE_FILE = 'allrecipe_world_cuisine.csv'


def get_recipe_links(cuisine_path: str) -> None:
    """This function takes a cuisine link and scrapes recipe links."""
    html = get(cuisine_path).text
    soup = BeautifulSoup(html, 'html.parser')
    recipes = soup.find_all('a', {"class": "mntl-card-list-items"})
    links = [recipe['href'] for recipe in recipes]

    with open(ALL_RECIPE_FILE, 'a+', newline='') as file:
        writing = writer(file)
        writing.writerows([[link] for link in links])


with open(ALL_CUISINE_FILE, 'r', newline='') as file:
    reader_obj = reader(file)
    for line in reader_obj:
        get_recipe_links(line[0])
        sleep(2)
