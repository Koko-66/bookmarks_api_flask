import random
import string
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """User class"""
    id = db.Column(db.Integer, primary_key=True) # will be incremented and managed automatically
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    bookmarks = db.relationship('Bookmark', backref="user")

    def __repr__(self) -> str:
        """Stringfy method"""
        return 'User>>>{self.user_name}'


class Bookmark(db.Model):
    """Bookmark class"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    short_url = db.Column(db.String(3), nullable=True)
    visits = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def generate_short_characters(self):
        """Generate 3 char. short url"""
        characters = string.digits+string.ascii_letters
        picked_chars = ''.join(random.choices(characters, k=3))

        # Query existing links to check if the same one already exists
        link=self.query.filter_by(short_url=picked_chars).first()

        if link:
            # If this link already exists
            self.generate_short_characters
        else:
            return picked_chars


    def __init__(self, **kwargs):
        """Override constructor to create short url autmatically"""
        super().__init__(**kwargs)
        self.short_url = self.generate_short_characters()

    def __repr__(self) -> str:
        """Stringfy method"""
        return 'User>>>{self.url}'
