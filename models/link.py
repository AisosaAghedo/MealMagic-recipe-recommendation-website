from models.base_model import Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Link(Base):
    """
    serves to link the user and recipe table
    in a many to many relationship
    """
    __tablename__ = 'link'
    user_id = Column('users_id', String(65), ForeignKey('users.id'), primary_key=True)
    recipe_id = Column('recipes_id', String(65), ForeignKey('recipes.id'), primary_key=True)
