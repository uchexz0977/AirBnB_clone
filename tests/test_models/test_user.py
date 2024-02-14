#!/usr/bin/python3
"""Defines tests for User class."""

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Defines tests for User class."""
    
    def test_init(self):
        """Test initialization of User."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_attributes(self):
        """Test User attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        """Test the to_dict method of User."""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIn('id', user_dict)
        self.assertEqual(user_dict['id'], user.id)
        self.assertIn('created_at', user_dict)
        self.assertEqual(user_dict['created_at'], user.created_at.isoformat())
        self.assertIn('updated_at', user_dict)
        self.assertEqual(user_dict['updated_at'], user.updated_at.isoformat())
        self.assertIn('email', user_dict)
        self.assertEqual(user_dict['email'], user.email)
        self.assertIn('password', user_dict)
        self.assertEqual(user_dict['password'], user.password)
        self.assertIn('first_name', user_dict)
        self.assertEqual(user_dict['first_name'], user.first_name)
        self.assertIn('last_name', user_dict)
        self.assertEqual(user_dict['last_name'], user.last_name)

    def test_str(self):
        """Test the string representation of User."""
        user = User()
        user_str = str(user)
        self.assertIsInstance(user_str, str)
        self.assertEqual(user_str[:6], "[User]")
        self.assertIn(user.id, user_str)
        self.assertIn(user.email, user_str)

if __name__ == '__main__':
    unittest.main()

