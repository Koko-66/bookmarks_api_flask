from flask import Blueprint


auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.route("/register", methods=['POST'])
def register():
    """Register user"""
    return "User created"


@auth.route("/me", methods=['GET'])
def me():
    """Show user"""
    return {"user": "me"}