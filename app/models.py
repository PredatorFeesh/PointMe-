from app import db
import flask_login
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)



class User(db.Model, flask_login.UserMixin ):
    """
    The main user model for our software. This should include the user type and all
    its attributes.
    
    """
    __tablename__ = 'user'

    id = db.Column('id',db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(255))

    authenticated = db.Column(db.Boolean, default=False)

    events = db.relationship("Event", backref="event", lazy="dynamic")
    
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
        
    def followed_events(self): 
        # EVENTS POSTED BY FOLLOWERS
        followed = Event.query.join(
            followers, (followers.c.followed_id == Event.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Event.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Event.timestamp.desc())


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
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
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


