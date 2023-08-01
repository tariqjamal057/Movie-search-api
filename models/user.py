"""
This module defines the User model for interacting with the "users" table in the database.
"""
from .base import BaseModel, db


class User(BaseModel):
    """
    Represents a user model for interacting with the "users" table in the database.
    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return str(self.name)
