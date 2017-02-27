from unittest import TestCase
from models import User

class TestUser(TestCase):

    def setUp(self):
        self.user = User.create("goesta.o@gmail.com", "cj4h8ofm")

    # def test_make_password(self):


    def test_check_password(self):
        self.assertTrue(self.user.check_password("cj4h8ofm"))

    def test_create(self):
        self.assertIsInstance(self.user, User, 'Object is not an user instance')

    def test_authenticate(self):
        testUser = User.authenticate("goesta.o@gmail.com", "cj4h8ofm")
        self.assertIsInstance(testUser, User)
