from flask import Blueprint


bookmarks = Blueprint("bookmarks", __name__, url_prefix="/api/v1/bookmarks")


@bookmarks.route("/", methods=['GET'])
def get_all():
    """Get all bookmarks"""
    return []
