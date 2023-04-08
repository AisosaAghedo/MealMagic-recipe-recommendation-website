#!/usr/bin/python3
"""api to interact with the users table"""
from . import User
from . import storage
from flask import jsonify, request, abort
from . import app_views



@app_views.route("/users/<user_id>", methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Get: returns a user in JSON format
    """
    user = storage.get(User, user_id)

    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users", methods=['GET', 'POST'],
                 strict_slashes=False)
def get_and_post_users():
    """ 
    GET: returns all users.
    POST: creates and saves a new user
    """
    if request.method == "GET":
        users = []

        for user in storage.all(User).values():
            users.append(user.to_dict())
        return jsonify(users)

    else:
        url_string = '/users/validate/'
        req = request.get_json()

        if req is None:
            abort(400, description="Not a json")
        if req.get('name') is None:
            abort(400, description="Missing name")
        if storage.get(User, None, req['name']):
            abort(400, description="Username is in use")
        if req.get("password") is None:
            abort(400, description="Missing password")
        if req.get('email') is None:
            abort(400, description="Missing email")
        user = User(**req)
        user.save()
        #send_email(user.email, url_string + user.id)
        return jsonify(user.to_dict()), 201



@app_views.route('/users/<user_id>', methods=["PUT", "DELETE"],
                 strict_slashes=False)
def put_and_delete(user_id):
    """
    PUT: updates user information
    DELETE: deletes user account
    """
    user = storage.get(User, user_id)
    if user is None:
            abort(404)

    if request.method == 'PUT':
        restricted_attr = ['id', 'created_at', 'updated_at', 'confirmed']
        req = request.get_json()

        if req is None:
                abort(400, description="Not a json")
        for key in req.keys():
            if key not in restricted_attr:
                """ making sure password is hashed"""
                if key == 'password':
                     user.secure_password(req[key])
                else:
                    setattr(user, key, req[key])
        user.save()
        return jsonify(user.to_dict()), 201

    else:
        storage.delete(user)
        storage.save()
        return jsonify({})
