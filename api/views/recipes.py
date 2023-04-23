#!/usr/bin/python3
"""
api endpoints for recipes model
"""
from . import User, Recipe, app_views, storage
from flask import abort, jsonify, request
from helpers import cache
import json
from engine_src.recommender import recommend_recipes

@app_views.route("/users/<user_id>/recipes", methods=['GET', 'POST'], strict_slashes=False)
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
            abort(400, description='recipe unavailable')
        recipe.users.append(user)
        recipe.save()
        recipe = recipe.to_dict()
        del recipe['users']
        return jsonify(recipe), 201


@app_views.route('/get_recipes', strict_slashes=False)
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

    value = cache.get_value(req['name'])
    # checks if the recipe is cached in redis if yes, converts from string to json
    if value:
        recipe = json.loads(value)
    else:
        # caches the recipe in redis otherwise as string
        recipe = storage.get(Recipe, None, req['name'])
        if recipe is not None:
            recipe = recipe.to_dict()
            if recipe.get('users'):
                del recipe['users']
            cache.set_value(req['name'], json.dumps(recipe))
    if recipe is None:
        abort(404)
    return jsonify(recipe)


@app_views.route('/recipes/ingredients', methods=['POST'], strict_slashes=False)
def get_recipe():
    """
    GET: gets a suggested recipe using entered ingredients
    """
    req = request.get_json()

    if req is None:
        abort(400, description="Not a json")
    if req.get('ingredients') is None:
            abort(400, description='Missing ingredients')
    if type(req['ingredients']) is not str:
        abort(400, description="should be a string of ingredients")

    recipe_suggestions = {'suggested_recipe': recommend_recipes(req['ingredients'])}
    return jsonify(recipe_suggestions)


@app_views.route('/recipe_search/<user_id>',
                 methods=['GET'], strict_slashes=False)
def search_recipe(user_id):
    """
    searches for recipes a user saved
    """
    req = request.get_json()
    user = storage.get(User, user_id)

    if user is None:
        abort(400, description="Not a user")

    if req is None:
        abort(400, description="Not a json")
    if req.get('query') is None:
            abort(400, description='Missing query')
    if type(req['query']) is not str:
        abort(400, description="should be a query string")
    results = jsonify(storage.similar(Recipe, user_id, req["query"]))
    return results


@app_views.route("/recipes_rating", strict_slashes=False)
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
