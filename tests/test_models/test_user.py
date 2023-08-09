#!/usr/bin/python3

"""UnitTests for User Model"""


import unittest
from uuid import uuid4
from models.user import User
from time import sleep
from datetime import datetime
from models import storage

class TestUserModel(unittest.TestCase):
    """Unit Tests for User Model"""

    def test_is_instance(self):
        user = User()
        self.assertEqual(User, type(user))
    
    def test_no_args(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())
    
    def test_id_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.id))

    def test_created_at_is_public_datetime(self):
        user = User()
        self.assertEqual(datetime, type(user.created_at))

    def test_updated_at_is_public_datetime(self):
        user = User()
        self.assertEqual(datetime, type(user.updated_at))

    def test_email_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.email))

    def test_password_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.password))

    def test_first_name_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.first_name))

    def test_last_name_is_public_str(self):
        user = User()
        self.assertEqual(str, type(user.last_name))

    def test_new_instance_in_file_object(self):
        user = User()
        self.assertIn("{}.{}".format(user.__class__.__name__, user.id), storage.all().keys())
        self.assertIn(user, storage.all().values())

    def test_user_unique_uuid(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_different_updated_at(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertNotEqual(user1.updated_at, user2.updated_at)
    
    def test_with_kwargs(self):
        now = datetime.now()
        temp_id = str(uuid4())
        model = User(id=temp_id, created_at=now.isoformat(), updated_at=now.isoformat())
        self.assertEqual(model.id, temp_id)
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)
        

if __name__ == "__main__":
    unittest.main()