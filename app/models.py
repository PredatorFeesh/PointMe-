from app import db
from app import login_manager

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), index=True, unique=True)
    salt = db.Column(db.String(100))
    password = db.Column(db.String(1024))