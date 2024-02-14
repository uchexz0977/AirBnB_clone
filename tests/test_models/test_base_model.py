#!/usr/bin/python3
"""Defines tests for BaseModel class."""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Defines tests for BaseModel class."""
    
    def test_init(self):
        """Test initialization of BaseModel."""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save(self):
        """Test the save method of BaseModel."""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIn('id', base_model_dict)
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertIn('created_at', base_model_dict)
        self.assertEqual(base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertIn('updated_at', base_model_dict)
        self.assertEqual(base_model_dict['updated_at'], base_model.updated_at.isoformat())

    def test_str(self):
        """Test the string representation of BaseModel."""
        base_model = BaseModel()
        base_model_str = str(base_model)
        self.assertIsInstance(base_model_str, str)
        self.assertEqual(base_model_str[:10], "[BaseModel")
        self.assertIn(base_model.id, base_model_str)

if __name__ == '__main__':
    unittest.main()

