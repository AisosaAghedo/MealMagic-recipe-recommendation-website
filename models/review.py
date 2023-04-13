#!/usr/bin/python3
""" holds class Review"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    __tablename__ = 'reviews'
    """definition of the Review class"""
    content = Column(Text)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    recipe_id = Column(String(60), ForeignKey('recipes.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization of a review object"""
        super().__init__(self, *args, **kwargs)

