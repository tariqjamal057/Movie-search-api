"""
This module defines the routes for a simple Flask application.
"""
from flask import jsonify, render_template


def home():
    """
    Returns a JSON response with a message saying "Hello, World!".
    """
    return jsonify({"message": "Hello, World!"})


def home_data():
    """
    Generates a response containing the rendered "home.html" template.

    :return: The rendered "home.html" template.
    """
    return render_template("home.html")
