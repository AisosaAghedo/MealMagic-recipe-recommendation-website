# MealMagic-recipe-recommendation-website
MealMagic is A website that recommends recipes based on different information from the user using a content based filtering recommendation system

# Table of contents
[Installation](#Installation)<br/>
[Usage](#Usage)<br/>
[Features](#Features)<br/>
[Dependencies](#Dependencies)<br/>
[Contact](#Contact)

  
## Installation
```
git clone https://github.com/AisosaAghedo/MealMagic-recipe-recommendation-website
```
## Usage
### To run the backend server
```
MealMagic-recipe-recommendation-website $ export MYSQL_USER=<user> MYSQL_PWD=<password> MYSQL_HOST=localhost  MYSQL_DB=<datatbase> EMAIL_SENDER=<email> EMAIL_PWD=<api_key>

MealMagic-recipe-recommendation-website$ python3 -m api.app
```

### To start up the frontend
```
MealMagic-recipe-recommendation-website/Frontend/mealMagic$ npm i

MealMagic-recipe-recommendation-website/Frontend/mealMagic$ npm run dev
```
## Features
#### The login page
<img src="https://github.com/AisosaAghedo/MealMagic-recipe-recommendation-website/blob/backend_api/assets/Screenshot%20(92).png" alt="login page"/>
#### Available ingredients entered is used to filter dishes matching that specification
<img src="https://github.com/AisosaAghedo/MealMagic-recipe-recommendation-website/blob/backend_api/assets/Screenshot%20(93).png" alt="ingredients page"/>
#### Several dishes made with those igredients are displayed
<img src="https://github.com/AisosaAghedo/MealMagic-recipe-recommendation-website/blob/backend_api/assets/Screenshot%20(94).png" alt="recipes page"/>
#### Detailed instructions on preparation of each meal
<img src="https://github.com/AisosaAghedo/MealMagic-recipe-recommendation-website/blob/backend_api/assets/Screenshot%20(90).png" alt="instructions to prepare meal"/>
We plan to add a password retrieval functionality in the future.
## Dependencies
- HTML
- CSS
- JavaScript
- Python
- Flask
- ReactJs
- Scikit-Learn
- SQLAlchemy
- Gensim
- Pandas
- Numpy
- Mysql
- Mysqldb
- Flask-jwt-extended
- BeautifulSoup
- Requests
