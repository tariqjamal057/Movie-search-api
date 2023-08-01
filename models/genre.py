"""
This module defines the Genre model for interacting with the "genres" table in the database.
"""
from .base import BaseModel, db


class Genre(BaseModel):
    """
    Represents a genre model for interacting with the "genres" table in the database.
    """

    __tablename__ = "genres"
    name = db.Column(db.String(100))
    movie = db.relationship("Movie", backref="genre", lazy="dynamic")

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return str(self.name)
