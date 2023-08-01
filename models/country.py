"""
This module defines the Country model for interacting with the "countries" table in the database.
"""
from .base import BaseModel, db


class Country(BaseModel):
    """
    Represents a country model for interacting with the "countries" table in the database.
    """

    __tablename__ = "countries"
    name = db.Column(db.String(100))

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return str(self.name)
