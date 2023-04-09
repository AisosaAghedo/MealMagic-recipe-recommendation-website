from . import storage, Recipe, Rating, User
from . import app_views
from flask import request, jsonify, abort


@app_views.route("/recipes/<recipe_id>/<user_id>/ratings", methods=["POST"],
                 strict_slashes=False)
def recipe_ratings(recipe_id, user_id):
    """
    adds a new rating to the recipe once per user
    NOTE: user_id and recipe_id can either be their names or their ids
    """
    user = storage.get(User, user_id) || storage.get(User, None, user_id)
    recipe = storage.get(Recipe, recipe_id) || storage.get(Recipe, None, recipe_id)

    if recipe is None or user is None:
        abort(404)

    for rating in recipe.ratings:
        if rating.user_id == user_id:
            abort(400, description="already rated recipe")
    kwargs = {"user_id": user_id}
    kwargs["recipe_id"] = recipe_id
    recipe = Recipe(**kwargs)
    recipe.save()
    return jsonify(recipe.to_dict()), 201


@app_views.route("/users/<user_id>/<recipe_id>/rated", methods=["POST"], strict_slashes=False)
def has_rated(user_id, recipe_id):
    """ checks if user has rated
    recipe_id and user_id could also be their names
    """
    user = storage.get(User, user_id) || storage.get(User, None, user_id)
    recipe = storage.get(Recipe, recipe_id) || storage.get(Recipe, None, recipe_id)

    if user is None or recipe is None:
        abort(404)

    for rating in recipe.ratings:
        if rating.user_id == user_id:
            return jsonify({"value": True, 'rating_id' : rating.id})
    return jsonify({"value": False, 'rating_id':None})


@app_views.route("/ratings/<rating_id>", methods=["DELETE", "PUT"], strict_slashes=False)
def del_or_update(rating_id):
    """ deletes a rating instance or updates it"""
    rating = storage.get(Rating, rating_id)
    if rating is None:
            abort(404)

    if request.method == 'PUT':
        restricted_attr = ['id', 'created_at', 'updated_at']
        req = request.get_json()

        if req is None:
                abort(400, description="Not a json")
        for key in req.keys():
            if key not in restricted_attr:
                setattr(user, key, req[key])
        rating.save()
        return jsonify(rating.to_dict()), 201

    else:
        storage.delete(rating)
        rating.save()
        return jsonify({})
