#!/usr/bin/python3
"""
api endpoints for recipes model
"""
from . import User, Recipe, app_views, storage
from flask import abort, jsonify, request


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

        req['user_id'] = user_id
        recipe = Recipe(**req)
        recipe.save()
        return jsonify(recipe.to_dict()), 201


@app_views.route('recipes/<recipe_name>', methods=['GET'], strict_slashes=False)
def get_recipe(recipe_name):
    """
    GET: gets a recipe using its name
    """
    #implement later on getting data from webscraping
    pass
