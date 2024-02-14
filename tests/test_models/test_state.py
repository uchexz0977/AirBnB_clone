#!/usr/bin/python3
"""Defines tests for State class."""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Defines tests for State class."""
    
    def test_init(self):
        """Test initialization of State."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_attributes(self):
        """Test State attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        """Test the to_dict method of State."""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIn('id', state_dict)
        self.assertEqual(state_dict['id'], state.id)
        self.assertIn('created_at', state_dict)
        self.assertEqual(state_dict['created_at'], state.created_at.isoformat())
        self.assertIn('updated_at', state_dict)
        self.assertEqual(state_dict['updated_at'], state.updated_at.isoformat())
        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['name'], state.name)

    def test_str(self):
        """Test the string representation of State."""
        state = State()
        state_str = str(state)
        self.assertIsInstance(state_str, str)
        self.assertEqual(state_str[:7], "[State]")
        self.assertIn(state.id, state_str)
        self.assertIn(state.name, state_str)

if __name__ == '__main__':
    unittest.main()

