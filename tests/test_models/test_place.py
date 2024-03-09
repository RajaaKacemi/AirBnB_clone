#!/usr/bin/python3
"""
Test module for the Place class.
"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_instance_creation(self):
        """
        Test creation of Place instance.
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes(self):
        """
        Test attributes of Place instance.
        """
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Cozy Cottage"
        place.description = "A cozy cottage in the countryside"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 123.456
        place.longitude = -78.910
        place.amenity_ids = ["001", "002", "003"]

        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.description, "A cozy cottage in the countryside")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 123.456)
        self.assertEqual(place.longitude, -78.910)
        self.assertEqual(place.amenity_ids, ["001", "002", "003"])

    def test_to_dict(self):
        """
        Test to_dict method of Place instance.
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)

    def test_string_representation(self):
        """
        Test string representation of Place instance.
        """
        place = Place()
        string_repr = str(place)
        self.assertTrue(string_repr.startswith('[Place]'))
        self.assertIn(place.id, string_repr)


if __name__ == '__main__':
    unittest.main()
