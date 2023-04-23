"""Factor function with settings for the app that allows for different 
configuration e.g. when testing or as a user"""
from flask import Flask


def create_app(test_config=None):
    """Create main app entry poin"""
    app = Flask(__name__,
                instance_relative_config=True)

    if test_config is None:   
        app.config.from_mapping(
            SECRET_KEY="dev")
    else:
        app.config.from_mapping(test_config)
        
    @app.route("/")
    def index():
        return "hello world"

    @app.route("/say_hello")
    def say_hello():
        return {"message": "Hello world"}

    return app