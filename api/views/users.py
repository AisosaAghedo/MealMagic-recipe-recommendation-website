#!/usr/bin/python3
"""api to interact with the users table"""
from . import User
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from helpers.random_string import string_gen
from . import storage
from flask import jsonify, request, abort, redirect
from . import app_views
from helpers.send_email import send_email
from flask_cors import cross_origin
HOST = 'http://127.0.0.1:5000/'
FRONT_END_HOST = 'http://localhost:5173/login'

@app_views.route('/users/validate/<user_id>')
def validate(user_id):
    """
    validates user account
    """
    user = storage.get(User, id=user_id)
    if user is None:
        abort(404)
    user.confirmed = True
    user.save()
    return redirect(FRONT_END_HOST)


@app_views.route('/users/forgot_passwords/<email>')
def change_password(email):
    """
    changes password of a user
    """
    user = storage.get(User, email=email)
    new_password = string_gen(10)

    if user is None:
        abort(404)
    user.secure_password(new_password)
    user.save()
    send_email('Password changed', user.email, new_password)
    return jsonify({'msg': 'password changed'})


@app_views.route("/users", methods=['GET'], strict_slashes=False)
@jwt_required()
def get_user():
    """
    Get: returns a user in JSON format
    """
    current_user = get_jwt_identity()
    user = storage.get(User, current_user['id'])

    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users", methods=['POST'],
strict_slashes=False)
def post_users():
    """ 
    POST: creates and saves a new user
    """
    url_string = HOST + 'api/meal_magic/users/validate/'
    req = request.get_json()

    if req is None:
        abort(400, description="Not a json")
    if req.get('email') is None:
        abort(400, description="Missing email")
    if storage.get(User, email=req['email']):
        abort(400, description="Email is in use")
    if req.get("password") is None:
        abort(400, description="Missing password")
    if req.get('name') is None:
        abort(400, description="Missing name")
    
    user = User(**req)
    user.save()
    send_email('Confirm your email account', user.email, url_string + user.id)
    return jsonify(user.to_dict()), 201


@app_views.route('/users', methods=["PUT", "DELETE"],
                 strict_slashes=False)
@jwt_required(fresh=True)
def put_and_delete():
    """
    PUT: updates user information
    DELETE: deletes user account
    """
    current_user = get_jwt_identity()
    user = storage.get(User, current_user['id'])
     
    if user is None:
            abort(404)

    if request.method == 'PUT':
        restricted_attr = ['id', 'created_at', 'updated_at', 'confirmed', 'email']
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
