#!/usr/bin/python3
"""
Test module for the City class.
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def test_instance_creation(self):
        """
        Test creation of City instance.
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attributes(self):
        """
        Test attributes of City instance.
        """
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_to_dict(self):
        """
        Test to_dict method of City instance.
        """
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)

    def test_string_representation(self):
        """
        Test string representation of City instance.
        """
        city = City()
        string_repr = str(city)
        self.assertTrue(string_repr.startswith('[City]'))
        self.assertIn(city.id, string_repr)


if __name__ == '__main__':
    unittest.main()
