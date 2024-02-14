#!/usr/bin/python3
"""Defines tests for Review class."""

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Defines tests for Review class."""
    
    def test_init(self):
        """Test initialization of Review."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_attributes(self):
        """Test Review attributes."""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_to_dict(self):
        """Test the to_dict method of Review."""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('id', review_dict)
        self.assertEqual(review_dict['id'], review.id)
        self.assertIn('created_at', review_dict)
        self.assertEqual(review_dict['created_at'], review.created_at.isoformat())
        self.assertIn('updated_at', review_dict)
        self.assertEqual(review_dict['updated_at'], review.updated_at.isoformat())
        self.assertIn('place_id', review_dict)
        self.assertEqual(review_dict['place_id'], review.place_id)
        self.assertIn('user_id', review_dict)
        self.assertEqual(review_dict['user_id'], review.user_id)
        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['text'], review.text)

    def test_str(self):
        """Test the string representation of Review."""
        review = Review()
        review_str = str(review)
        self.assertIsInstance(review_str, str)
        self.assertEqual(review_str[:8], "[Review]")
        self.assertIn(review.id, review_str)
        self.assertIn(review.place_id, review_str)
        self.assertIn(review.user_id, review_str)
        self.assertIn(review.text, review_str)

if __name__ == '__main__':
    unittest.main()
