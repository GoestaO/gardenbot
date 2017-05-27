import unittest
from main import app, db
from models import User
import requests
from forms import LoginForm
from flask import request, Response
from flask_login import login_user, logout_user
import json

class TestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://gardenbot:gardenbot@localhost:3306/gardenbottest"
        self.app = app.test_client()
        db.create_all()
        TestCase.createTestUser()
        self.loginForm = TestCase.createTestLoginForm()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        pass

    @staticmethod
    def createTestLoginForm():
        """Creates a pre filled LoginForm to test login fucntionality"""

        login_form = LoginForm()
        login_form.email.data = "test123@huhu.com"
        login_form.password.data = "huhu"
        return login_form

    @staticmethod
    def createTestUser():
        u = User.create("test123@huhu.com", "huhu")
        db.session.add(u)
        db.session.commit()

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_home(self):
        """sends HTTP GET request to the application
               on the specified path"""
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200, "Error: '/' is 404")

    # def test_status(self):
    #     response = self.app.get("/status")
    #     self.assertEqual(response.status_code, 200, "Error: /status is 404")

    def test_authenticate(self):
        test_user = User.authenticate("test123@huhu.com", "huhu")
        self.assertIsNotNone(test_user, "Authenticate error: Is not None")
        self.assertIsInstance(test_user, User, "test_user is not an instance of User")

    def test_loginForm_validation(self):
        self.assertTrue(self.loginForm.validate(), "Error in validation of LoginForm")

    def test_login_post(self):
        data = dict(email="gösta@huhu.com", password="huhu")
        content_type = "application/x-www-form-urlencoded"
        response = self.app.post('/login', data=data, content_type=content_type)
        self.assertTrue(response.status_code is not None, "Error in Login via Post: Not found")


    def logout(self):
        return self.app.get('/logout', follow_redirects=True)


if __name__ == '__main__':
    unittest.main()
