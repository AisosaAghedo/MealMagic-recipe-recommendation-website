#!/usr/bin/python3
"""
handling of the ratings api view
"""
from . import Rating, User, Recipe
from flask import abort, jsonify, request
from . import app_views, storage


@app_views.route("/recipe/<recipe_id>/ratings", strict_slashes=False)
def recipe_ratings(recipe_id):
    """
    GET: retrives the ratings on a recipe
    """
    ratings = []
    recipe = storage.get(Recipe, recipe_id)

    if recipe is None:
        abort(404)
    for rating in recipe.ratings:
        ratings.append(rating.to_dict())

    return (jsonify(ratings))


@app_views.route("/recipe/<recipe_id>/<user_id>/ratings", methods=["POST"],
                 strict_slashes=False)
def post_rating(recipe_id, user_id):
    """
    POST: adds a new rating to the recipe
    """
    recipe = storage.get(Recipe, recipe_id)
    user = storage.get(User, user_id)
    req = request.get_json()

    if recipe is None or user is None:
        abort(404)
    if req is None:
        abort(400, description='Not a json')
    if req.get('rate_number') is None:
        abort(400, description="rate_number is missing")

    kwargs = {"user_id": user_id, 'rate_number': req['rate_number']}
    kwargs["recipe_id"] = recipe_id
    rating = Rating(**kwargs)
    rating.save()
    return jsonify(rating.to_dict()), 201


@app_views.route("/ratings/<rating_id>", methods=["PUT"], strict_slashes=False)
def update_rating(rating_id):
    """
    updates a row on the ratings table
    """
    rating = storage.get(Rating, rating_id)
    req = request.get_json()

    if req is None:
        abort(400, description="Not a json")
    if req.get('rate_number') is None:
        abort(400, description='Missing rate_number')

    rating.rate_number = req['rate_number']
    rating.save()
    return jsonify(rating.to_dict()), 201
