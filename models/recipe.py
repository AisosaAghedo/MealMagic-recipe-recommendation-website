#!/usr/bin/python3
""" holds class Recipe"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Recipe(BaseModel, Base):
    __tablename__ = 'recipes'
    """definition of the Recipe class"""
    name = Column(String(100), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    reviews = relationship("Review", backref="recipe", cascade = "all, delete, delete-orphan")
    ratings = relationship("Rating", backref="recipe", cascade = "all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialization of a Recipe object"""
        super().__init__(self, *args, **kwargs)
