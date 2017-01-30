import os

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = "postgresql://test:test@localhost:5432/garden"
    SECRET_KEY = 'flask is fun!'  # Create a unique key for your app.
