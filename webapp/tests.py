import unittest
from app import app, db


class TestCase(unittest.TestCase):


    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://gardenbot:gardenbot@osmc.local:3306/gardenbot"
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


