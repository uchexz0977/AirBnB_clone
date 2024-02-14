#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import unittest
from datetime import datetime
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Tests instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test instantiation with no arguments."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test instantiation with attributes."""
        place = Place(city_id="1", user_id="2", name="Test Place",
                      description="Test description", number_rooms=2,
                      number_bathrooms=1, max_guest=4, price_by_night=100,
                      latitude=40.7128, longitude=-74.0060,
                      amenity_ids=["1", "2"])
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "2")
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.description, "Test description")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["1", "2"])

    def test_default_values(self):
        """Test instantiation with default values."""
        place = Place()
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

    def test_instantiation_with_args_and_kwargs(self):
        """Test instantiation with args and kwargs."""
        place = Place("1", user_id="2")
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "2")


class TestPlaceToDict(unittest.TestCase):
    """Tests for Place to_dict method."""

    def test_to_dict(self):
        """Test to_dict method."""
        place = Place(city_id="1", user_id="2", name="Test Place",
                      description="Test description", number_rooms=2,
                      number_bathrooms=1, max_guest=4, price_by_night=100,
                      latitude=40.7128, longitude=-74.0060,
                      amenity_ids=["1", "2"])
        place_dict = place.to_dict()
        expected = {
            'id': place.id,
            '__class__': 'Place',
            'created_at': place.created_at.isoformat(),
            'updated_at': place.updated_at.isoformat(),
            'city_id': "1",
            'user_id': "2",
            'name': "Test Place",
            'description': "Test description",
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 40.7128,
            'longitude': -74.006,
            'amenity_ids': ["1", "2"]
        }
        self.assertDictEqual(place_dict, expected)


if __name__ == '__main__':
    unittest.main()

