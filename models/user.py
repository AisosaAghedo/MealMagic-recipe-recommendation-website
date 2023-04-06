#!/usr/bin/python3
""" holds class User"""
import models
import bcrypt
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin


location = "default.jpg"

class User(BaseModel, Base, UserMixin):
    """Representation of a user """
    __tablename__ = 'users'

    name = Column(String(50), nullable=False, unique=True)
    email =  Column(String(50), nullable=False)
    confirmed = Column(Boolean, default=False)
    password = Column(String(60), nullable=False)
    profile_picture = Column(String(120), default=location)
    saved_recipes = relationship("Recipe", backref="saver", cascade = "all, delete, delete-orphan")
    reviews = relationship("Review", backref="reviewer", cascade = "all, delete, delete-orphan")
    ratings = relationship("Rating", backref="rater", cascade = "all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        if kwargs.get('password') is not None:
            pwd = kwargs['password']
            del kwargs['password']
            self.secure_password(pwd)
        super().__init__(*args, **kwargs)

    def secure_password(self, pwd):
        """ encrypts user password to md5"""
        byte = pwd.encode('utf-8')
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(byte, salt)

    def confirm_pwd(self, pwd):
        """checks if password is correct"""
        user_bytes = pwd.encode('utf-8')
        return bcrypt.checkpw(user_bytes, self.password)
