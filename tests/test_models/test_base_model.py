#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Test the initialization of a BaseModel instance."""
        base_model = BaseModel()
        self.assertEqual(base_model.id, None)
        self.assertEqual(base_model.created_at, None)
        self.assertEqual(base_model.updated_at, None)

    def test_save(self):
        """Test the save method of the BaseModel class."""
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(base_model.created_at, None)
        self.assertNotEqual(base_model.updated_at, None)
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class."""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], "BaseModel")
        self.assertEqual(base_model_dict['id'], None)
        self.assertEqual(base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'], base_model.updated_at.isoformat())

    def test_str(self):
        """Test the string representation of the BaseModel class."""
        base_model = BaseModel()
        base_model_str = str(base_model)
        self.assertEqual(base_model_str[:10], "[BaseModel] (")
        self.assertEqual(base_model_str[-1], ")")
        self.assertIn(base_model.id, base_model_str)
        self.assertIn(str(base_model.created_at), base_model_str)
        self.assertIn(str(base_model.updated_at), base_model_str)

    def test_init_with_kwargs(self):
        """
        Test for the __init__ method with kwargs.
        """
        kwargs = {
            'id': 'test_id',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-01T00:00:00.000000',
            'name': 'test_name',
            'value': 123
        }
        base_model = BaseModel(**kwargs)
        self.assertEqual(base_model.id, kwargs['id'])
        self.assertEqual(base_model.created_at, datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base_model.updated_at, datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base_model.name, kwargs['name'])
        self.assertEqual(base_model.value, kwargs['value'])


if __name__ == "__main__":
    unittest.main()

