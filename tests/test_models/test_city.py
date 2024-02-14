#!/usr/bin/python3
"""Defines tests for City class."""

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Defines tests for City class."""
    
    def test_init(self):
        """Test initialization of City."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_attributes(self):
        """Test City attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        """Test the to_dict method of City."""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIn('id', city_dict)
        self.assertEqual(city_dict['id'], city.id)
        self.assertIn('created_at', city_dict)
        self.assertEqual(city_dict['created_at'], city.created_at.isoformat())
        self.assertIn('updated_at', city_dict)
        self.assertEqual(city_dict['updated_at'], city.updated_at.isoformat())
        self.assertIn('state_id', city_dict)
        self.assertEqual(city_dict['state_id'], city.state_id)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['name'], city.name)

    def test_str(self):
        """Test the string representation of City."""
        city = City()
        city_str = str(city)
        self.assertIsInstance(city_str, str)
        self.assertEqual(city_str[:6], "[City]")
        self.assertIn(city.id, city_str)
        self.assertIn(city.state_id, city_str)
        self.assertIn(city.name, city_str)

if __name__ == '__main__':
    unittest.main()

