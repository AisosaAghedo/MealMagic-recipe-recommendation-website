import MySQLdb as mysqldb
import pandas as pd

recipe_df = pd.read_csv('./input/final_recipes.csv')
db_name = "recipe_recommendation"
host = "localhost"
user = "team"
password = "password"

db = mysqldb.connect(host=host, user=user, passwd=password, db=db_name)
cursor = db.cursor()

recipe_data = [
    {
        'recipe_url': row['Recipe_link'],
        'name': row['Recipe_name'],
        'img_url': row['Recipe_img'],
        'ingredients': row['Recipe_ingredients'],
        'directions': row['Recipe_directions'],
    }
    for index, row in recipe_df.iterrows()
]

for data in recipe_data:
    query = "INSERT INTO recipes (name, img_url, ingredients, directions, recipe_url) VALUES (%s, %s, %s, %s, %s)"
    values = [(data['name'], data['img_url'], data['ingredients'], data['directions'], data['recipe_url'])]
    cursor.executemany(query, values)
    db.commit()
    print(f"{data['name']} is inserted successfully!")
    
print("Data inserted successfully")
db.close()
