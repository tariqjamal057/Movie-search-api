"""
This module defines the Movie model for interacting with the "movies" table in the database.
"""
from .base import BaseModel, db


class Movie(BaseModel):
    """
    Represents a movie model for interacting with the "movies" table in the database.
    """

    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text, nullable=True)
    genre = db.Column(db.Integer, db.ForeignKey("genres.id"))
    release_year = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return str(self.title)
