import os

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = "mysql://gardenbot:gardenbot@localhost:3306/gardenbot"
    SECRET_KEY = '000b3d18-7f83-4515-ab66-99199cbbd074'  # Create a unique key for your app.
