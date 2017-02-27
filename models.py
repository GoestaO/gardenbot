from app import db, login_manager, bcrypt
# from datetime import datetime
import re, datetime
from flask_login import UserMixin


@login_manager.user_loader
def _user_loader(user_id):
    return User.query.get(int(user_id))


def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()


'''The model for a User object'''


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(255))
    name = db.Column(db.String(64))
    slug = db.Column(db.String(64), unique=True)
    active = db.Column(db.Boolean, default=True)
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)  # Call parent constructor

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return "<User: {0}>".format(self.email)

    @staticmethod
    def make_password(plaintext):
        return bcrypt.generate_password_hash(plaintext).decode("UTF_8")

    def check_password(self, raw_password):
        raw_password = raw_password.encode("UTF_8")
        return bcrypt.check_password_hash(self.password_hash, raw_password)

    @classmethod
    def create(cls, email, password, **kwargs):
        return User(
            email=email,
            password_hash=User.make_password(password), **kwargs)

    @staticmethod
    def authenticate(email, password):
        user = User.query.filter(User.email == email).first()
        if user and user.check_password(password):
            return user
        return False


class Protocol(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    watering_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    duration = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Protocol, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Timestamp: {0}; Seconds: {1}'.format(self.watering_timestamp, self.duration)
