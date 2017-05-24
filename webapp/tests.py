import unittest
from main import app, db
from models import User
import requests


class TestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://gardenbot:gardenbot@localhost:3306/gardenbottest"
        self.app = app.test_client()
        db.create_all()
        self.createUser()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        pass

    @staticmethod
    def createUser():
        u = User.create("test123@huhu.com", "huhu")
        db.session.add(u)
        db.session.commit()

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

        ''' sends HTTP GET request to the application
        on the specified path '''
    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = self.app.get("/status")
        self.assertEqual(response.status_code, 200)


    def test_authenticate(self):
        test_user = User.authenticate("test123@huhu.com", "huhu")
        self.assertIsInstance(test_user, User)




if __name__ == '__main__':
    unittest.main()
