from app import db
#from datetime import datetime
import re, datetime


def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()


'''The model for a User object'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(255))
    name = db.Column(db.String(64))
    created_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)  # Call parent constructor

    def __repr__(self):
        return "<User: {0}>".format(self.email)
