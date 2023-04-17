#!/usr/bin/python3
"""
definition of blueprint to handle
functionalities involving user aithentication
"""

from flask import Blueprint, request, jsonify
from models import storage
from models.user import User
from flask_jwt_extended import create_access_token
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


    if user is None or user.confirm_pwd(password) is False:
        return jsonify({"msg": "Please check your login details and try again"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@auth.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response
