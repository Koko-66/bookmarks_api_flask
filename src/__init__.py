"""Factor function with settings for the app that allows for different 
configuration e.g. when testing or as a user"""

import os
from flask import Flask
from src.auth import auth
from src.bookmarks import bookmarks


def create_app(test_config=None):
    """Create main app entry poin"""
    app = Flask(__name__,
                instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"))
    else:
        app.config.from_mapping(test_config)

    # register Blueprints in the app instance
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    return app