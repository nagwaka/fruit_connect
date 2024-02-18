from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=True)
    product_type = db.Column(db.String(100), nullable=True)
    about_me = db.Column(db.Text, nullable=True)

