#!/usr/bin/python3
""" holds class Rating"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Rating(BaseModel, Base):
    __tablename__ = 'ratings'
    """definition of the Rating class"""
    rate_number = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    recipe_id = Column(String(60), ForeignKey('recipes.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization of a Rating object"""
        super().__init__(self, *args, **kwargs)
