from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.allrecipes.com/recipes/86/world-cuisine/?page=2'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
world_cuisine = soup.find_all('a', {"class": "taxonomy-nodes__link"})
cuisines = [cuisine['href'] for cuisine in world_cuisine
            ]

with open('allrecipe_world_cuisine.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([[cuisine] for cuisine in cuisines])
