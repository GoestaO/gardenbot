import os

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    APPLICATION_ROOT = "gardenbot"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://gardenbot:gardenbot@osmc.local:3306/gardenbot"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://GoestaO:cj4h8ofm@GoestaO.mysql.pythonanywhere-services.com:3306/gardenbot"
    SECRET_KEY = '000b3d18-7f83-4515-ab66-99199cbbd074'  # Create a unique key for your app.

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}:{port}/{databasename}".format(
    username="sql11186742",
    password="WmI7jJHdMm",
    port=3306,
    hostname="sql11.freemysqlhosting.net",
    databasename="sql11186742",
    )

    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False
