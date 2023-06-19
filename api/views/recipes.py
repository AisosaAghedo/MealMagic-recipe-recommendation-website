#!/usr/bin/python3
"""
api endpoints for recipes model
"""
from . import User, Recipe, app_views, storage
from flask import abort, jsonify, request
from helpers import cache
import json
from engine_src.recommender import recommend_recipes
from ast import literal_eval


@app_views.route('/get_recipes', methods=['POST'],
strict_slashes=False)
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
    recipe['directions'] = literal_eval(recipe['directions'])
    recipe['ingredients'] = literal_eval(recipe['ingredients'])
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
