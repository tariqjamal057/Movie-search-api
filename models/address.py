"""
This module defines the Address model for interacting with the "address" table in the database.
"""
from .base import BaseModel, db


class Address(BaseModel):
    """
    Represents a address model for interacting with the "addresses" table in the database.
    """

    __tablename__ = "addresses"
    street = db.Column(db.String(200))
    city = db.Column(db.String(100))
    postal_code = db.Column(db.String(20))
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"))
    state = db.relationship("State", backref=db.backref("addresses", lazy=True))

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return str(self.city + ", " + self.state.name)
