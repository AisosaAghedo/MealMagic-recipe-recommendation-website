#!/usr/bin/python3
from . import storage
from . import Review, User, Recipe
from . import app_views
from flask_jwt_extended import jwt_required
from flask import abort, jsonify, request


@app_views.route('/recipes/<recipe_id>/reviews',
                 methods=['GET'], strict_slashes=False)
@jwt_required()
def get_reviews(recipe_id):
    """
    gets all reviews under a particular recipe
    """
    recipe = storage.get(Recipe, recipe_id)
    reviews = []

    if recipe is None:
        abort(404)
    
    for review in recipe.reviews:
        reviews.append(review.to_dict())
    return jsonify(reviews)


@app_views.route('/recipes/<recipe_id>/<user_id>/reviews',
                 methods=['POST'], strict_slashes=False)
@jwt_required()
def user_review(recipe_id, user_id):
    """
    adds a new review by a user
    """
    recipe = storage.get(Recipe, recipe_id)
    req = request.get_json()
    user = storage.get(User, user_id)

    if user is None or recipe is None:
        abort(404)
    if req is None:
        abort(400, description="Not a json")
    if req.get("content") is None:
        abort(400, description="Missing content")

    req['user_id'] = user_id
    req['recipe_id'] = recipe_id
    review = Review(**req)
    review.save()
    return jsonify(review.to_dict())


@app_views.route('reviews/<review_id>', strict_slashes=False)
@jwt_required()
def review_get(review_id):
    """GET:gets a review using its id"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    return jsonify(review.to_dict())


@app_views.route('reviews/<review_id>', methods=['DELETE', 'PUT'],
                 strict_slashes=False)
@jwt_required(fresh=True)
def review(review_id):
    """DELETE: deletes a review, PUT: updates a review"""
    review = storage.get(Review, review_id)

    if review is None:
        abort(404)

    if request.method == 'PUT':
        restricted_attr = ['id', 'created_at', 'updated_at']
        req = request.get_json()

        if req is None:
            abort(400, description="Not a json")
        if req.get('content') is None:
            abort(400, description='Missing content')

        for key in req.keys():
            if key not in restricted_attr:
                setattr(review, key, req[key])
        review.save()
        return jsonify(review.to_dict()), 201

    else:
        storage.delete(review)
        storage.save()
        return jsonify({})
