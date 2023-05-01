"""Factor function with settings for the app that allows for different 
configuration e.g. when testing or as a user"""

import os
from flask import Flask
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db

# create_app is the factory function
def create_app(test_config=None):
    """Create main app entry point"""
    # create and configure the app
    app = Flask(__name__,
                instance_relative_config=True)
    # load the instance config, if it exists, when not testing
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI")
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

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY=os.environ.get("SECRET_KEY"),
#         DATABASE=os.path.join(app.instance_path, 'src.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # register Blueprints in the app instance
#     app.register_blueprint(auth)
#     app.register_blueprint(bookmarks)

#     return app