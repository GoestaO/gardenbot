import os

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    APPLICATION_ROOT = "gardenbot"
    SECRET_KEY = '000b3d18-7f83-4515-ab66-99199cbbd074'  # Create a unique key for your app.
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{}/{}'.format(APPLICATION_DIR, 'gardenbot.db')
    APPLICATION_PASSWORD = u'$2a$04$0hPiiaPtniIy3HpgbzgEi.Ss532/le3pqOBwxAUThMdVNcvgpMcvC'
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False
