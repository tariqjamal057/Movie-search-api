"""
This module defines the State model for interacting with the "states" table in the database.
"""
from .base import BaseModel, db


class State(BaseModel):
    """
    Represents a state model for interacting with the "states" table in the database.
    """

    __tablename__ = "states"
    name = db.Column(db.String(100))
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), nullable=False)
    country = db.relationship("Country", backref=db.backref("states", lazy=True))

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return str(self.name)
