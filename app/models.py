from app import db
import flask_login
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, flask_login.UserMixin ):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'users'

    id = db.Column('user_id',db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(255))

    authenticated = db.Column(db.Boolean, default=False)

    events = db.relationship("Event", backref="event", lazy="dynamic")
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False




class Event(db.Model):
    id = db.Column('event_id', db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(2000))
    location = db.Column(db.String(225))
    start_date = db.Column(db.String(225))
    end_date = db.Column(db.String(225))

    
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user = db.relationship('User')

class Attraction(db.Model):
    id = db.Column('attraction_id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(500))
    location= db.Column(db.String(100))
    link = db.Column(db.String(200))
    date_posted = db.Column(db.String(100))
    image_link = db.Column(db.String(200))

class Post(db.Model):
    id = db.Column('post_id', db.Integer, primary_key=True, autoincrement=True)
