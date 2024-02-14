#!/usr/bin/python3
""" this script defines test for filestorage """
import unittest
from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.file_content = {
            "BaseModel.1234": {
                "__class__": "BaseModel",
                "id": "1234",
                "name": "TestObject",
                "created_at": "2023-01-01T00:00:00",
                "updated_at": "2023-01-01T00:00:00"
            }
        }

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(file_content))
    def test_reload(self, mock_open):
        """Test reload method."""
        storage.reload()
        self.assertEqual(storage.all()["BaseModel.1234"].name, "TestObject")

    @patch("builtins.open", new_callable=mock_open)
    def test_save(self, mock_open):
        """Test save method."""
        obj = BaseModel(name="TestObject")
        storage.new(obj)
        storage.save()
        mock_open.assert_called_with(storage.__file_path, "w")

    def test_all(self):
        """Test all method."""
        obj = BaseModel(name="TestObject")
        storage.new(obj)
        self.assertEqual(storage.all()["BaseModel.{}".format(obj.id)], obj)

    def test_new(self):
        """Test new method."""
        obj = BaseModel(name="TestObject")
        storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), storage.__objects)


if __name__ == "__main__":
    unittest.main()

