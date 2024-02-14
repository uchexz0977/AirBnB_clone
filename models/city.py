#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city."""

    def __init__(self, *args, **kwargs):
        """Initialize a new City instance."""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', "")
        self.name = kwargs.get('name', "")

    def to_dict(self):
        """Return a dictionary representation of the City instance."""
        city_dict = super().to_dict()
        city_dict.update({
            'state_id': self.state_id,
            'name': self.name,
        })
        return city_dict

    def __str__(self):
        """Return the string representation of the City instance."""
        return "[City] ({}) {}".format(self.id, self.__dict__)

