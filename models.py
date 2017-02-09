from app import db, login_manager
# from datetime import datetime
import re, datetime


@login_manager.user_loader
def _user_loader(user_id):
    return User.query.get(int(user_id))

def slugify(s):
    return re.sub('[^\w]+', '-', s).lower()


'''The model for a User object'''
class User(db.Model):
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
    
    def get_id(self):
        return unicode(self.id)
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return self.active
