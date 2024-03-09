#!/usr/bin/python3
"""
Test module for the User class.
"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_instance_creation(self):
        """
        Test creation of User instance.
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes(self):
        """
        Test attributes of User instance.
        """
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict(self):
        """
        Test to_dict method of User instance.
        """
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    def test_string_representation(self):
        """
        Test string representation of User instance.
        """
        user = User()
        string_repr = str(user)
        self.assertTrue(string_repr.startswith('[User]'))
        self.assertIn(user.id, string_repr)


if __name__ == '__main__':
    unittest.main()
