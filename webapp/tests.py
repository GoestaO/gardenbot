import unittest
from main import app, db
from models import User
import requests


class TestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://gardenbot:gardenbot@osmc.local:3306/gardenbot"
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        pass

        ''' sends HTTP GET request to the application
        on the specified path '''
    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = self.app.get("/status")
        self.assertEqual(response.status_code, 200)

        # def test_make_unique_nickname(self):
        #     u1 = User(name='john', email='5@example.com')
        #     db.session.add(u1)
        #     db.session.commit()
        #     u2 = User(name='huhu', email='4@example.com')
        #     db.session.add(u2)
        #     db.session.commit()
        #     self.assertTrue(u1.email != u2.email)


if __name__ == '__main__':
    unittest.main()
