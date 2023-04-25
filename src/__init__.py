"""Factor function with settings for the app that allows for different 
configuration e.g. when testing or as a user"""

import os
from flask import Flask
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db

# create_app is the factory function
def create_app(test_config=None):
    """Create main app entry poin"""
    #
    app = Flask(__name__,
                instance_relative_config=True)
    #
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEY_DB_URI")
            )
    # if test_config is not None, then the app is in test mode
    else:
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    db.app = app
    # initialize the database
    db.init_app(app)
    # register Blueprints in the app instance
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    return app
