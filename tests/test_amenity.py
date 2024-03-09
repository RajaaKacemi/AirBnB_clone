#!/usr/bin/python3
"""
Test module for the Amenity class.
"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_instance_creation(self):
        """
        Test creation of Amenity instance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """
        Test attributes of Amenity instance.
        """
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

    def test_to_dict(self):
        """
        Test to_dict method of Amenity instance.
        """
        amenity = Amenity()
        amenity.name = "WiFi"
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('name', amenity_dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

    def test_string_representation(self):
        """
        Test string representation of Amenity instance.
        """
        amenity = Amenity()
        string_repr = str(amenity)
        self.assertTrue(string_repr.startswith('[Amenity]'))
        self.assertIn(amenity.id, string_repr)


if __name__ == '__main__':
    unittest.main()
