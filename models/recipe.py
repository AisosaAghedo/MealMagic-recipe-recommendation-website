#!/usr/bin/python3
""" holds class Recipe"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

class Recipe(BaseModel, Base):
    __tablename__ = 'recipes'
    """definition of the Recipe class"""
    name = Column(String(100), nullable=False, unique=True)
    img_url = Column(String(100))
    ingredients = Column(Text)
    directions = Column(Text)
    recipe_url = Column(String(100))
    users = relationship('User', back_populates='saved_recipes', secondary='link')
    reviews = relationship("Review", backref="recipe", cascade = "all, delete, delete-orphan")
    ratings = relationship("Rating", backref="recipe", cascade = "all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialization of a Recipe object"""
        super().__init__(self, *args, **kwargs)
