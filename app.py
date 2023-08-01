"""
This module initializes the Flask application and sets up the database.

It creates a Connexion application, sets up the API using the "swagger.yml" specification file,
and initializes the Flask app with the appropriate configuration. The database (SQLAlchemy)
is also initialized and configured.

Classes and Objects:
    - connex_app (connexion.App): The Connexion application instance.
    - app (Flask app): The Flask app instance.
    - Migrate (class): A class for handling database migrations.
"""
import connexion
from flask_migrate import Migrate

from config import app_config
from models import db

connex_app = connexion.App(__name__, specification_dir="./")
connex_app.add_api("swagger.yml")

app = connex_app.app
app.config.from_object(app_config)
db.init_app(app)

Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True)

from models import *  # pylint: disable=wildcard-import
