from flask import Blueprint, request, jsonify
import validators
from src.database import User, db
# modules to help encrypt password in database
from werkzeug.security import check_password_hash, generate_password_hash
import src.constants.http_status_codes as constants



auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.route("/register", methods=['GET', 'POST'])
def register():
    """Register user"""
    # grab data posted by the user
    user_name = request.json["user_name"]
    email = request.json["email"]
    password = request.json["password"]

    # Check length of password
    if len(password) < 6:
        return jsonify({"error": "Password is too short"
                        }),constants.HTTP_400_BAD_REQUEST

    # Check length of user_name
    if len(user_name) < 3:
        return jsonify({"error": "User_name is too short"
                        }),constants.HTTP_400_BAD_REQUEST

    # Check if user_name is alphanumeric and doesn't contain spaces
    if not user_name.isalnum() or " " in user_name:
        return jsonify({"error": "User_name can be only alphanumeric and cannot contain spaces"
                        }),constants.HTTP_400_BAD_REQUEST

    # Check if email is valid using validators module
    if not validators.email(email):
        return jsonify({"error": "Your email is not valid"
                        }),constants.HTTP_400_BAD_REQUEST

    # Check if email already exists
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error": "Account with this email already exists"
                        }),constants.HTTP_409_CONFLICT

    # Check if user already exists
    if User.query.filter_by(user_name=user_name).first() is not None:
        return jsonify({"error": "A user with this user_name already exists"
                        }),constants.HTTP_409_CONFLICT
        
    pswd_hash = generate_password_hash(password)

    # Set details for new user
    user = User(user_name=user_name, password=pswd_hash, email=email)
    # Save and commit user in the database
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created", 
        "user": {
            "user_name": user_name,
            "email": email
            }
        }), constants.HTTP_201_CREATED


@auth.route("/me", methods=['GET'])
def me():
    """Show user"""
    return {"user": "me"}
