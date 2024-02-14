#!/usr/bin/python3
"""Defines tests for Amenity class."""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Defines tests for Amenity class."""
    
    def test_init(self):
        """Test initialization of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_attributes(self):
        """Test Amenity attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        """Test the to_dict method of Amenity."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('id', amenity_dict)
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertIn('created_at', amenity_dict)
        self.assertEqual(amenity_dict['created_at'], amenity.created_at.isoformat())
        self.assertIn('updated_at', amenity_dict)
        self.assertEqual(amenity_dict['updated_at'], amenity.updated_at.isoformat())
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], amenity.name)

    def test_str(self):
        """Test the string representation of Amenity."""
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertIsInstance(amenity_str, str)
        self.assertEqual(amenity_str[:9], "[Amenity]")
        self.assertIn(amenity.id, amenity_str)
        self.assertIn(amenity.name, amenity_str)

if __name__ == '__main__':
    unittest.main()

