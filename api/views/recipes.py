#!/usr/bin/python3
"""
api endpoints for recipes model
"""
from . import User, Recipe, app_views, storage
from flask import abort, jsonify, request
#from recommender import recommend_recipes

@app_views("/users/<user_id>/recipes", methods=['GET', 'POST'], strict_slashes=False)
def saved_recipes(user_id):
    """ GET: gets all recipes by a user
    POST: adds a new recipe for a user"""

    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    if request.method == 'GET':
        saved_recipes = []

        for recipe in user.saved_recipes:
            saved_recipes.append(recipe.to_dict())
        return jsonify(saved_recipes)
    
    else:
        req = request.get_json()
        
        if req is None:
            abort(400, description="Not a json")
        if req.get('name') is None:
            abort(400, description='Missing name')
        if req.get('id'):
            del req['id']

        recipe = storage.get(Recipe, None, req.get('name'))
        if recipe is None:
            recipe = Recipe(**req)
            user.saved_recipes.append(recipe)
        else:
            recipe.users.append(user)
        recipe.save()
        return jsonify(recipe.to_dict()), 201


@app_views('/get_recipes', strict_slashes=False)
def find_recipe():
    """
    finds recipe from db using passed name in json
    """
    req = request.get_json()

    if req is None:
        abort(400, description="Not a json")
    if req.get('name') is None:
            abort(400, description='Missing name')
    if type(req['name']) is not str:
        abort(400, description="should be a string of the recipe's name")
    recipe = storage.get(Recipe, None, req['name'])
    if recipe is None:
        abort(404)
    return jsonify(recipe.to_dict())


'''
@app_views.route('/recipes/<ingredients>', methods=['GET'], strict_slashes=False)
def get_recipe(ingredients):
    """
    GET: gets a suggested recipe using entered ingredients
    """
    if type(ingredients) is not str:
        abort(400, description='argument should be a string of ingredients comma separated')

    recipe_suggestions = {'suggested_recipe': recommended_recipes(ingredients)}
    return jsonify(recipe_suggestions)
'''


@app_views.route('/recipe_search/<user_id>/<query>',
                 methods=['POST'], strict_slashes=False)
def search_recipe(user_id, query):
    """
    searches for recipes a user saved
    """
    results = jsonify(storage.similar(Recipe, user_id, query))
    return results


@app_views("/recipes_rating", strict_slashes=False)
def get_average_rating():
    """
    gets average rating on a recipe
    """
     req = request.get_json()

    if req is None:
        abort(400, description="Not a json")
    if req.get('name') is None:
            abort(400, description='Missing name')
    if type(req['name']) is not str:
        abort(400, description="should be a string of the recipe's name")

    recipe = storage.get(Recipe, None, req['name'])
    if recipe is None:
        abort(404)
    total_rating = 0

    for rating in recipe.ratings:
        total_rating += rating.rate_number
    try:
        return total_rating / len(recipe.ratings)
    except ZeroDivisionError:
        return 0
