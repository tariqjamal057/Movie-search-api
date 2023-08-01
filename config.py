"""
Module contains the configuration for the application
"""
from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    The above class defines configuration settings for a application
    """

    DEBUG = False
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    The DevelopmentConfig class is a subclass of the Config class and sets the
    DEBUG attribute to True.
    """

    DEBUG = True


class ProductionConfig(Config):
    """
    The `ProductionConfig` class is a subclass of the `Config` class.
    """

    pass  # pylint: disable=unnecessary-pass


# Set the app configuration class based on an environment variable or a default option
import os

if os.environ.get("FLASK_ENV") == "production":
    app_config = ProductionConfig
else:
    app_config = DevelopmentConfig
