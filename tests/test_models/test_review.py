#!/usr/bin/python3
"""
Test module for the Review class.
"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_instance_creation(self):
        """
        Test creation of Review instance.
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes(self):
        """
        Test attributes of Review instance.
        """
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "This place is amazing!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "This place is amazing!")

    def test_to_dict(self):
        """
        Test to_dict method of Review instance.
        """
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "This place is amazing!"
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

    def test_string_representation(self):
        """
        Test string representation of Review instance.
        """
        review = Review()
        string_repr = str(review)
        self.assertTrue(string_repr.startswith('[Review]'))
        self.assertIn(review.id, string_repr)


if __name__ == '__main__':
    unittest.main()
