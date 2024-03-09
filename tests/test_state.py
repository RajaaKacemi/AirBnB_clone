#!/usr/bin/python3
"""
Test module for the State class.
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_instance_creation(self):
        """
        Test creation of State instance.
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")

    def test_attributes(self):
        """
        Test attributes of State instance.
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict(self):
        """
        Test to_dict method of State instance.
        """
        state = State()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('name', state_dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)

    def test_string_representation(self):
        """
        Test string representation of State instance.
        """
        state = State()
        string_repr = str(state)
        self.assertTrue(string_repr.startswith('[State]'))
        self.assertIn(state.id, string_repr)


if __name__ == '__main__':
    unittest.main()
