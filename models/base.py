"""
This module defines a BaseModel class and provides common functionality for interacting 
with the database.

Classes:
    BaseModel: An abstract model that includes common attributes and methods 
    for database operations.
"""
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    """
    An abstract model that includes common attributes for database models.
    """

    __abstract__ = True  # This makes it an abstract model

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def save(self):
        """
        Save the current object to the database.

        This function adds the current object to the session and commits the
        changes to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Sets the `deleted_at` attribute of the current object to the current UTC datetime,
        and commits the changes to the database session.
        """
        self.deleted_at = datetime.utcnow()
        db.session.commit()

    def restore(self):
        """
        Restores the deleted_at attribute of the object and commits the changes to the database.

        This function sets the deleted_at attribute of the object to None and saves the
        changes to the database using the commit() method of the db.session object.
        """
        self.deleted_at = None
        db.session.commit()

    def hard_delete(self):
        """
        Deletes the current object from the database.

        This function removes the current object from the database by calling the `delete`
        method of the `db.session` object. After the deletion, the changes are committed
        to the database by calling the `commit` method of the `db.session` object.
        """
        db.session.delete(self)
        db.session.commit()
