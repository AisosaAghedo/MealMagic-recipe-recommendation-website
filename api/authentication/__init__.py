#!/usr/bin/python3
"""
definition of blueprint to handle
functionalities involving user aithentication
"""

from flask import Blueprint, request, jsonify, make_response
from models import storage
from models.user import User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

auth = Blueprint('auth', __name__, url_prefix="/auth")


@auth.route("/login", methods=["POST"])
def login():
    """
    logs in user if email and password are valid
    """
    if request.get_json is None:
        return jsonify({"error": "requires json data"}), 400
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = storage.get(User, email=email)

    if user is None or password is None:
        return jsonify({"msg": "Please check your login details and try again"}), 401

    if user.confirm_pwd(password) is False:
        return jsonify({"msg": "Please check your login details and try again"}), 401

    if user.confirmed is False:
         return jsonify({"msg": "Account has not been verified"}), 401

    access_token = create_access_token(identity={'email': email, 'id': user.id}, fresh=True)
    refresh_token = create_refresh_token(identity={'email':email, 'id': user.id})
    return jsonify(
                {"access_token": access_token, "refresh_token": refresh_token}
            )


@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():

        current_user = get_jwt_identity()

        new_access_token = create_access_token(identity=current_user)

        return make_response(jsonify({"access_token": new_access_token}), 200)


@auth.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response
