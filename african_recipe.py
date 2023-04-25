from requests import get
from bs4 import BeautifulSoup
import os
import csv

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          os.pardir)) + "/MealMagic-recipe-recommendation-website/"

print(parent_dir)
RECIPE = os.path.join(parent_dir, 'input', 'final_recipes.csv')

list_of_pages = [
    'https://www.yummymedley.com/category/african-cuisine/',
    'https://www.yummymedley.com/category/african-cuisine/page/2/',
    'https://www.yummymedley.com/category/african-cuisine/page/3/',
    'https://www.yummymedley.com/category/african-cuisine/page/4/',
    'https://www.yummymedley.com/category/african-cuisine/page/5/',
    'https://www.yummymedley.com/category/african-cuisine/page/6/'
]


list_of_recipes = []

def get_recipes_page(url):
    html = get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    list_of_recipe  = soup.find_all('div', class_='post-img')
    hrefs = [div.find('a')['href'] for div in list_of_recipe]
    for link in hrefs:
        list_of_recipes.append(link)


for page in list_of_pages:
    get_recipes_page(page)

count = 0
def collect_recipe_data(url):
    html = get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    if soup.find('div', class_='wprm-recipe'):
        img = soup.find('img', class_='wp-post-image')
        if img is None:
            return
        img = soup.find('img', class_='wp-post-image').get('src')
        recipe_template = soup.find('div', class_='wprm-recipe')
        recipe_name = recipe_template.find('h2').text
        ingredients = [ingr.text for ingr in soup.find_all('li', class_= 'wprm-recipe-ingredient')]
        directions = [instr.text for instr in soup.find_all('div', class_="wprm-recipe-instruction-text")]
    with open(RECIPE, 'a', newline='') as file:
        try:
            writer = csv.writer(file)
            row = [url, recipe_name, img, ingredients, directions]
            writer.writerow(row)
        except UnboundLocalError:
            return


for recipe in list_of_recipes:
    collect_recipe_data(recipe)
