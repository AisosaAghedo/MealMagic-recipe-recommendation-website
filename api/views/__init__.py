#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/meal_magic')


from models import storage
from models.rating import Rating
from models.recipe import Recipe
from models.user import User
from models.review import Review

from .users import *
from .recipes import *
from .ratings import *
from .reviews import *
