#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state."""

    def __init__(self, *args, **kwargs):
        """Initialize a new State instance."""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")

    def to_dict(self):
        """Return a dictionary representation of the State instance."""
        state_dict = super().to_dict()
        state_dict['name'] = self.name
        return state_dict

    def __str__(self):
        """Return the string representation of the State instance."""
        return "[State] ({}) {}".format(self.id, self.name)

