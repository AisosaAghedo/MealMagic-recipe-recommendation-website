#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/meal_magic')


from models import storage
from models.recipe import Recipe
from models.user import User

from .users import *
from .recipes import *
